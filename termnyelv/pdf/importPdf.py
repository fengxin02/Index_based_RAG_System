import os
import fitz as pymu


def openread_pdf(path):

    try:
        doc = pymu.open(path)
        doc_text = []
        for page in doc:
            doc_text.append({
                'page_number': page.number + 1,
                'text': page.get_text("text"),
            })
        doc.close()
        print("Read PDF successfully")
        return doc_text
    except Exception as e:
        print(f"File reading went Wrong!{e}")
        return []

def load_pdf(path):

    domencts = []
    print("start loading PDFs")

    for filename in os.listdir(path):
        if filename.endswith(".pdf"):
            #tejles utvonal kereses
            full_path = os.path.join(path, filename)
            print(f"{full_path}")
            pagecontent = openread_pdf(full_path)

            if pagecontent: domencts.append({
                    'filename': filename,
                    'pages': pagecontent
                })
            else:
                print("PDF is empty")

    return domencts