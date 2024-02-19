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
    "camarao": 30.00,
    "carne de sol": 30.00,
}
caixa = 30

dict_receitas["vinagrete"] = ("coentro", "cebola", "tomate", "pimentao")

loop = False
while not loop:
  pedido = input()
  if pedido not in dict_receitas:
    tupla_ingredientes = ()
    for i in range(9):
      tupla = input(), 
      tupla_ingredientes = tupla_ingredientes + tupla
    dict_receitas[pedido] = tupla_ingredientes
print(dict_receitas)

# Criando um dicionário para o custo de cada receita
dict_precos = {}
for chave, valor in dict_receitas.items():
    custo_total = 0
    # Percorrendo a tupla para calcular o valor de cada ingrediente
    for ingrediente in valor:
        custo_total += dict_ingredientes.get(ingrediente, 0) #.get() recebe 0 como valor padrão para evitar quebra do código
    dict_precos[chave] = (custo_total + 5) # Adicionando os 5 reais q a questão ordena
print(dict_precos)