escolas_de_samba = ("Porto da Pedra", "Beija-flor", "Salgueiro", "Grande Rio", "Unidos da Tijuca", "Imperatriz", "Mocidade", "Portela", "Vila Isabel", "Mangueira", "Paraíso do Tuiuti", "Viradouro")
dict_escolas = {}
lista_primeira_aparicao = []
encerrar = False
# Loop para receber os inputs e formar o dicionário
while not encerrar:
  escola = input()
  if escola == "Fim":
    encerrar = True
  else:
    chave, valor = escola.split(":")
    # Verifica se a chave já existe no dictonário
    if chave in dict_escolas:
      print(f"{chave} teve sua nota atualizada!")
    dict_escolas[chave] = float(valor)
    if chave not in escolas_de_samba:
      print("Epa, o que essa escola está fazendo aqui?!")
    else:
      # Verifica se é a primeira aparição da chave
      if chave not in lista_primeira_aparicao:
        print(f"{chave} teve sua nota apurada!")
        lista_primeira_aparicao.append(chave)
    if chave not in escolas_de_samba:
      del dict_escolas[chave]

sorted_escolas = sorted(dict_escolas, key = dict_escolas.get, reverse = True)
idx = 1
for key, value in sorted_escolas:
  print(f"{idx}. {key}: {value}")
  idx += 1
x = 1
for key, value in sorted_escolas:
  if x == 1:
    print(f"É CAMPEÃ! A ESCOLA {key} É A GRANDE VENCEDORA DO CARNAVAL DE 2024, FAZENDO {value} PONTOS!!")
  if x == 12:
    print(f"Infelizmente, a escola {key} não alcançou as expectativas, fazendo apenas {value} pontos, e foi rebaixada.")
  x +=1







sorted(dict_escolas, key = dict_escolas.get, reverse = True)
