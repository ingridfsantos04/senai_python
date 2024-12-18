#Dadoos do aluno
print("Sistema de Notas do aluno")
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))

#Calcula a média da nota
media = (nota1 + nota2) / 2

#Verifica a situação do aluno
if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

#Exibe o resultado
print("\nResultado do Aluno")
print(f"Aluno: {nome}")
print(f"Média: {media:.2f}") 
print(f"Situação: {situacao}")


