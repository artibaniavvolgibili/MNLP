import os
import re

cartella_input = "data/raw"
cartella_output = "output/sentence_split_versione1"

if not os.path.exists(cartella_output):
    os.makedirs(cartella_output)

lista_file = os.listdir(cartella_input)

for nome_file in lista_file:
    if nome_file.endswith(".sent_split"):

        percorso_input = os.path.join(cartella_input, nome_file)
        percorso_output = os.path.join(cartella_output, nome_file)

        file_input = open(percorso_input, "r", encoding="utf-8")
        testo = file_input.read()
        file_input.close()

        testo = testo.replace("<EOS>", " ")

        pezzi = re.split(r'(?<=[.!?])\s+', testo)

        frasi_finali = []

        for pezzo in pezzi:
            pezzo_pulito = pezzo.strip()

            if pezzo_pulito != "":
                frasi_finali.append(pezzo_pulito)

        file_output = open(percorso_output, "w", encoding="utf-8")

        for frase in frasi_finali:
            file_output.write(frase + "\n")

        file_output.close()

        print("Creato file:", nome_file)

print("Ho finito.")