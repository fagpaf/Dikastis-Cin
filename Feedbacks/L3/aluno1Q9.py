pokemons_ash = []
pokemons_gary = []
batalhas = []
batalha = 1
vitorias_ash = 0
vitorias_gary = 0
qtd_ash, qtd_gary = input().split()
qtd_ash1 = int(qtd_ash)
qtd_gary1 = int(qtd_gary)
if qtd_ash1 == 0 and qtd_gary1 == 0:
    print('QUE COMECEM AS BATALHAS')
    print('=============== ===============')
    print('Nenhuma batalha foi concluída.')
elif qtd_gary1 > 0 and qtd_ash1 == 0:
    print('QUE COMECEM AS BATALHAS')
    print('=============== ===============')
    print('Ash deixou seus pokemons descansando!')
    print('Gary é o grande vencedor!')
elif qtd_ash1 > 0 and qtd_gary1 == 0:
    print('QUE COMECEM AS BATALHAS')
    print('=============== ===============')
    print('Gary deixou seus pokemons descansando!')
    print('Ash é o grande vencedor!')
else:
    if qtd_ash1 == 1 and qtd_gary1 == 1:
        pokemon1 = input().split(',')
        pokemon_ash = [pokemon1[0], pokemon1[1], int(pokemon1[2]), int(pokemon1[3])]
        pokemons_ash.append(pokemon_ash)
        pokemon2 = input().split(',')
        pokemon_gary = [pokemon2[0], pokemon2[1], int(pokemon2[2]), int(pokemon2[3])]
        pokemons_gary.append(pokemon_gary)
    else:
        for ash in range(0, qtd_ash1):
            pokemon = input().split(',')
            pokemon_ash = [pokemon[0], pokemon[1], int(pokemon[2]), int(pokemon[3])]
            pokemons_ash.append(pokemon_ash)
        for gary in range(0, qtd_gary1):
            pokemon1 = input().split(',')
            pokemon_gary = [pokemon1[0], pokemon1[1], int(pokemon1[2]), int(pokemon1[3])]
            pokemons_gary.append(pokemon_gary)
    decisao_ash = ''
    print('QUE COMECEM AS BATALHAS')
    while decisao_ash != 'FIM DAS BATALHAS':
        decisao_ash = input()
        if decisao_ash == 'FIM DAS BATALHAS':
            continue
        numeros_decisao = input().split()
        par_impar = [int(numeros_decisao[0]), int(numeros_decisao[1])]
        if decisao_ash == 'par':
            if sum(par_impar) % 2 == 0:
                ash_comeca = True
            else:
                ash_comeca = False
        else:
            if sum(par_impar) % 2 == 0:
                ash_comeca = False
            else:
                ash_comeca = True
        if ash_comeca:
            escolhido_ash = input().split()
            pokemon_escolhido_ash = escolhido_ash[0]
            escolha_final_ash = ''
            for nome in pokemons_ash:
                if nome[0] == pokemon_escolhido_ash:
                    escolha_final_ash = nome
                    break
            ataque_ash = escolha_final_ash[3] * 2
            escolhido_gary = input().split()
            pokemon_escolhido_gary = escolhido_gary[0]
            escolha_final_gary = ''
            for nome1 in pokemons_gary:
                if nome1[0] == pokemon_escolhido_gary:
                    escolha_final_gary = nome1
                    break
            ataque_gary = escolha_final_gary[3] * 2

            while escolha_final_ash[2] > 0 and escolha_final_gary[2] > 0:
                escolha_final_gary[2] -= ataque_ash
                if escolha_final_gary[2] <= 0:
                    continue
                escolha_final_ash[2] -= ataque_gary
            else:
                if escolha_final_ash[2] > 0:
                    print(f'{escolha_final_gary[0]} desmaiou e {escolha_final_ash[0]} venceu esta luta')
                    vitorias_ash += 1
                    batalhas.append([batalha, escolha_final_ash[0].upper(), escolha_final_gary[0].lower()])
                else:
                    print(f'{escolha_final_ash[0]} desmaiou e {escolha_final_gary[0]} venceu esta luta')
                    vitorias_gary += 1
                    batalhas.append([batalha, escolha_final_ash[0].lower(), escolha_final_gary[0].upper()])
            batalha += 1
        else:
            escolhido_ash = input().split()
            pokemon_escolhido_ash = escolhido_ash[0]
            escolha_final_ash = ''
            for nome in pokemons_ash:
                if nome[0] == pokemon_escolhido_ash:
                    escolha_final_ash = nome
                    break
            ataque_ash = escolha_final_ash[3] * 2
            escolhido_gary = input().split()
            pokemon_escolhido_gary = escolhido_gary[0]
            escolha_final_gary = ''
            for nome1 in pokemons_gary:
                if nome1[0] == pokemon_escolhido_gary:
                    escolha_final_gary = nome1
                    break
            ataque_gary = escolha_final_gary[3] * 2
            while escolha_final_ash[2] > 0 and escolha_final_gary[2] > 0:
                escolha_final_ash[2] -= ataque_gary
                if escolha_final_ash[2] <= 0:
                    continue
                escolha_final_gary[2] -= ataque_ash
            else:
                if escolha_final_gary[2] <= 0:
                    print(f'{escolha_final_gary[0]} desmaiou e {escolha_final_ash[0]} venceu esta luta')
                    vitorias_ash += 1
                    batalhas.append([batalha, escolha_final_ash[0].upper(), escolha_final_gary[0].lower()])
                elif escolha_final_ash[2] <= 0:
                    print(f'{escolha_final_ash[0]} desmaiou e {escolha_final_gary[0]} venceu esta luta')
                    vitorias_gary += 1
                    batalhas.append([batalha, escolha_final_ash[0].lower(), escolha_final_gary[0].upper()])
                batalha += 1
    print('=============== ===============')
    ordem = 0
    for lutas in batalhas:
        print(f'{batalhas[ordem][0]}° Batalha: {batalhas[ordem][1]} vs {batalhas[ordem][2]}')
        ordem += 1
    if vitorias_ash > vitorias_gary:
        print('Ash é o grande vencedor!')
    elif vitorias_gary > vitorias_ash:
        print('Gary é o grande vencedor!')
    else:
        print('Depois de todas as batalhas, ainda terminou em empate!')