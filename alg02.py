import pandas as pd
datos = ""
df = pd.read_excel("Analisis_Twitter2.xlsx")
tabla = pd.DataFrame(df)
quitar = ",;:.\n!\"'"

for i in range(161):
    datos += tabla["Text"][i]

for caracter in quitar:
    datos = datos.replace(caracter,
                          "")
datos = datos.lower()

palabras = datos.split(" ")

print(palabras)