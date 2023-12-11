arsenal = ['Foice de Hades', 'Talismã de Ícaro', 'Elmo da Invisibilidade', 'Cinto de Hermes', 'Espada Anaklusmos', 'Escudo Aegis',  'Adaga Katoptris']
lista_arma_indesejada = []
semideus = input()
# Criando a Matriz das Armas a Serem Removidas
while semideus != 'Parar':
  lista_input = []
  for i in semideus.split('-'):
    lista_input.append(i)
  lista_arma_indesejada.append(lista_input)
  semideus = input()
# 

lista_copia = arsenal[:]
for v in range(len(lista_arma_indesejada)):
  if v == 1:
    print(f' irá batalhar na base do murro!')