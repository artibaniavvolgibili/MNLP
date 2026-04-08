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

def divisione_sicura(a, b):
    if b == 0:
        return 0.0
    return a / b

lista_file = os.listdir(cartella_gold)

tutti_risultati = []

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

        veri_positivi = len(set_gold.intersection(set_pred))
        tot_pred = len(set_pred)
        tot_gold = len(set_gold)

        precision = divisione_sicura(veri_positivi, tot_pred)
        recall = divisione_sicura(veri_positivi, tot_gold)

        if precision + recall == 0:
            f1 = 0.0
        else:
            f1 = 2 * precision * recall / (precision + recall)

        risultato = {
            "precision": precision,
            "recall": recall,
            "f1": f1
        }

        tutti_risultati.append(risultato)

        print("\nFile:", nome_file)
        print("Frasi gold     :", tot_gold)
        print("Frasi predette :", tot_pred)
        print("Match esatti   :", veri_positivi)
        print("Precision      :", round(precision, 4))
        print("Recall         :", round(recall, 4))
        print("F1             :", round(f1, 4))

# media finale
if len(tutti_risultati) > 0:
    somma_precision = 0
    somma_recall = 0
    somma_f1 = 0

    for r in tutti_risultati:
        somma_precision += r["precision"]
        somma_recall += r["recall"]
        somma_f1 += r["f1"]

    media_precision = somma_precision / len(tutti_risultati)
    media_recall = somma_recall / len(tutti_risultati)
    media_f1 = somma_f1 / len(tutti_risultati)

    print("\n===== MEDIA COMPLESSIVA =====")
    print("Precision media:", round(media_precision, 4))
    print("Recall media   :", round(media_recall, 4))
    print("F1 media       :", round(media_f1, 4))
else:
    print("Nessun file valutato.")