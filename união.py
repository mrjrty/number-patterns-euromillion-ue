import pandas as pd
import numpy as np
from itertools import chain
from collections import Counter
lista_valores = []
lista_estrelas = []

print("Olá Paloma, bem vinda ao seu gerador de números euro milhão")
print("------------------------------------------------------------")
print()

qtd_analises = input("Vamos começar!!!  Quantos jogos você deseja análisar?")

print("OK, vamos lá. Vamos análisar seus " + qtd_analises + " jogos!")

print()

print("--------------------------------------------------------------")

print()

for i in range(int(qtd_analises)):
    
    print("Jogo número " + str(i))
    print("--------------------------------------------------------------")
    recebe_valores = input("Digite seus 5 digitos separados por virgulas! ")
    lista_valores.append(recebe_valores)
    print("--------------------------------------------------------------")
    recebe_estrelas = input("Agora digite suas 2 estrelas!")
    lista_estrelas.append(recebe_estrelas)
print("--------------------------------------------------------------")
print("Sua matriz dos 5 numeros do jogo é:")
df_1 = pd.DataFrame(lista_valores)

print(df_1)
print("--------------------------------------------------------------")

print("--------------------------------------------------------------")
print("Sua matriz das 2 estrelas do jogo é:")
df_2 = pd.DataFrame(lista_estrelas)

print(df_2)
print("--------------------------------------------------------------")


contador = Counter(chain.from_iterable(lista_valores))

# printa o objeto Counter, sendo as chaves o elemento
# contado e os valores quantas vezes eles aparecem na matriz
#print(contador)

for numero, qtd in contador.items():
      print(f"O número: {numero}: se repetiu: {qtd}")

print("------------------------- ESTRELAS -------------------------------------")


contador_estrelas = Counter(chain.from_iterable(lista_estrelas))

# printa o objeto Counter, sendo as chaves o elemento
# contado e os valores quantas vezes eles aparecem na matriz
#print(contador)

for numero_estrelas, qtd_estrelas in contador_estrelas.items():
      print(f"O número: {numero_estrelas}: se repetiu: {qtd_estrelas}")

print("--------------------------------------------------------------")

