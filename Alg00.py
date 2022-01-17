import pandas as pd
datos = ""
df = pd.read_excel("Analisis_Twitter2.xlsx")
tabla = pd.DataFrame(df)
quitar = ",;:.\n!\"'"
 
for i in range(160):
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
    palabra = "Cyberbullying"
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1
    else:
        diccionario_frecuencias[palabra] = 1
 
for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]
    print(f"La palabra '{palabra}' tiene una frecuencia de {frecuencia}")