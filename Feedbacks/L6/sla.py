# Leitura da entrada e criação da matriz
tamanho = int(input())
matriz = [input().split() for x in range(tamanho)]

alvos = [
    ("PENGUINBAR", "Penguin Bar"),
    ("PRAIAGELADA", "Praia Gelada"),
    ("PENGUICUPSTADIUM", "PenguiCup Stadium"),
    ("DELEGACIAPOLAR", "Delegacia Polar"),
    ("SUBZEROWAY", "SubzeroWay"),
    ("FRIODEJANEIRO", "Frio de Janeiro")
]


# Função para buscar a palavra
def retroceder(linha, coluna, palavra, indice, visitados, matriz, tamanho):
    if indice == len(palavra):
        return True

    if linha < 0 or linha >= tamanho or coluna < 0 or coluna >= tamanho:
        return False

    if visitados[linha][coluna] or matriz[linha][coluna] != palavra[indice]:
        return False

    visitados[linha][coluna] = True

    direcoes = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 1),
                (1, -1), (1, 0), (1, 1)]

    for delta_linha, delta_coluna in direcoes:
        nova_linha = linha + delta_linha
        nova_coluna = coluna + delta_coluna

        if retroceder(nova_linha, nova_coluna, palavra, indice + 1, visitados, matriz, tamanho):
            return True

    visitados[linha][coluna] = False
    return False

# verificação na matriz
encontrado = None
for palavra, nome in alvos:
    for linha in range(tamanho):
        for coluna in range(tamanho):

            if matriz[linha][coluna] == palavra[0]:
                visitados = [[False for y in range(tamanho)] for x in range(tamanho)]

                if retroceder(linha, coluna, palavra, 0, visitados, matriz, tamanho):
                    encontrado = nome
                    break
        if encontrado:
            break
    if encontrado:
        break

# prints finais
if encontrado == "Delegacia Polar":
    print("Se formos até a Delegacia Polar, estaremos mexendo com um fora da lei. Vamos até lá investigar!")
elif encontrado == "Frio de Janeiro":
    print(
        "ARRGH! Todos sabem que o melhor carnaval é no bloco Pinguim da Madrugada. Vamos buscar nossa estátua no Frio de Janeiro")
elif encontrado:
    print(
        f"Temos que correr! O Pinguim da Madrugada pode estar no(a) {encontrado}. Vamos salvar nosso Carnaval de Inverno!")
else:
    print("Nosso carnaval de inverno está perdido... NÃOOOOO")
