from faker import Faker
import pandas as pd
import random
import numpy as np

fake = Faker("es_MX")

data = []

for _ in range(100):

    nombre = fake.name()
    email = fake.email()
    telefono = fake.phone_number()
    edad = random.randint(18, 65)
    salario = random.randint(8000, 50000)

    if random.random() < 0.2:
        edad = -edad  

    if random.random() < 0.2:
        salario = str(salario) + " pesos"  

    if random.random() < 0.2:
        email = None  # nulo

    if random.random() < 0.2:
        nombre = "   " + nombre + "   "  

    data.append({
        "nombre": nombre,
        "email": email,
        "edad": edad,
        "salario": salario
    })

data = pd.DataFrame(data)

data= pd.concat([data, data.iloc[0:5]])

data.to_csv("datos_sucios.csv", index=False)


print(data)