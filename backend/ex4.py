nome = input('Qual o nome do aluno: ')
nota1 = float(input('Qual a primeira nota: '))
nota2 = float(input('Qual a primeira nota: '))
nota3 = float(input('Qual a primeira nota: '))

media = (nota1 + nota2 + nota3) / 3
aval = ''
if media == 10:
    aval = 'Excelente'

elif 7 <= media <=10:
    aval = 'muito bom'

elif (media >= 5) and (media <= 7):
    aval = 'Regular'
else:
    aval = 'ruim'





print('\n'*3)
print('---------------------------------------')
print(f'Nome dp aluno: {nome}\n')
print(f'Primeira nota:{nota1}\n')
print(f'Segunda nota:{nota2}\n')
print(f'Terceira nota:{nota3}\n')
print(f'Média:{media}\n')
print(f'avaliação:{aval}\n')
print('---------------------------------------')