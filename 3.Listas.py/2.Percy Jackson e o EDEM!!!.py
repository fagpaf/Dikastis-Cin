Q = int(input())
Q_respostas = input()
Respostas_Percy = Q_respostas.split(',')
# Lista correta 
gabarito = [
{'Nome': 'Zeus', 'Especialidade': 'trovão', 'Natureza': 'deus'},
{'Nome': 'Afrodite', 'Especialidade': 'amor', 'Natureza': 'deusa'},
{'Nome': 'Poseidon', 'Especialidade': 'oceanos', 'Natureza': 'deus'},
{'Nome': 'Hércules', 'Especialidade': 'força', 'Natureza': 'semideus'},
{'Nome': 'Aquiles', 'Especialidade': 'resistência', 'Natureza': 'semideus'},
{'Nome': 'Orfeu', 'Especialidade': 'música', 'Natureza': 'semideus'}
]
# Situações
if Q == 0:
  print('Infelizmente, Percy Jackson, chegou atrasado para a exame...')
else:
  for n in range(Q):
        print(f'A resposta da {n}ª questão está... CORRETA!')
        print(f'A resposta da {n}ª questão está... ERRADA!')