"""
Desenvolva um programa
que leia o primeiro termo
e a razão de um PA. No final
mostre os 10 primeiros termos
dessa progressão
"""
a1 = int(input('Ensira o primeiro termo: '))
diff = int(input('Ensira a razão: '))
terms = []
for x in range(1, 11):
    terms.append(a1 + ((x - 1) * diff))
print(terms)
