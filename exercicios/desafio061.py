"""
Refaça o Desafio 051,
lendo o primeiro
termo e a razão de uma
PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while
"""
a1 = int(input('Primeiro termo: '))
diff = int(input('razão: '))
count = 1
terms = []
while len(terms) != 11:
    terms.append(a1 + ((count - 1) * diff))
    count+=1
print(terms)