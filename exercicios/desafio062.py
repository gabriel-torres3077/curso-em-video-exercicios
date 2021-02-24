"""
Melhores o desafio 062,
perguntando para o usuário
se ele quer mostrar mais alguns
termos. O programa encerra quando
ele disser que quer mostrar 0 termos
"""
a1 = int(input('Primeiro termo: '))
diff = int(input('razão: '))
count = 1
numterms = 10
ended = False
terms = []
while numterms != 0:
    while count <= numterms:
        terms.append(a1 + ((count - 1) * diff))
        count+=1
    print(terms)
    numterms += int(input('Você deseja acicionar mais quantos termos? '))


