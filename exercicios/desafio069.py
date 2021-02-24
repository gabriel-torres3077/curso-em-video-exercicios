"""
Crie um programa
que leia a idade e o
sexo de várias
pessoas. A cada
pessoa cadastrada, o
programa deverá
perguntar se o usuário
quer ou não continuar.
No final, mostre:
-Quantas pessoas tem mais de 18 anos
-Quantos homens foram cadastrados.
-quantas mulheres tem menos de 20 anos
"""
males = youngerFemales = olderPeoples = age = count = 0
sex = keepGoing = ''
while True:
    count += 1
    print('Cadastro {}.' .format(count))
    sex = str(input('Ensira o sexo [M/F]: '))
    age = int(input('Ensira a idade: '))
    if age > 18:
        olderPeoples += 1
    if sex in 'Mm':
        males += 1
    if age < 20 and sex in 'Ff':
        youngerFemales += 1
    keepGoing = str(input('Você deseja continuar cadastrando os usuários? [S/N]'))
    if keepGoing in 'Nn':
        break
print('-Quantas pessoas tem mais de 18 anos: {} \n'
      '-Quantos homens foram cadastrados: {} \n'
      '-quantas mulheres tem menos de 20 anos: {}' .format(olderPeoples, males, youngerFemales))