import re
import pandas as pd

datos = []
tab = pd.read_excel("Analisis_Twitter2.xlsx")
df = pd.DataFrame(tab)

for i in range(df.shape[0]):
    datos.append(df["Text"][i])
    favor = re.findall(r'bueno', datos[i])
    contra = re.findall(r'malo', datos[i])
    if favor == False:
        print(f"La fila {i+1} esta a favor del ciberbullying.")
    elif contra != i:
        print(f"La fila {i+1} esta en contra del cyberbullying.")
    else:
        print(f"La fila {i+1} es neutra del cyberbullying.")