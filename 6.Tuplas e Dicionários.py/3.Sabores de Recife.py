dict_receitas = {
    "bobo de camarao": ("camarao", "macaxeira", "leite de coco", "dende", "tomate", "cebola"),
    "tapioca de carne de sol": ("massa de tapioca", "carne de sol", "queijo coalho", "tomate", "cebola"),
    "carne de sol com macaxeira": ("carne de sol", "macaxeira", "manteiga"),
    "camarao na moranga": ("moranga", "camarao", "cebola", "alho", "tomate", "pimentao", "creme de leite", "azeite", "coentro")
}

dict_ingredientes = {
    "tomate": 3.00,
    "cebola": 2.00,
    "coentro": 1.00,
    "manteiga": 5.50,
    "macaxeira": 3.00,
    "alho": 1.50,
    "pimentao": 2.00,
    "azeite": 15.00,
    "camarao": 30.00,
    "carne de sol": 30.00,
    "queijo coalho": 15.00,
    "massa de tapioca": 10.00,
    "leite de coco": 5.00,
    "dende": 15.00,
    "creme de leite": 4.00,
    "moranga": 10.00,
}
caixa = 30
for chave in dict_receitas:
  for i in range(len(dict_receitas[chave])):
    comida, ingrediente = dict_receitas[chave][i]
    print(comida)
    print(ingrediente)