nome_feiticeiro = input().strip()
vida_feiticeiro = int(input())
ataque_feiticeiro = int(input())
defesa_feiticeiro = int(input())
reversao_feitico = input().strip() == 'True'
expansao_dominio = input().strip() == 'True'
vida_mahoraga = int(input())
ataque_mahoraga = int(input())
defesa_mahoraga = int(input())
golpes_input = input().strip()
golpes = golpes_input.split(', ') if golpes_input != '' else []
if not reversao_feitico:
    print('Exorcizar o Mahoraga sem conseguir me curar vai ser bem difícil, mas eu não tenho escolha!')
else:
    print('Mesmo com a regeneração, ainda não vai ser fácil! Vamos nessa!')
contagem_adaptação = [[golpe, 0] for golpe in golpes]
ultimo_movimento = None
limite_adaptacao = False
derrota_por_adaptacao = False
while True:
    # Turno do feiticeiro
    movimento_feiticeiro = input().strip()
    movimento_valido = False
    if movimento_feiticeiro in golpes:
        movimento_valido = True
    elif movimento_feiticeiro == 'black flash':
        movimento_valido = True
    elif movimento_feiticeiro == 'expansão de domínio':
        movimento_valido = True
    elif movimento_feiticeiro == 'reversão de feitiço':
        movimento_valido = True
    else:
        print('Eu não sei que ideia é essa de tentar usar um golpe que eu não domino!')
    if movimento_valido:
        if movimento_feiticeiro == 'expansão de domínio':
            if expansao_dominio:
                if nome_feiticeiro == 'Satoru Gojo':
                    print(f'Como assim o Mahoraga já se adaptou ao infinito de {nome_feiticeiro}!?')
                else:
                    print('Nem mesmo a sua adaptação pode derrotar isto!')
                    vida_mahoraga = 0
            else:
                print('Droga. Eu não aprendi a expandir meu domínio ainda!')
        elif movimento_feiticeiro == 'reversão de feitiço':
            if reversao_feitico:
                vida_feiticeiro += 25
                print('Eu posso continuar lutando mais um pouco...')
        elif movimento_feiticeiro == 'black flash':
            dano = (ataque_feiticeiro + 25) * 2
            vida_mahoraga -= dano
            print('As faíscas negras ignoram qualquer tipo de defesa! Toma essa Mahoraga!')
            ultimo_movimento = 'black flash'
        else:
            if movimento_feiticeiro in golpes:
                indice = None
                for i in range(len(contagem_adaptação)):
                    if contagem_adaptação[i][0] == movimento_feiticeiro:
                        indice = i
                        break
                if indice is not None:
                    contagem = contagem_adaptação[indice][1]
                    if contagem >= 3:
                        print('Esse ataque é inútil! Melhor tentar outra coisa.')
                    else:
                        dano = (ataque_feiticeiro - defesa_mahoraga) + 25
                        if contagem == 1:
                            dano = dano // 2
                        elif contagem == 2:
                            dano = dano // 4
                        dano = int(dano)
                        vida_mahoraga -= dano
                        contagem_adaptação[indice][1] += 1
                        nova_contagem = contagem_adaptação[indice][1]
                        if nova_contagem == 1:
                            print(f'A roda do Mahoraga girou uma vez! {movimento_feiticeiro} só vai funcionar mais duas vezes')
                        elif nova_contagem == 2:
                            print(f'A roda do Mahoraga girou pela segunda vez! {movimento_feiticeiro} só vai funcionar mais uma vez')
                        elif nova_contagem >= 3:
                            print(f'A roda do Mahoraga girou pela terceira vez! {movimento_feiticeiro} não vai funcionar mais')
                ultimo_movimento = movimento_feiticeiro
        # Verifica se Mahoraga foi derrotado após o ataque
        if vida_mahoraga <= 0:
            vitoria = True
        else:
            vitoria = False
        # Verifica adaptação completa
        todos_adaptados = True
        for golpe, contagem in contagem_adaptação:
            if contagem < 3:
                todos_adaptados = False
                break
        if todos_adaptados:
            print('Droga... Eu não tenho mais nada pra usar contra o Mahoraga... Essa luta acabou.')
            limite_adaptacao = True
            derrota_por_adaptacao = True
        # Sai do loop se Mahoraga foi derrotado ou adaptado
        if vida_mahoraga <= 0 or derrota_por_adaptacao:
            break
        # Turno do Mahoraga
        movimento_mahoraga = input().strip()
        if movimento_mahoraga not in ['ataque', 'regeneração', 'adaptação']:
            pass
        else:
            if movimento_mahoraga == 'regeneração':
                vida_mahoraga += 25
                print('Ele está se regenerando.')
            elif movimento_mahoraga == 'ataque':
                dano = (ataque_mahoraga - defesa_feiticeiro) + 25
                dano = int(dano)
                vida_feiticeiro -= dano
            elif movimento_mahoraga == 'adaptação':
                if ultimo_movimento == 'black flash':
                    print('Nem você vai conseguir se adaptar a isso, mahoraga!')
                elif ultimo_movimento in ['expansão de domínio', 'reversão de feitiço']:
                    pass
                else:
                    if ultimo_movimento in golpes:
                        indice = None
                        for i in range(len(contagem_adaptação)):
                            if contagem_adaptação[i][0] == ultimo_movimento:
                                indice = i
                                break
                        if indice is not None:
                            contagem_atual = contagem_adaptação[indice][1]
                            if contagem_atual < 3:
                                contagem_adaptação[indice][1] += 1
                                nova_contagem = contagem_adaptação[indice][1]
                                if nova_contagem == 2:
                                    print(f'A roda do Mahoraga girou pela segunda vez! {ultimo_movimento} só vai funcionar mais uma vez')
                                elif nova_contagem == 3:
                                    print(f'A roda do Mahoraga girou pela terceira vez! {ultimo_movimento} não vai funcionar mais')
                                todos_adaptados = True
                                for _, cnt in contagem_adaptação:
                                    if cnt < 3:
                                        todos_adaptados = False
                                        break
                                if todos_adaptados:
                                    print('Droga... Eu não tenho mais nada pra usar contra o Mahoraga... Essa luta acabou.')
                                    limite_adaptacao = True
                                    derrota_por_adaptacao = True
        # Verifica se feiticeiro foi derrotado ou adaptado
        if vida_feiticeiro <= 0 or derrota_por_adaptacao:
            break
    else:
        # Se movimento inválido, pula turno do Mahoraga
        movimento_mahoraga = input().strip()
        if movimento_mahoraga not in ['ataque', 'regeneração', 'adaptação']:
            pass
        else:
            if movimento_mahoraga == 'regeneração':
                vida_mahoraga += 25
                print('Ele está se regenerando.')
            elif movimento_mahoraga == 'ataque':
                dano = (ataque_mahoraga - defesa_feiticeiro) + 25
                dano = int(dano)
                vida_feiticeiro -= dano
            elif movimento_mahoraga == 'adaptação':
                pass
        # Verifica se feiticeiro foi derrotado
        if vida_feiticeiro <= 0:
            break
# Resultado final
if vida_mahoraga <= 0:
    print(f'{nome_feiticeiro} conseguiu!')
    if nome_feiticeiro == 'Megumi Fushiguro':
        print('Depois de muito tempo, finalmente o Mahoraga foi exorcizado. Fushiguro é o primeiro usuário das dez sombras a conseguir esse feito!')
    elif nome_feiticeiro == 'Sukuna':
        print('Você me mostrou o caminho, Megumi Fushiguro, e por isso eu sou grato!')
    elif nome_feiticeiro == 'Satoru Gojo':
        print('Nem você sua adaptação é páreo para o infinito, queridinho.')
    else:
        print('Depois de muito tempo, finalmente o Mahoraga foi exorcizado, mas Fushiguro não participou da luta, logo o ritual foi anulado.')
elif vida_feiticeiro <= 0 or derrota_por_adaptacao:
    if nome_feiticeiro == 'Satoru Gojo':
        print('Magnífico, Satoru Gojo. Lembrarei de você enquanto eu durar nesta vida.')
    else:
        print(f'Parece que nem mesmo {nome_feiticeiro} foi pareo contra o Mahoraga...')