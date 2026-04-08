import os

cartella_gold = "data/processed"
cartella_v1 = "output/sentence_split_versione1"
cartella_v2 = "output/sentence_split_versione2"

def leggi_frasi(percorso):
    file = open(percorso, "r", encoding="utf-8")
    righe = file.readlines()
    file.close()

    frasi = []

    for riga in righe:
        riga = riga.strip()
        if riga != "":
            frasi.append(riga)

    return frasi

lista_file = os.listdir(cartella_gold)

for nome_file in lista_file:
    if nome_file.endswith(".sent_split"):

        percorso_gold = os.path.join(cartella_gold, nome_file)
        percorso_v1 = os.path.join(cartella_v1, nome_file)
        percorso_v2 = os.path.join(cartella_v2, nome_file)

        if not os.path.exists(percorso_v1):
            print("Manca file versione1:", nome_file)
            continue

        if not os.path.exists(percorso_v2):
            print("Manca file versione2:", nome_file)
            continue

        frasi_gold = leggi_frasi(percorso_gold)
        frasi_v1 = leggi_frasi(percorso_v1)
        frasi_v2 = leggi_frasi(percorso_v2)

        set_gold = set(frasi_gold)
        set_v1 = set(frasi_v1)
        set_v2 = set(frasi_v2)

        mancate_v1 = set_gold - set_v1
        mancate_v2 = set_gold - set_v2

        print("\n==============================")
        print("FILE:", nome_file)
        print("==============================")

        print("\nFrasi NON matchate da VERSIONE 1:")
        if len(mancate_v1) == 0:
            print("Nessuna")
        else:
            contatore = 1
            for frase in mancate_v1:
                print(str(contatore) + ".", frase)
                contatore = contatore + 1

        print("\nFrasi NON matchate da VERSIONE 2:")
        if len(mancate_v2) == 0:
            print("Nessuna")
        else:
            contatore = 1
            for frase in mancate_v2:
                print(str(contatore) + ".", frase)
                contatore = contatore + 1