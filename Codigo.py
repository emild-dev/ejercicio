meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": " una respuesta a una broma",
            "SHEESH": "ligera desaprobacion",
            "CREEPY": "aterrador,siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            }

print(meme_dict["LOL"])
while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("no se encuentra en la lista de palabras")
