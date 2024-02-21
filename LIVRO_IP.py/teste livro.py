def verificao_de_estoque(dict_receitas, dict_estoque, dict_ingredientes, caixa):
    result = True
    tupla_reposicao = ()
    for ingredientes_receita in dict_receitas.values():
        for ingrediente_estoque in ingredientes_receita:
            # Verificando o estoque
            if dict_estoque[ingrediente_estoque] < 1:
                tupla_reposicao += (ingrediente_estoque, )
    # Repondo o estoque
    if len(tupla_reposicao) > 0:
        custo_reposicao = 0
        for ingrediente_reposicao in tupla_reposicao:
            custo_reposicao += dict_ingredientes.get(ingrediente_reposicao, 0)
            print(custo_reposicao)
        caixa -= custo_reposicao
        # Preparando o pedido
        for ingredientes_receita in dict_ingredientes.keys():
            dict_estoque[ingredientes_receita] -= 1
        
        return reposicao_do_estoque(dict_estoque, caixa)

    # Preparando o pedido
    else:
        for ingredientes_receita in dict_ingredientes.keys():
            dict_estoque[ingredientes_receita] -= 1
        
        return result

def reposicao_do_estoque(dict_receitas, dict_estoque, dict_ingredientes, caixa):
  for ingrediente_reposicao in dict_estoque.keys():
      dict_estoque[ingrediente_reposicao] += 4
  return verificao_de_estoque(dict_receitas, dict_estoque, dict_ingredientes, caixa)

def receita(dict_pedidos, dict_precos, caixa):
    
    result = 0
    result = float(result)

    total_de_vendas = 0
    for pedido, quantidade in dict_pedidos.items():
        preco = dict_precos.get(pedido, 0)
        total_item = quantidade * preco
        total_de_vendas += total_item
        
    result += caixa + total_de_vendas
    return result


caixa = 30
dict_receitas = {
    "bobo de camarao": ("camarao", "macaxeira", "leite de coco", "dende", "tomate", "cebola"),
    "tapioca de carne de sol": ("massa de tapioca", "carne de sol", "queijo coalho", "tomate", "cebola"),
    "carne de sol com macaxeira": ("carne de sol", "macaxeira", "manteiga"),
    "camarao na moranga": ("moranga", "camarao", "cebola", "alho", "tomate", "pimentao", "creme de leite", "azeite", "coentro")
}
dict_ingredientes = {
    "coentro": 1.00,
    "alho": 1.50,
    "cebola": 2.00,
    "pimentao": 2.00,
    "macaxeira": 3.00,
    "tomate": 3.00,
    "creme de leite": 4.00,
    "leite de coco": 5.00,
    "manteiga": 5.50,
    "moranga": 10.00,
    "massa de tapioca": 10.00,
    "dende": 15.00,
    "azeite": 15.00,
    "queijo coalho": 15.00,
    "camarao": 30.00,
    "carne de sol": 30.00,
}
# Criando o estoque do restaurante
dict_estoque = {}
for ingrediente in dict_ingredientes:
    dict_estoque[ingrediente] = 5

# Loop dos inputs e criando o dicionário de pedido para saber qual o mais vendido
dict_pedidos = {}
condicional = 0
loop = False
while not loop:
    try:
        pedido = input()
        if pedido not in dict_receitas:
            condicional += 1
            if condicional == 3: # Limita as duas entradas do pedido
                print(f"Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Sabores de Recife.")
                # Tupla para ser concatenada e ser o valor da nova receita no dict_receitas
                tupla_ingredientes = ()
                for i in range(9):
                    tupla = input(), 
                    tupla_ingredientes += tupla # Concatenando a tupla para "adicionar" os ingredientes do novo pedido
                dict_receitas[pedido] = tupla_ingredientes
                # Criando o dict_pedidos
                if pedido not in dict_pedidos:
                    dict_pedidos[pedido] = 1
                else:
                    dict_pedidos[pedido] += 1
            else:
                print(f"{pedido} ainda não é uma opção disponível.")
        else:
            print(f"{pedido} saindo...")
            # Criando o dict_pedidos
            if pedido not in dict_pedidos:
                dict_pedidos[pedido] = 1
            else:
                dict_pedidos[pedido] += 1
    except EOFError:
        loop = True
print("##### Fim do expediente #####")

# Criando um dicionário para o custo de cada receita
dict_precos = {}
for chave, valor in dict_receitas.items():
    custo_total = 0
    # Percorrendo a tupla para calcular o valor de cada ingrediente
    for ingrediente in valor:
        custo_total += dict_ingredientes.get(ingrediente, 0) #.get() recebe 0 como valor padrão para evitar quebra do código
    if len(dict_receitas) > 4:
        dict_precos[chave] = (custo_total + 5) # Adicionando os 5 reais q a questão ordena
    else:
        dict_precos[chave] = custo_total

num_pedidos = 0
for qtd_pedidos in dict_pedidos.values():
    num_pedidos += qtd_pedidos

while num_pedidos > 0:
    dispensa = verificao_de_estoque(dict_receitas, dict_estoque, dict_ingredientes, caixa)
    if dispensa == True:
        if num_pedidos == 1:
            lucro = receita(dict_pedidos, dict_precos, caixa)
    else:
        repositorio = reposicao_do_estoque(dict_receitas, dict_estoque, dict_ingredientes, caixa)
        if num_pedidos == 1:
            lucro = receita(dict_pedidos, dict_precos, caixa)
    num_pedidos -= 1
lucro -= 30
print(f"O lucro obtido no dia de hoje foi de R${lucro:.2f}.")

# Usando "max" para determinar o pedido mais vendido e .capitalize() para iniciar o nome do pedido com letra maiúscula
mais_vendido = max(dict_pedidos, key = dict_pedidos.get)
if mais_vendido == "bobo de camarao":
    print("O bom e tradicional Bobó de Camarão, líder em vendas, nunca será superado!")
else:
    print(f"{mais_vendido.capitalize()} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário Bobó de Camarão.")

print(dict_estoque)