"""
Crie um programa que
leia uma frase qualquer e
diga se ela é um palindromo,
desconsiderando os espaços
"""
phrase = str(input('Ensira a frase a ser analisada'))
phrase.split()
char = 0
newPhrase = []
reversePhrase = []
for char in range(0, len(phrase)):
    newPhrase.append(phrase[char])
    reversePhrase.append(phrase[char])
reversePhrase.reverse()
if (newPhrase == reversePhrase):
    palindrome = 'É'
else:
    palindrome = 'NÃO É'

print('Frase original: {} \n'
      'frase separada: {} \n'
      'frase inversa: {} \n'
      'A frase {} um palindromo?'.format(phrase, newPhrase, reversePhrase, palindrome))
