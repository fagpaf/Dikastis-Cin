# Q7

animes_favoritos = ['Fullmetal Alchemist: Brotherhood', 'Attack On Titan', 'Death Note', 'Naruto', 'One Piece', 'Demon Slayer', 'Dragon Ball Z', 'Jujutsu Kaisen', 'Pokemon', 'Bleach']
pontos = [0,0,0,0,0,0,0,0,0,0]
quantidade_amigos = int(input())
print(f'{quantidade_amigos} amigos participaram da votação!')

for amigos in range(0, quantidade_amigos):
    nome = input()
    print(f'{nome} é a {amigos + 1}ª pessoa à votar!')
    primeiro = input().title()
    if primeiro in animes_favoritos:
        print(f'{nome} colocou {primeiro} em 1º lugar do seu ranking!')
        indice = animes_favoritos.index(primeiro)
        pontos[indice] += 3
    else:
        while primeiro not in animes_favoritos:
            print(f'O anime {primeiro} não está presente na votação!')
            primeiro = input().title()

        print(f'{nome} colocou {primeiro} em 1º lugar do seu ranking!')
        indice = animes_favoritos.index(primeiro)
        pontos[indice] += 3

    segundo = input().title()
    if segundo in animes_favoritos:
        if segundo == primeiro:
            while segundo == primeiro:
                print(f'{nome}, você já votou neste anime! Escolha um outro anime para ocupar a sua 2º posição!')
                segundo = input().title()
            else:
                print(f'{nome} colocou {segundo} em 2º lugar do seu ranking!')
                indice = animes_favoritos.index(segundo)
                pontos[indice] += 2
        else:
            print(f'{nome} colocou {segundo} em 2º lugar do seu ranking!')
            indice = animes_favoritos.index(segundo)
            pontos[indice] += 2
    else:
        while segundo not in animes_favoritos:
            print(f'O anime {segundo} não está presente na votação!')
            segundo = input().title()
        else:
            if segundo == primeiro:
                while segundo == primeiro:
                    print(f'{nome}, você já votou neste anime! Escolha um outro anime para ocupar a sua 2º posição!')
                    segundo = input().title()
                else:
                    print(f'{nome} colocou {segundo} em 2º lugar do seu ranking!')
                    indice = animes_favoritos.index(segundo)
                    pontos[indice] += 2
            else:
                print(f'{nome} colocou {segundo} em 2º lugar do seu ranking!')
                indice = animes_favoritos.index(segundo)
                pontos[indice] += 2

    terceiro = input().title()
    if terceiro in animes_favoritos:
        if terceiro == primeiro:
            while terceiro == primeiro:
                print(f'{nome}, você já votou neste anime! Escolha um outro anime para ocupar a sua 3º posição!')
                terceiro = input().title()
            else:
                print(f'{nome} colocou {terceiro} em 3º lugar do seu ranking!')
                indice = animes_favoritos.index(terceiro)
                pontos[indice] += 1
        elif terceiro == segundo:
            while terceiro == segundo:
                print(f'{nome}, você já votou neste anime! Escolha um outro anime para ocupar a sua 3º posição!')
                terceiro = input().title()
            else:
                print(f'{nome} colocou {terceiro} em 3º lugar do seu ranking!')
                indice = animes_favoritos.index(terceiro)
                pontos[indice] += 1
        else:
            print(f'{nome} colocou {terceiro} em 3º lugar do seu ranking!')
            indice = animes_favoritos.index(terceiro)
            pontos[indice] += 1
    else:
        while terceiro not in animes_favoritos:
            print(f'O anime {terceiro} não está presente na votação!')
            terceiro = input().title()
        else:
            if terceiro == primeiro:
                while terceiro == primeiro:
                    print(f'{nome}, você já votou neste anime! Escolha um outro anime para ocupar a sua 3º posição!')
                    terceiro = input().title()
                else:
                    if terceiro == segundo:
                        while terceiro == segundo:
                            print(f'{nome}, você já votou neste anime! Escolha um outro anime para ocupar a sua 3º posição!')
                            terceiro = input().title()
                        else:
                            print(f'{nome} colocou {terceiro} em 3º lugar do seu ranking!')
                            indice = animes_favoritos.index(terceiro)
                            pontos[indice] += 1
            elif terceiro == segundo:
                while terceiro == primeiro:
                    print(f'{nome}, você já votou neste anime! Escolha um outro anime para ocupar a sua 3º posição!')
                    terceiro = input().title()
                else:
                    if terceiro == segundo:
                        while terceiro == segundo:
                            print(f'{nome}, você já votou neste anime! Escolha um outro anime para ocupar a sua 3º posição!')
                            terceiro = input().title()
                        else:
                            print(f'{nome} colocou {terceiro} em 3º lugar do seu ranking!')
                            indice = animes_favoritos.index(terceiro)
                            pontos[indice] += 1
            else:
                print(f'{nome} colocou {terceiro} em 3º lugar do seu ranking!')
                indice = animes_favoritos.index(terceiro)
                pontos[indice] += 1

indice_final = pontos.index(max(pontos))
print(f'Com {max(pontos)} pontos, {animes_favoritos[indice_final]} foi votado como o melhor anime!')
if animes_favoritos[indice_final] == 'Pokemon':
    print('César - Pokémon é o melhor anime da história!!!')
print('Eita mandaram dúvida no discord, vou lá responder!')
