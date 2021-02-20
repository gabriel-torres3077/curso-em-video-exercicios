"""
Faça um programa que
leia o ano de nascimento
de um jovem e informe de
acordo com sua idade:

-Se ele ainda vai se alistar ao serviço militar
-Se é a hora de se alistar
-Se já passou do tempo do alistamento

o programa tambem deve
mostrar o tempo que falta ou
passou do prazo
"""
year = int(input('Ensira o seu ano de nascimento: '))
if ((2021-year) > 18):
    print('Ja passou do prazo de alistamento militar, você está {} anos atrasado'.format(2021-year))
elif ((2021-year) < 18):
    print('Ainda faltam {} anos para você se alistar ao serviço miliar' .format(2021-year))
else:
    print('Ja está na hora de se alistar ao serviço militar')