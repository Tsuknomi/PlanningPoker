#criando o array#
valores = []

print("Digite a quantidade de números que deseja ter:")
tamanho = int(input())

print("Digite os números desejados:")
for i in range(tamanho):
  valores.append(int(input()))



print("Deseja remover um número?(s/n):")
escolha = input()

if escolha == 's' :
  print("Digite o número que deseja remover:")
  x = int(input())
  remover = valores.index(x)
  valores.pop(remover)
  valores.sort()

else:
  valores.sort()

print("Estes são os números:")
for i in range(len(valores)):
  print(valores[i])
