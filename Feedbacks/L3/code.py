num_feiticeiros = int(input())
feiticeiros = []
niveis = []
avanca = 0
for x in range(num_feiticeiros):
    nome = input()
    nivel = int(input())
    feiticeiros.append(nome)
    niveis.append(nivel)
if len(feiticeiros)%2 ==0:
    rodadas = len(feiticeiros)//2
else:
    rodadas = (len(feiticeiros) + 1)//2

for x in range(rodadas):
    print(f"\n--- Rodada {x+1} ---")
    confrontos = len(feiticeiros)//2
    if len(feiticeiros)%2 ==1 and len(feiticeiros)!= 1:
      avanca = 1
    else:
      avanca = 0
    for x in range(confrontos):
        print(f"Confronto: {feiticeiros[x]} vs {feiticeiros[x+1]}")
        if niveis[x] >= niveis[x+1]:
            print(f"{feiticeiros[x]} vence!")
            feiticeiros.pop(x+1)
            niveis.pop(x+1)
        else:
            print(f"{feiticeiros[x+1]} vence!")
            feiticeiros.pop(x)
            niveis.pop(x)
    if avanca:
      print(f"{feiticeiros[-1]} avança automaticamente!")
print(f"\nO campeão do torneio é {feiticeiros[0]} com nível de energia amaldiçoada {niveis[0]}!")
if feiticeiros[0] == "Itadori":
    if niveis[0] > 90:    
        print("\n### Nas sombras da alma de Itadori, Sukuna desperta e toma o controle! ###")
        print("Uma aura de destruição toma conta, não há escapatória.")
        print("Com um riso diabólico, ele manifesta sua Expansão de Domínio: Fukuma Mizushi!")
    else:
        print("\nItadori vence com honra e bravura!")
    