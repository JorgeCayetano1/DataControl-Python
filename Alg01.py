import pandas as pd
datos = ""
df = pd.read_excel("Analisis_Twitter2.xlsx")
tabla = pd.DataFrame(df)
quitar = ",;:.\n!\"'"

for i in range(df.shape[0]):
    datos += tabla["Text"][i]



# Los caracteres que no contamos como palabras
quitar = ",;:.\n!\"'"

for caracter in quitar:
    datos = datos.replace(caracter,
                          "")
datos = datos.lower()

palabras = datos.split(" ")

diccionario_frecuencias = {}
for palabra in palabras:
    for i in range(2):
        palabra = ["Cyberbullying", "ver"]
        if palabra[i] in diccionario_frecuencias:
            diccionario_frecuencias[palabra[i]] += 1
        else:
            diccionario_frecuencias[palabra[i]] = 1

for palabra[i] in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra[i]]
    print(f"La palabra '{palabra[i]}' tiene una frecuencia de {frecuencia}")