import os
import spacy

cartella_input = "data/raw"
cartella_output = "output/sentence_split_spacy"

if not os.path.exists(cartella_output):
    os.makedirs(cartella_output)

modello_inglese = spacy.load("en_core_web_sm")
modello_italiano = spacy.load("it_core_news_sm")

# aumentiamo comunque il limite per sicurezza
modello_inglese.max_length = 2000000
modello_italiano.max_length = 2000000

lista_file = os.listdir(cartella_input)

def dividi_in_blocchi(testo, grandezza_blocco=500000):
    blocchi = []
    inizio = 0

    while inizio < len(testo):
        fine = inizio + grandezza_blocco

        if fine >= len(testo):
            blocchi.append(testo[inizio:])
            break

        pezzo = testo[inizio:fine]

        ultimo_spazio = pezzo.rfind(" ")
        if ultimo_spazio != -1:
            fine = inizio + ultimo_spazio

        blocchi.append(testo[inizio:fine])
        inizio = fine

    return blocchi

for nome_file in lista_file:
    if nome_file.endswith(".sent_split"):

        percorso_input = os.path.join(cartella_input, nome_file)
        percorso_output = os.path.join(cartella_output, nome_file)

        file_input = open(percorso_input, "r", encoding="utf-8")
        testo = file_input.read()
        file_input.close()

        testo = testo.replace("<EOS>", " ")

        if nome_file.startswith("it_"):
            modello = modello_italiano
        else:
            modello = modello_inglese

        blocchi = dividi_in_blocchi(testo, 500000)

        frasi_finali = []

        for blocco in blocchi:
            doc = modello(blocco)

            for frase in doc.sents:
                frase_pulita = frase.text.strip()
                if frase_pulita != "":
                    frasi_finali.append(frase_pulita)

        file_output = open(percorso_output, "w", encoding="utf-8")

        for frase in frasi_finali:
            file_output.write(frase + "\n")

        file_output.close()

        print("Creato file spaCy:", nome_file)

print("Ho finito.")