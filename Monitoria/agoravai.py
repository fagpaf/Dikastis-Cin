num_feiticeiros = int(input())
feiticeiros = []

for i in range(num_feiticeiros):
    nome = input()
    nivel = int(input())
    feiticeiros.append([nome, nivel])

rodada = 1
while len(feiticeiros) > 1:
    print(f"\n--- Rodada {rodada} ---")
    vencedores = []
    for i in range(0, len(feiticeiros), 2):
        if i + 1 < len(feiticeiros):
            f1 = feiticeiros[i]
            f2 = feiticeiros[i + 1]
            print(f"Confronto: {f1[0]} vs {f2[0]}")
            if f1[1] >= f2[1]:
                print(f"{f1[0]} vence!")
                vencedores.append(f1)
            else:
                print(f"{f2[0]} vence!")
                vencedores.append(f2)
        else:
            print(f"{feiticeiros[i][0]} avança automaticamente!")
            vencedores.append(feiticeiros[i])
    
    feiticeiros = vencedores
    rodada += 1

campeao = feiticeiros[0]
print(f"\nO campeão do torneio é {campeao[0]} com nível de energia amaldiçoada {campeao[1]}!")

if campeao[0] == "Itadori":
    if campeao[1] > 90:
        print(f"\n### Nas sombras da alma de Itadori, Sukuna desperta e toma o controle! ###")
        print(f"Uma aura de destruição toma conta, não há escapatória.")
        print(f"Com um riso diabólico, ele manifesta sua Expansão de Domínio: Fukuma Mizushi!")
    else:
        print(f"\nItadori vence com honra e bravura!")