import pandas as pd

nombres = ['Ana', 'Luis', 'Pedro']
edades = [25, 30, 35]

datos = {'Nombres': nombres, 'Edades': edades}

df = pd.DataFrame(datos)

df.to_excel('datos.xlsx', index=False)
print('Archivo Excel generado con éxito')