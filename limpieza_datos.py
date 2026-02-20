import pandas as pd 

data=pd.read_csv("datos_sucios.csv")



print(data.head())
print(data.info())

#Eliminar filas duplicadas
data = data.drop_duplicates()

#Eliminar espacios en blanco al inicio y al final de los nombres
data ["nombre"] = data["nombre"].str.strip()

#Convertir edades negativas a positivas 
data["edad"] = data["edad"].abs()

#Eliminar el texto de pesos en la columna de salario
data["salario"]=data["salario"].astype(str).str.replace("pesos","")

#Convertir la columna de salario a numérica, los valores no convertibles se establecerán como NaN
data["salario"]=pd.to_numeric(data["salario"],errors="coerce")

#Verficar si existen valores nulos en el DataFrame
print(data.isnull().sum())

#Para eliminar salarios nulos 
data=data.dropna()


#Resetear indice 
data = data.reset_index(drop=True)

data.to_csv("datos_limpios.csv",index=False)

print(data.info())

print(data)
