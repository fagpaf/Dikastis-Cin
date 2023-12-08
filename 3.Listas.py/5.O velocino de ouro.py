informacoes_deuses = [['Zeus', 'Poseidon', 'Atenas', 'Ares', 'Afrodite'], [100, 90, 80, 70, 60], ['Raio', 'Tridente', 'Égide', 'Lança', 'Cinto Mágico']]
sequencia = input()
lista_algarismos = []
for i in sequencia:
  lista_algarismos.append(int(i))
for n in lista_algarismos:
  if (0 <= n < 2) or (n == 3):
    print(f'Deus:{informacoes_deuses[0][int(n)]}')
    print(f'Poder:{informacoes_deuses[1][int(n)]}')
    print(f'Artefato:{informacoes_deuses[2][int(n)]}')
    print()
  elif (n == 2):
    print(f'Deusa:{informacoes_deuses[0][int(n)]}')
    print(f'Poder:{informacoes_deuses[1][int(n)]}')
    print(f'Artefato:{informacoes_deuses[2][int(n)]}')
    print()
  elif (n == 4):
    print(f'Deusa:{informacoes_deuses[0][int(n)]}')
    print(f'Poder:{informacoes_deuses[1][int(n)]}')
    print(f'Artefato:{informacoes_deuses[2][int(n)]}')