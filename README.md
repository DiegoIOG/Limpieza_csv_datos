## Limpieza de datos en formato .csv 

Mediante pandas se elimina los errores de datos como lo son los espaciados entre los nombres , el texto en numeros  al igual que duplicados,se convierten los errores de edades a positvo, esto mediante un python generar_datos.py que genera un .csv con datos sucios que luego son limpiados en otro python limpieza_datos.py el cual elimina los errores para genera valores limpios que no interfieran con procesos proximos para esto se genera un nuevo .csv llamado datos_limpios.csv. Una aplicacion mas realista se puede aplicar a datos recibidos de clientes ya sea por compras o manejo dedatos de produccion de esta manera se podria genera una automatizacion que limpia datos para que lleguen limpios a su destino ayudano a eliminar posibles errores en la parte de bussines inteligent mediante la visualizacion de datos para la toma de decisiones.

# Proceso 
Generacion de datos --> Limpieza de datos --> Datos limpios 


# Datos 
Se eliminaron en total 18 datos nulos en el apartado de email y 5 filas duplicadas.
Reducciendo de 106 datos a 78  datos. 

#  Librerías utilizadas

-Pandas 
-Numpy
-Faker

