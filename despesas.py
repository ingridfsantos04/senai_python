nome = input('Qual o seu nome?: ')
salario = int(input('Qual o valor do seu Salário?: '))
despesa1 = int(input('Informe a sua despesa e o Valor: '))
despesas2 = int(input('Informe a sua segunda despesa e o Valor: '))
total = salario - despesa1 - despesas2
print('Sobrará o valor de: {}'.format(total))