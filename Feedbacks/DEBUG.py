entrada = input()
pessoas = entrada.split("-")
teleportes = []
for x in range(len(pessoas)):
    teleportes.append(0)

while entrada != "Acabou!":
    entrada = input()

    if entrada != "Acabou!":
        pessoa1,pessoa2 = entrada.split("-")
        
        if pessoa1 not in pessoas or pessoa2 not in pessoas:
            print("Essa dupla não esta na lista!")
        else:
            posicao1 = pessoas.index(pessoa1)
            posicao2 = pessoas.index(pessoa2)

            teleportes[posicao1] += 1
            teleportes[posicao2] += 1

            pessoas[posicao1],pessoas[posicao2] = pessoas[posicao2],pessoas[posicao1]
            teleportes[posicao1],teleportes[posicao2] = teleportes[posicao2],teleportes [posicao1]

print("Fila do almoço:")

for x,y in enumerate(pessoas):
    print(f"{y}: {teleportes[x]} ",end="")
    if teleportes[x] == 1:
        print("teleporte!")
    else:
        print("teleportes!")