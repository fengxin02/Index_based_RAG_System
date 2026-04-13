import re

from nltk import SnowballStemmer
from nltk.corpus import stopwords
from openai import OpenAI
import os
from termnyelv.index.indexSearch import find_index_number
from termnyelv.pdf.importPdf import load_pdf
from dotenv import load_dotenv

load_dotenv()
pdf_direc = "C:\\Users\\fengx\\PycharmProjects\\termeszetesnyelv_hazi2\\res"
rag_index = {}

stopword = set(stopwords.words('hungarian'))
stemmer = SnowballStemmer('hungarian')

#chat-gpt-nek kuld promtot
def llm(context, question):
    try:
        #automatikusan kiolvassa az env-bol a keyt
        #ha chatpgt- hasznalsz kommentezd ki a kovetkezo sort
        #openai = OpenAI()

        #ha github (ingyenes) kommentezd ki a kovetkezo sort
        openai = OpenAI(
            base_url="https://models.inference.ai.azure.com",
            api_key=os.environ.get("GITHUB_TOKEN")
        )

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
            model="gpt-4o-mini",
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
    #return  context

#feldolgozza a kerdest es visszaadja a kulcsszot
def pro_question(question):
    keyword = []
    for tok in [i for i in re.split(r'(\d+|\W+)', question) if i]:
        tok = tok.lower()
        tok = stemmer.stem(tok)
        if tok not in stopword and len(tok) > 1:
            keyword.append(tok)

    return keyword

#llm-nek keresre valo index (rag index inicializalas)
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

#RAG indexbol keresi ki a megaadott szavat
def search_global(word):
    word = word.lower()
    word= stemmer.stem(word)
    find_loc = set()
    for place, data in rag_index.items():
        if word in data['counts']:
            find_loc.add(place)

    if len(find_loc) > 0:
        print(f"{word} is in :")
        for place in find_loc:
            print(f"\t{place}")
    else:
        print(f"{word} is not in the documents")


#teszt: kiirja a dokumnetumot
def doc_list(docs):
    for doc in docs:
        print(f"{doc['filename']}")
        for pagecont in doc['pages']:
            print(f"Page {pagecont['page_number']}:")
            print(f"Content: {pagecont['text']}")



if __name__ == "__main__":

    #beolvassa a pdf-eket
    docs = load_pdf(pdf_direc)

    #felepiti az indexet
    rag_index_build(docs)

    #doc_list(docs)
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
    #teszt dokumentum feldolgozasra

    #keys = find_best_part("Mit csinál a nyelv")
    #print(llm(keys, "Mit csinál a nyelv"))

    #doclist(docs)
    #search_global("Péter")
    #search_doc_num("Péter",docs)
    #search_doc_num("Nyelv",docs)
    #keys = pro_question("Milyen kódról beszél?")
    #for key in keys:
     #  print(key)

    #con = find_best_part("Milyen kódról beszél?")
    #print(con)