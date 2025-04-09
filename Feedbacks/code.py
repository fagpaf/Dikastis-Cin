def chamar_informação(lideres, acontecimentos): #Função para chamar informações
    comando = input()
    if comando == 'FIM':
        return lideres, acontecimentos
    else: 
        if comando == 'REGISTRAR LÍDER': #Verificar o tipo de comando 
            nome = input()
            cargo = input()
            origem = input()
            nascimento = input()
            informacoes = {'cargo': (cargo), 'origem': (origem), 'nascimento': (nascimento)}
            lideres[nome] = informacoes
        elif comando == 'REGISTRAR ACONTECIMENTO':
            data = input()
            acontecimento = input()
            local = input()
            informacoes = {'data': (data), 'local': (local)}
            acontecimentos[acontecimento] = informacoes
        chamar_informação(lideres, acontecimentos) #Chamar a função recursivamente 
        return lideres, acontecimentos
    
lideres = {}
acontecimentos = {}

chamar_informação(lideres, acontecimentos)
impressoes_lideres = ('Consegui encontrar os seguintes líderes da Revolução Pernambucana de 1817:', 'Aff, pelo jeito nessa época não tinha LinkedIn pra facilitar encontrar os tais líderes dessa tal Revolução... Desisto.')
impressoes_acontecimentos = ('Vivenciei os seguintes acontecimentos históricos da Revolução Pernambucana de 1817:', 'Ter que ler todos esses jornais não é legal, e ainda não encontrei nenhum acontecimento... saudade do Pernambuco Extraordinário pra me manter informado.')
if lideres != {}: #Printar os líderes
    print(impressoes_lideres[0])
    for i in lideres.keys():
        informacoes = lideres[i]
        cargo = informacoes['cargo']
        origem = informacoes['origem']
        nascimento = informacoes['nascimento']
        print(f'{i}:')
        print(f'- Cargo/Papel: {cargo}')
        print(f'- Cidade de Origem: {origem}')
        print(f'- Data de Nascimento: {nascimento}')
else:
    print(impressoes_lideres[1])
print()

if acontecimentos != {}: #Printar os acontecimentos
    print(impressoes_acontecimentos[0])
    for i in acontecimentos.keys():
        informacoes = acontecimentos[i]
        data = informacoes['data']
        local = informacoes['local']
        print(f'({data}): {i}, {local}')

else:
    print(impressoes_acontecimentos[1])

if lideres != {} and acontecimentos != {}:
    print()
    print('Pronto, agora CIn tô preparado pra lutar e tornar Pernambuco o melhor país em linha reta do mundo!!!')
