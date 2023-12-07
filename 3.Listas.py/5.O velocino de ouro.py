informacoes_deuses = [['Zeus', 'Poseidon', 'Atenas', 'Ares', 'Afrodite'], [100, 90, 80, 70, 60], ['Raio', 'Tridente', 'Égide', 'Lança', 'Cinto Mágico']]
sequencia = input()
for n in sequencia:
  print(f'Deus:{informacoes_deuses[0][int(n)]}')