"""
Escreva um
programa que leia um
número 'n' inteiro
qualquer e mostre na
tela os 'n' primeiros
elementos de uma Sequência
de Fibonacci
"""
numTerms = int(input('Quantos termos você deseja mostrar? '))
term1 = 0
term2 = 1
print('{}, {}'.format(term1, term2), end='')
count = 3
nextTerm = 0
actualTerm = 0
while count <= numTerms:
    nextTerm = term1 + term2
    print(', {}'.format(nextTerm), end='')
    term1 = term2
    term2 = nextTerm
    count += 1
