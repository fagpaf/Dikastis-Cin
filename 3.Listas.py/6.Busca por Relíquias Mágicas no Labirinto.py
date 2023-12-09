matriz = []
qtd_reliquias = 0
sequencia = input()
# Loop da Matriz
while sequencia != 'Fim do labirinto':
    linha_matriz = []
    for i in sequencia.split():
      algarismo = int(i)
      linha_matriz.append(algarismo)
      if algarismo == 1:
        qtd_reliquias += 1
    matriz.append(linha_matriz)
    sequencia = input()
# Condicionais Para o Print
if qtd_reliquias != 0:
  print('Relíquias encontradas nos seguintes locais:')
  for v_linha, linha in enumerate(matriz):
    for v_coluna, valor in enumerate (linha):
      if valor == 1:
        print(f'linha: {v_linha}, coluna: {v_coluna}')
else:
  print('Nenhuma relíquia encontrada no labirinto.')