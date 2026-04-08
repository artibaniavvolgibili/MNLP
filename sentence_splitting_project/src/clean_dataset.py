import os

cartella_input = "data/raw"
cartella_output = "data/processed"

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

        testo = testo.replace("<EOS>", "\n")

        righe = testo.split("\n")
        frasi_pulite = []

        for riga in righe:
            riga = riga.strip()
            if riga != "":
                frasi_pulite.append(riga)

        file_output = open(percorso_output, "w", encoding="utf-8")

        for frase in frasi_pulite:
            file_output.write(frase + "\n")

        file_output.close()

        print("Creato file gold:", nome_file)

print("Pulizia dataset completata.")