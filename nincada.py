import random

print("Digite abaixo as possíveis informações para a sua wordlist")
print("Quando terminar, deixe um campo vazio e pressione Enter")

list_dados = []

quanti = int(input("Digite quantas combinações você quer: "))

while True:
    dado = input("XD: ")
    if dado == "":
        break
    list_dados.append(dado)

if not list_dados:
    print("Não há dados fornecidos.")
else:
    combinacoes = set()

    while len(combinacoes) < quanti:
        dd1, dd2 = random.sample(list_dados, 2)
        combinacao = dd1 + dd2
        combinacoes.add(combinacao)

    for combinacao in combinacoes:
        print(combinacao)

