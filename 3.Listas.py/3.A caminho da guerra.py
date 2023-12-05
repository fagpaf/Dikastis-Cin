#Itens que Procura
lista_deseja = []
itens_que_deseja = input()
lista_deseja = itens_que_deseja.split(', ')
#Itens Encontrados no Acampamento 
lista_encontrou = []
itens_que_encontrou = input()
lista_encontrou = itens_que_encontrou.split(', ')

lista_agrupamento = []
for i in lista_deseja:
  if i in lista_encontrou:
    lista_agrupamento.append(i)
print('sds')