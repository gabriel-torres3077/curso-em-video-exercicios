"""
Faça um programa
que leia uma frase pelo
teclado e mostre:
-Quantas vezes aparece a letra'A'
-Em que posição ela aparece a primeira vez
-Em que posiçlão ela aparece a ultimavez
"""
phrase = str(input('Ensira uma frase qualquer: ')).strip()
print('-Quantas vezes aparece a letra A: {}\n'
      '-Em que posição ela aparece a primeira vez: {}\n'
      '-Em que posiçlão ela aparece a ultimavez: {}\n'.format(phrase.count('a'), phrase.find('a')+1, phrase.rfind('a')+1))