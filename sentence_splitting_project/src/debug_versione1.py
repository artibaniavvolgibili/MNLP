import os

cartella_gold = "data/processed"
cartella_pred = "output/sentence_split_versione1"

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
        percorso_pred = os.path.join(cartella_pred, nome_file)

        if not os.path.exists(percorso_pred):
            print("Manca file predetto:", nome_file)
            continue

        frasi_gold = leggi_frasi(percorso_gold)
        frasi_pred = leggi_frasi(percorso_pred)

        set_gold = set(frasi_gold)
        set_pred = set(frasi_pred)

        frasi_mancate = set_gold - set_pred

        print("\n==============================")
        print("FILE:", nome_file)
        print("==============================")

        print("\nFrasi NON trovate dalla Versione 1:")

        if len(frasi_mancate) == 0:
            print("Nessuna")
        else:
            contatore = 1

            for frase in frasi_mancate:
                print(str(contatore) + ".", frase)
                contatore = contatore + 1