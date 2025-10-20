from termnyelv.pdf.importPdf import load_pdf

if __name__ == "__main__":
    pdf_direc = "C:\\Users\\fengx\\PycharmProjects\\termeszetesnyelv_hazi\\res"

    docs = load_pdf(pdf_direc)

    for doc in docs:
        print(f"{doc['filename']}")
        for pagecont in doc['pages']:
            print(f"Page {pagecont['page_number']}:")
            print(f"Content: {pagecont['text']}")