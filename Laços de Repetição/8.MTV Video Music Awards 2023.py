vencedor = ""
numero_celebridades = int(input())
for i in range(1, numero_celebridades + 1):
  celebridade = input()
  print(f'Apresentador: Contamos com a ilustre presença de {celebridade}, uma salva de palmas!')
# Candidatos ao Prêmio VMA
loop = True
while loop:
  nome_candidato = input()
  if nome_candidato == 'Início da Premiação':
    loop = False
  if loop == True:
    # Premiação
      possivel_ganhadora1 = 'Taylor Swift'
      possivel_ganhadora2 = 'Katy Perry'
      possivel_ganhadora3 = 'Ariana Grande'
      possivel_ganhadora4 = 'Beyoncé'
      possivel_ganhadora5 = 'Shakira'
      #print(f'Apresentador: Vamos deixar de enrolação e ir para a premiação!')
      #print(f'Apresentador: E a artista do ano do MTV Video Music Awards 2023 é...')
      # Taylor Swift Win
      print(nome_candidato)
      if (nome_candidato == possivel_ganhadora1) or (vencedor == possivel_ganhadora1):
        vencedor = possivel_ganhadora1
      # Katy Parry Win
      elif (nome_candidato == possivel_ganhadora2) or (vencedor == possivel_ganhadora2):
        vencedor = possivel_ganhadora2
      # Ariana Grande Win
      elif (nome_candidato == possivel_ganhadora3) or (vencedor == possivel_ganhadora3):
        vencedor = possivel_ganhadora3
      elif (nome_candidato == possivel_ganhadora4) or (vencedor == possivel_ganhadora4):
        vencedor = possivel_ganhadora4
      # Shakira Win
      elif (nome_candidato == possivel_ganhadora5) or (vencedor == possivel_ganhadora5):
        vencedor = possivel_ganhadora5
        
print(vencedor)