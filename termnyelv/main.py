from termnyelv.index.indexSearch import find_index_number, find_index_words
from termnyelv.pdf.importPdf import load_pdf

global_index = {}
pdf_direc = "C:\\Users\\fengx\\PycharmProjects\\termeszetesnyelv_hazi\\res"

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

if __name__ == "__main__":

    docs = load_pdf(pdf_direc)

    #felepiti az indexet
    index_build(docs)

    #teszt dokumentum feldolgozasra
    #doclist(docs)
    search_global("nyelv")
    #search_doc_num("Nyelv",docs)
