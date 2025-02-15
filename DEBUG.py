lista_viloes = []
viloes = ''

while viloes != 'Já temos nossa lista de vilões':
    viloes = input()

    if viloes == 'Como a lista está ficando?':
        print(', '.join(lista_viloes))
    elif viloes == 'Já temos nossa lista de vilões':
        break
    elif viloes == 'Vilão mais perigoso do que pensávamos':
        indice_atual = int(input())
        indice_novo = int(input())

        nome_vilao2 = lista_viloes[indice_atual]
        lista_viloes.pop(indice_atual)
        lista_viloes.insert(indice_novo, nome_vilao2)
    elif viloes == 'Que estranho, esses dois vilões… troque-os de lugar':
        nome_vilao3 = input()
        nome_vilao4 = input()

        ind = lista_viloes.index(nome_vilao3)
        ind2 = lista_viloes.index(nome_vilao4)
        lista_viloes[ind] = nome_vilao4
        lista_viloes[ind2] = nome_vilao3

    elif viloes == 'Essa posição não está de acordo, ele nem odeia carecas':
        nome_vilao5 = input()

        lista_viloes.remove(nome_vilao5)
        lista_viloes.append(nome_vilao5)
    else:
        nome_vilao = input()

        if viloes == 'Novo vilão - Muito Perigoso':
            lista_viloes.insert(0, nome_vilao)
        elif viloes == 'Novo vilão - Meio perigoso':
            lista_viloes.append(nome_vilao)
        elif viloes == 'O que ele está fazendo aqui?':
            lista_viloes.remove(nome_vilao)
print('O resultado final ficou assim:')
saida_final = ', '.join(lista_viloes)
print(saida_final)
