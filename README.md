# Index-based RAG System / Indexalapú RAG Rendszer

*(Scroll down for the Hungarian version / A magyar verzióért görgess lejjebb)*

---

## 🇬🇧 English Version

### About The Project
This project is a Python-based application that combines a classical keyword-based inverted index with a Large Language Model (LLM) to create a robust **Retrieval-Augmented Generation (RAG)** system. The application is capable of reading PDF documents, indexing their contents, and answering user questions based strictly on the relevant document chunks, complete with source citations.

### Key Features
* **PDF Processing & Chunking:** Automatically reads and splits PDF files into manageable chunks to optimize the context window for the LLM.
* **Custom Search Engine:** Implements an inverted index mechanism for fast information retrieval. It uses various scoring and ranking algorithms (such as TF-IDF, BM25, Cosine Similarity, Jaccard, etc.) to find the most relevant document chunks.
* **LLM Integration:** Utilizes the OpenAI API (GPT-3.5) to process the retrieved context and generate accurate, context-aware, and cited answers.

### Technologies Built With
* **Python**
* **OpenAI API**
* **Natural Language Processing (NLP)** techniques

## 🇭🇺 Magyar Verzió
A Projektről
Ez a projekt egy Python alapú alkalmazás, amely egy klasszikus szópéldány-alapú keresőindexet és egy nagy nyelvi modellt (LLM) ötvöz, létrehozva ezáltal egy hatékony RAG (Retrieval-Augmented Generation) rendszert. Az alkalmazás képes PDF dokumentumok beolvasására, indexelésére, valamint a felhasználói kérdések releváns dokumentumrészletek alapján történő megválaszolására, forrásmegjelöléssel kiegészítve.

### Főbb Funkciók
* **PDF Feldolgozás: PDF fájlok automatikus beolvasása és darabolása (chunking) a hatékonyabb LLM kontextuskezelés érdekében.**

* **Keresőmotor (Inverted Index): Fordított index alapú kulcsszavas kereső megvalósítása a releváns információk gyors előkereséséhez. A rendszer többféle rangsorolási algoritmust támogat (TF-IDF, BM25, Koszinusz hasonlóság, Jaccard index).**

* **LLM Integráció: Az OpenAI API (GPT-3.5) integrálása a kinyert részletek feldolgozására, hogy a modell pontos és az eredeti szövegre támaszkodó (grounded) válaszokat generáljon.**

### Használt Technológiák
* **Python**

* **OpenAI API**

* **Természetes Nyelvfeldolgozás (NLP)**

