#Estruturas de Dados
lista = [1,2,3,4,5,6,7,8,9,10]
#tupla = (1,2,3,4)
#dicionario = {"nome": "miguel", "idade":29}
#print(lista)
#lista.append(11)
#lista.insert(3,120)
#print(lista)
#dicionario['nome'] = "Ana"
numeros = []
sum = 0
while True:
  new = int(input("Insira um numero: "))
  numeros.append(new)
  sum = sum + new
  a = input("Deseja continuar S/N: ").upper()
  if a == "N":
    break

print(numeros)
print(sum)
13