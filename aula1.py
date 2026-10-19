#Primeira aula!
#Recap! Faça um pequeno programa de notas de aluno (Que legal :D)
#Vou usar esse código para comentar e anotar coisas
print("Hello guys :)")

#Custom functions & Class Reminders
def input_number(text):
  while True:
    number = input(text)
    try:
      return float(number)
      break
    except:
      print('Erro: Deve digitar apenas números!')

#Polimorfismo

class Contador:                           #Crie a Classe
  def __init__(self, number):             #Defina seus parâmetros (Não esquece do self viuuuuu)
    self.number = number

  def add(self, value):                 #Defina suas ações
    self.number += value

  def sub(self, value):                 #Defina suas ações
    self.number -= value

  def show(self):                 #Defina suas ações
    print(self.number)

#


name = input("Digite seu nome : ")
age = input("Digite sua idade : ")
grades = []
for i in range(3):
    grades.append(float(input_number(f"Digite a nota {i+1} : ")))

print()
print()
print("-- Resultados : --")
final_score = sum(grades)/3
print("Nome : "+name)
print("Idade : "+age)
print("Média : "+str(final_score))
if final_score >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")

print("------------------")