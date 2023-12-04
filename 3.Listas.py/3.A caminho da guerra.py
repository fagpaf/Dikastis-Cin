lista_deseja = ['']
lista_encontrou = ['']
itens_que_deseja = input()
itens_que_encontrou = input()
lista_deseja += itens_que_deseja.split(', ')
lista_encontrou += itens_que_encontrou.split(', ')
print('Estes são os itens que já tenho no Acampamento Meio-Sangue:')

for i, item in enumerate