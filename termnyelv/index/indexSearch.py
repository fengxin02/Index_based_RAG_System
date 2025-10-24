import re

def find_index(pagecontent):
    # ebben taroljuk a szavakat, es helyet
    index = {}
    text = pagecontent['text']
    #szetvalaszt megkeres
    for tok in [i for i in re.split(r'(\d+|\W+)', text) if i]:
        #kis nagy betu ne legyen kulonbseg
        tok = tok.lower()
        if len(tok) < 2:
            continue
        #elso talalat a szora
        if not tok in index:
            index[tok] = 1
        else:
            index[tok] = index[tok] + 1

    return index
    #megtaltalt szo kiir


   #1, 'legjobb' talalat kell llmn-ek -->> megszamolni hanyszor fordul elo ebben az oldalon
#mo: azt majd return
   #2, a szavak nincsenek toldalektalanitva (mennyire fontos???)
   #3, toldalel talanitas jobban mukodne, keresesben es majd llm-nek elott  is jobb igy keresni
   #4, felesleges toldalek szo eltavolitas
   #FK MOODLE IS DEAD :DDD