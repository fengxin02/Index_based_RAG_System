from termnyelv.index.indexSearch import find_index
from termnyelv.pdf.importPdf import load_pdf

if __name__ == "__main__":
    pdf_direc = "C:\\Users\\fengx\\PycharmProjects\\termeszetesnyelv_hazi\\res"

    docs = load_pdf(pdf_direc)

    #teszt dokumentum feldolgozasra
#    for doc in docs:
#        print(f"{doc['filename']}")
#        for pagecont in doc['pages']:
#            print(f"Page {pagecont['page_number']}:")
#            print(f"Content: {pagecont['text']}")

    #teszt indexkereses
    word = "az"
    for doc in docs:
        print(doc['filename'])
        for pagecont in doc['pages']:
            index = find_index(pagecont)
            #vagy fuggvenyben vagy kint??
            if word in index:
                print(f"Word founded: {word} in {pagecont['page_number']} times: {index[word]}")
