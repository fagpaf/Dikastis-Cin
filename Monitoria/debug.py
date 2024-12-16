# Entrada de dados
print("Digite o número de feiticeiros participantes: ")
num_feiticeiros = int(input())

feiticeiros = []
for i in range(num_feiticeiros):
    nome = input(f"Digite o nome do feiticeiro {i + 1}: ")
    nivel = int(input(f"Digite o nível de poder de {nome}: "))
    feiticeiros.append({'nome': nome, 'nivel': nivel})

# Torneio
rodada = 1
while len(feiticeiros) > 1:
    print(f"\n--- Rodada {rodada} ---")
    vencedores = []
    
    # Confrontos
    for i in range(0, len(feiticeiros), 2):
        if i + 1 < len(feiticeiros):
            f1 = feiticeiros[i]
            f2 = feiticeiros[i + 1]
            print(f"Confronto: {f1['nome']} vs {f2['nome']}")
            if f1['nivel'] >= f2['nivel']:
                print(f"{f1['nome']} vence!")
                vencedores.append(f1)
            else:
                print(f"{f2['nome']} vence!")
                vencedores.append(f2)
        else:
            print(f"{feiticeiros[i]['nome']} avança automaticamente!")
            vencedores.append(feiticeiros[i])
    
    feiticeiros = vencedores
    rodada += 1

# Vencedor
campeao = feiticeiros[0]
print(f"\nO campeão do torneio é {campeao['nome']} com nível de poder {campeao['nivel']}!")