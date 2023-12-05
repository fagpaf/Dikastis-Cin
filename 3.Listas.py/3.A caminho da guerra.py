#Itens que Procura
lista_deseja = []
itens_que_deseja = input()
lista_deseja = itens_que_deseja.split(', ')
x = int(len(lista_deseja))
#Itens Encontrados no Acampamento 
lista_encontrou = []
itens_que_encontrou = input()
lista_encontrou = itens_que_encontrou.split(', ')
y = int(len(lista_encontrou))
if x > y:
print('Estes são os itens que já tenho no Acampamento Meio-Sangue:')
  for i in range(1, x+1):
    print(f"{i}° item: {lista_deseja.idx(i)}")
