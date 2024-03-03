import random

valor_minimo=1
valor_maximo=6

juega_otra_vez="Si"

while juega_otra_vez =="Si" or juega_otra_vez=="S":
    print("Tirando los dados....")
    print("Los numeros son.....")
    print(random.randint(valor_minimo,valor_maximo))
    print(random.randint(valor_minimo,valor_maximo))
    juega_otra_vez = input("Tira los dados otra vez?")



