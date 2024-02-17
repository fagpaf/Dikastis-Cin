# Montando Lista de Lista para facilitar o uso dos input's
lista_total = []
loop = False
while not loop:
  escola = input()
  if escola == "Não há mais escolas":
    loop = True
  else:
    tema_desfile = input()
    tempo_limite = int(input())
    lista_total.append([escola, tema_desfile, tempo_limite])

# Criando um dicionário com Listas para facilitar o uso dele
dict_notas = {}
continuar = False
while not continuar:
  # Essa Lista irá receber as Notas dos input's
  lista_do_dicionario = []
  quesito = input()
  if quesito == "Não há mais quesitos":
    continuar = True
  else:
    # Utilizando for para não ter erro na montagem do dicionário e renovar o input da Nota
    for i in range(len(lista_total)):
      avaliacao = input()
      nome, nota = avaliacao.split(" - ")
      nota = float(nota)
      lista_do_dicionario.append([nome, nota])
    if len(lista_do_dicionario) == len(lista_total):
      # O Valor é a Lista 
      dict_notas[quesito] = lista_do_dicionario

for chave in dict_notas:
  print(f"{chave}:")
  #pesquisar como isso funciona
  for i in range(len(dict_notas[chave])):
    escola, nota = dict_notas[chave][i]
  ######################################
    if nota == 10: 
      nota = int(nota)
      print(f"{escola}: {nota}")
    else:
      print(f"{escola}: {nota}")


print(f"E o vencedor do desfile de escola de samba do Rio de Janeiro de 2024 é:\n{nome_vencedor} com uma nota final de {nota_vencedor}!")