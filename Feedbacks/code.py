def processamento_cadeia(condicoes, contagem, matriz, estado, binario1, estado1, estado2, binario2): #Função para separar os estados e os números referentes as mudanças
    if qtd_estados <10:
        for condicao in condicoes:
            conexao = (f'q{contagem}') 
            binario1 = condicao[:1]
            estado1 = condicao[4:6]
            binario2 = condicao[8:9]
            estado2 = condicao[12:14]
            linha = [conexao, binario1, estado1, binario2, estado2]
            matriz.append(linha)
            contagem += 1
        linha = [conexao, binario1, estado1, binario2, estado2]
        matriz.append(linha)
        contagem += 1

    else:
        for condicao in condicoes:
            conexao = (f'q{contagem}') 
            for letra in condicao:
                x = letra.isalnum()
                if x == True:
                    estado +=letra
                else:
                    if estado != '':
                        if binario1 == '':
                            binario1 = estado
                        elif estado1 == '':
                            estado1 = estado
                        elif binario2 == '':
                            binario2 = estado
                        estado = ''   
                                           
            estado2 = estado 
            linha = [conexao, binario1, estado1, binario2, estado2]
            matriz.append(linha)
            contagem += 1
            binario1 = ''
            estado1 = ''
            binario2 = ''
            estado2 = ''
            estado = ''

    return matriz #Retorna como uma matriz, onde cada linha é referente as condições de um qn    
    
def registro_conexoes(estado_atual, alteracoes, cadeias_aceitas, rejeicao): #Função para verificar as cadeias
    if cadeia_binaria == 'ε':
        if estado_atual == estado_aceitacao:
            print('Caramba, essa cadeia é abençoada! Nem precisei trabalhar!')
            cadeias_aceitas +=1 #Variável para controlar a quantidade de cadeias aceitas 
        else:
            print('Nossa, que maldição! Nem começou e já deu errado…')

    else:
        for elemento in cadeia_binaria: #Fazer verificação bit por bit 
            
            if elemento != '0' and elemento != '1' and rejeicao == False: #Variável Rejeição é para a cadeia para de ser verificada caso haja um erro 
                print(f'Só pode estar de brincadeira comigo! Como vou lidar com {elemento} dentro da máquina?')
                rejeicao = True
                alteracoes.append('ERROR')
            elif rejeicao == False: 
                linha = int(estado_atual.replace('q', ''))-1
                mudanca = matriz[linha].index(elemento)
                estado_anterior = estado_atual
                estado_atual = matriz[linha][mudanca + 1]
                if estado_anterior != estado_atual:
                    alteracoes.append(estado_atual)

        if estado_atual == estado_aceitacao and rejeicao ==False:
            print('Beleza! Após suar muito a cadeia foi aceita, o esforço ta sendo compensado!')
            cadeias_aceitas += 1
        elif rejeicao ==False: 
            print('Que tristeza, todo esse arrudeio pra nada…')

    alteracoes = impressao_alteracoes(alteracoes) #Essa lista de alteções é usada para mostras na ordem a sequencia de mudanças na linha do tempo
    return estado_atual, cadeias_aceitas, alteracoes

def impressao_conexões(matriz, num_linha): #Print das conexoes no início 
    for i in range(qtd_estados):
        linha_atual = matriz[num_linha]
        print(f'{linha_atual[0]}: {{{linha_atual[1]} -> {linha_atual[2]}, {linha_atual[3]} -> {linha_atual[4]}}}') 
        num_linha += 1

def impressao_alteracoes(alteracoes):
    impressao = ' -> '.join(alteracoes)
    print(f'{{{impressao}}}')
    alteracoes = []
    return alteracoes

binario1 = ''
estado1 = ''
binario2 = ''
estado2 = ''
contagem = 1
matriz = []
condicoes = []
rejeicao = False
num_linha = 0
alteracoes = []
cadeias_aceitas = 0 
qtd_estados = int(input())
estado = ''

if qtd_estados >1:#Verificar se tem mais de uma dimensão 
    estado_aceitacao = input()

    for i in range(qtd_estados):
        condicao = input()
        condicoes.append(condicao)
    qtd_cadeias = int(input())

    matriz = processamento_cadeia(condicoes, contagem, matriz, estado, binario1, estado1, estado2, binario2)
    impressao_conexões(matriz, num_linha)

    for j in range(qtd_cadeias): #Para cada cadeia será repetido o processo de verificar suas cadeias de bits 
        cadeia_binaria = input()
        estado_atual = input()
        alteracoes.append(estado_atual)
        estado_atual, cadeias_aceitas, alteracoes = registro_conexoes(estado_atual, alteracoes, cadeias_aceitas, rejeicao)

    razao = cadeias_aceitas/qtd_cadeias #Verificar a razão entre as cadeias aceitas e o total de cadeias 
    if razao == 1:
        print('Sensacional :)! Com certeza vamos voltar pra casa com esse autômato, até Alan Turing teria inveja!')
    elif razao >= 0.75:
        print('Show de bola! Se fizermos alguns ajustes nesse autômato, temos muitas chances de voltar pra casa!')
    elif razao >= 0.5:
        print('Até que esse autômato da pro gasto, mas vamos precisar de uns bons ajustes…')
    elif razao >= 0.25:
        print('Nossa, que situação horrível, não faço a mínima ideia de como concertar esse autômato')
    else:
        print('Nossas expectativas já eram baixas, mas não sabia que seria tão catastrófico assim :/')
else: 
    print('É… acho que não tem muito o que fazer com apenas uma dimensão, vou ter que me contentar com minha triste realidade :(')