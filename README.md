# Index-based RAG System / Indexalapú RAG Rendszer

*(Scroll down for the Hungarian version / A magyar verzióért görgess lejjebb)*

---

## 🇬🇧 English Version

### About The Project
This project is a Python-based application that combines a classical keyword-based inverted index with a Large Language Model (LLM) to create a robust **Retrieval-Augmented Generation (RAG)** system. The application is capable of reading PDF documents, indexing their contents, and answering user questions based strictly on the relevant document chunks, complete with source citations.

### Key Features
* **PDF Processing & Chunking:** Automatically reads and splits PDF files into manageable chunks to optimize the context window for the LLM.
* **Custom Search Engine:** Implements an inverted index mechanism for fast information retrieval. It uses various scoring and ranking algorithms (such as TF-IDF, BM25, Cosine Similarity, Jaccard, etc.) to find the most relevant document chunks.
* **LLM Integration:** Utilizes the OpenAI API (GPT-4o-mini) to process the retrieved context and generate accurate, context-aware, and cited answers.

### Technologies Built With
* **Python**
* **OpenAI API** (or GitHub Models)
* **Natural Language Processing (NLP)** techniques

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/fengxin02/Index_based_RAG_System.git
   cd Index_based_RAG_System
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate     # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK stopwords data:**
   ```bash
   python -c "import nltk; nltk.download('stopwords')"
   ```

5. **Configure environment variables:**
   Create a `.env` file in the project root:
   ```
   # For OpenAI API
   OPENAI_API_KEY=your-openai-api-key

   # For GitHub Models (free tier)
   GITHUB_TOKEN=your-github-token
   ```

6. **Add your PDF files:**
   Place your PDF documents in the `res/` folder (or update `pdf_direc` in `rag/main.py` to point to your PDF directory).

7. **Run the application:**
   ```bash
   python -m rag.main
   ```

---

## 🇭🇺 Magyar Verzió

### A Projektről
Ez a projekt egy Python alapú alkalmazás, amely egy klasszikus szópéldány-alapú keresőindexet és egy nagy nyelvi modellt (LLM) ötvöz, létrehozva ezáltal egy hatékony **RAG (Retrieval-Augmented Generation)** rendszert. Az alkalmazás képes PDF dokumentumok beolvasására, indexelésére, valamint a felhasználói kérdések releváns dokumentumrészletek alapján történő megválaszolására, forrásmegjelöléssel kiegészítve.

### Főbb Funkciók
* **PDF Feldolgozás:** PDF fájlok automatikus beolvasása és darabolása (chunking) a hatékonyabb LLM kontextuskezelés érdekében.
* **Keresőmotor (Inverted Index):** Fordított index alapú kulcsszavas kereső megvalósítása a releváns információk gyors előkereséséhez. A rendszer többféle rangsorolási algoritmust támogat (TF-IDF, BM25, Koszinusz hasonlóság, Jaccard index).
* **LLM Integráció:** Az OpenAI API (GPT-4o-mini) integrálása a kinyert részletek feldolgozására, hogy a modell pontos és az eredeti szövegre támaszkodó (grounded) válaszokat generáljon.

### Használt Technológiák
* **Python**
* **OpenAI API** (vagy GitHub Models)
* **Természetes Nyelvfeldolgozás (NLP)**

### Telepítés és Beállítás

1. **Repo letöltése:**
   ```bash
   git clone https://github.com/fengxin02/Index_based_RAG_System.git
   cd Index_based_RAG_System
   ```

2. **Virtuális környezet létrehozása (ajánlott):**
   ```bash
   python -m venv venv
   venv\Scripts\activate     # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. **Függőségek telepítése:**
   ```bash
   pip install -r requirements.txt
   ```

4. **NLTK stopwords adatok letöltése:**
   ```bash
   python -c "import nltk; nltk.download('stopwords')"
   ```

5. **Környezeti változók beállítása:**
   Hozz létre egy `.env` fájlt a projekt gyökerében:
   ```
   # OpenAI API-hoz
   OPENAI_API_KEY=your-openai-api-key

   # GitHub Models-hoz (ingyenes)
   GITHUB_TOKEN=your-github-token
   ```

6. **PDF fájlok hozzáadása:**
   Helyezd a PDF dokumentumaidat a `res/` mappába (vagy módosítsd a `pdf_direc` változót a `rag/main.py`-ban a saját PDF mappád elérési útjára).

7. **Alkalmazás futtatása:**
   ```bash
   python -m rag.main
   ```
