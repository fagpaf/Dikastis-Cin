num_feiticeiros = int(input())
feiticeiros_principal = []
rodada = 0
for nomes in range(0, num_feiticeiros):
    nome_feiticeiro = input()
    nivel_energia = int(input())
    feiticeiros_principal.append([nome_feiticeiro, nivel_energia])
    
while len(feiticeiros_principal) > 1:
    print(f'\n--- Rodada {rodada + 1} ---')
    perdedores = []
    for indice in range(0, len(feiticeiros_principal), 2):
        if indice + 1 < len(feiticeiros_principal):
            feiticeiro1 = feiticeiros_principal[indice]
            feiticeiro2 = feiticeiros_principal[indice + 1]

            if feiticeiro1[1] >= feiticeiro2[1]:
                vencedor = feiticeiro1
                perdedores.append(feiticeiro2)
            else:
                vencedor = feiticeiro2
                perdedores.append(feiticeiro1)
            print(f'Confronto: {feiticeiro1[0]} vs {feiticeiro2[0]}')
            print(f'{vencedor[0]} vence!')
        else:
            feiticeiro_sobrando = feiticeiros_principal[indice]
            print(f'{feiticeiro_sobrando[0]} avança automaticamente!')
    for perdedor in perdedores:
        feiticeiros_principal.remove(perdedor)
    rodada += 1
print(f'\nO campeão do torneio é {feiticeiros_principal[0][0]} com nível de energia amaldiçoada {feiticeiros_principal[0][1]}!')
if feiticeiros_principal [0][0] == 'Itadori' and feiticeiros_principal [0][1] > 90:
    print('\n### Nas sombras da alma de Itadori, Sukuna desperta e toma o controle! ###')
    print('Uma aura de destruição toma conta, não há escapatória.')
    print('Com um riso diabólico, ele manifesta sua Expansão de Domínio: Fukuma Mizushi!')
elif feiticeiros_principal [0][0] == 'Itadori' and feiticeiros_principal [0][1] <= 90:
    print('\nItadori vence com honra e bravura!')
