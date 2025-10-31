import re

from nltk import SnowballStemmer
from nltk.corpus import stopwords
from openai import OpenAI
import os
from termnyelv.index.indexSearch import find_index_number, find_index_words
from termnyelv.pdf.importPdf import load_pdf


global_index = {}
pdf_direc = "C:\\Users\\fengx\\PycharmProjects\\termeszetesnyelv_hazi\\res"
rag_index = {}

stopword = set(stopwords.words('hungarian'))
stemmer = SnowballStemmer('hungarian')

#chat-gpt-nek kuld promtot
def llm(context, question):
    try:
        openai = OpenAI(api_key="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")
        system_prompt = (
            "Válaszolj a felhasználó kérdésére a meg adott kontextus alapján. Ne használj külső tudást."
        )

        user_prompt = f"""
                kontextus:
                {context}

                kérdés:
                {question}
                """
        print("Sending request to LLM...")
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": user_prompt}
            ]
        )
        return completion.choices[0].message.content

    except Exception as e:
        print(e)

#megkeresi a legmegfelelobb reszt (top2-t valaszt ki)
def find_best_part(question):
    keys = pro_question(question)
    if not keys:
        print("No keywords found in PDF")

    #megszamolja hany x keresett szo van
    pagescore = {}
    for place, data in rag_index.items():
        score = 0
        pagecount = data['counts']
        for key in keys:
            if key in pagecount:
                #hany x szerepelt hozza adja
                score += pagecount[key]
        if score > 0:
            pagescore[place] = score

    if not pagescore:
        print("No info found in PDF")

    #rendezi a score listat ezzel kikeressuk a legjobbat
    sorted_pages = sorted(pagescore.items(), key=lambda item: item[1], reverse=True)

    #a top 2 legjobb eredmeny kuljuk tovabb mmlnek
    top = 2
    #csak a place-t tarja meg
    top_locations = [place for place, score in sorted_pages[0:top]]

    #eredeti szoveg tarolas
    context = []
    for place in top_locations:
        context.append(rag_index[place]['text'])
    context = "\n........................................................................\n".join(context)

    answer = llm(context, question)
    return answer


#feldolgozza a kerdest es visszaadja a kulcsszot
def pro_question(question):
    keyword = []
    for tok in [i for i in re.split(r'(\d+|\W+)', question) if i]:
        tok = tok.lower()
        tok = stemmer.stem(tok)
        if tok not in stopword and len(tok) > 1:
            keyword.append(tok)

    return keyword

#llm-nek keresre valo index
def rag_index_build(docs):

    for doc in docs:
        filename = doc['filename']
        for pagecont in doc['pages']:
            # A hely lesz a kulcs
            place = f"{filename} (page: {pagecont['page_number']})"

            word_counts = find_index_number(pagecont)

            #nyers szoveg es rag_index
            rag_index[place] = {
                'text': pagecont['text'],
                'counts': word_counts
            }

    print("Building rag index successfully.")


def index_build(docs):
    for doc in docs:
        filename = doc['filename']

        for pagecont in doc['pages']:
            #hol van az oldalon
            place = f"{filename} (page: {pagecont['page_number']})"

            words = find_index_words(pagecont)

            for word in words:
                if word not in global_index:
                    global_index[word] = set()
                global_index[word].add(place)

    print("Building global index successfully.")


#globalis indexbol keresi ki a megaadott szavat
#??? kell e stem??????
def search_global(word):
    word = word.lower()
    if word in global_index:
        print(f"The '{word}' word is in the documents:")
        for loc in global_index[word]:
            print(f"  - {loc}")
    else:
        print(f"Can not find '{word}' in documents.")




def doc_list(docs):
    for doc in docs:
        print(f"{doc['filename']}")
        for pagecont in doc['pages']:
            print(f"Page {pagecont['page_number']}:")
            print(f"Content: {pagecont['text']}")


#teszt indexkeresdarabszammal
#ebbol egy listat kene csinalni nem mindig mindenegyes alkalommal lefutni
#last global_index
def search_doc_num(word,docs):
    word = word.lower()
    for doc in docs:
        print(doc['filename'])
        for pagecont in doc['pages']:
            index = find_index_number(pagecont)
             #vagy fuggvenyben vagy kint??
            if word in index:
                print(f"Word founded: {word} in {pagecont['page_number']} times: {index[word]}")

#kell egy olyan index ami a keresett szavat kilistazza hogy hol vannak
# es meg mondja hol fordul elo legtobbszor
if __name__ == "__main__":

    #beolvassa a pdf-eket
    docs = load_pdf(pdf_direc)

    #felepiti az indexet
    index_build(docs)
    rag_index_build(docs)
    #teszt dokumentum feldolgozasra


    while True:
        print("......................................................")
        print("1. Index keresés")
        print("2. ChatGPT kérdezes a pdf kontexusból")
        print("0. kilépés")
        print("......................................................")
        choice = input("írd be a választ: ")
        if choice == "1":
            print("'z'-vel lehet visszamenni a menübe")
            key = input("írd be a keresett szót: ")
            if key == "z":
                continue
            search_global(key)

        elif choice == "2":
            print("'z'-vel lehet visszamenni a menübe")
            question = input("írd be a kérdésedet: ")
            if question == "z":
                continue
            keys = find_best_part(question)
            print(llm(keys, question))

        elif choice == "0":
            break
        else:
            print("0-2ig írj be számokat")


    print("Kilépés a programból")

    #keys = find_best_part("Mit csinál a nyelv")
    #print(llm(keys, "Mit csinál a nyelv"))

    #doclist(docs)
    #search_global("Péter")
    #search_doc_num("Péter",docs)
    #search_doc_num("Nyelv",docs)
   # keys = pro_question("Mit csinál a nyelv?")
    #for key in keys:
    #   print(key)

    #con = find_best_part("Mit csinál a nyelv")
    #print(con)