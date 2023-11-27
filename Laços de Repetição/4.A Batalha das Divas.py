# Variaveis Globais:
n = int(input())
nota_final_tay = 0
nota_final_bey = 0
equipe_b = 0
equipe_t = 0
cantora1 = 'Taylor Swift'
cantora2 = 'Beyoncé'
print(f'Vai começar! Vamos ver quem é a verdadeira diva!')
for i in range(1, n+1, 1):
  print(f'Vai começar a {i}º rodada!')
  # Notas:
  nota_coreografia_taylor = int(input())
  nota_final_tay = 4*nota_coreografia_taylor
 
  nota_figurino_taylor = int(input())
  nota_final_tay = 3*nota_figurino_taylor
  
  nota_coreografia_beyonce = int(input())
  nota_final_bey = 4*nota_coreografia_beyonce

  nota_figurino_beyonce = int(input())
  nota_final_bey = 3*nota_figurino_beyonce
# Rounds:
  diff = int(abs(nota_final_bey - nota_final_tay))
  if nota_final_bey < nota_final_tay:
    print(f'Fim da apresentação! O placar da rodada {i} foi {nota_final_tay}x{nota_final_bey} para os representantes da {cantora1}.')
    equipe_t += 1
    equipe_b += 0
    if diff > 20:
      print(f'A diferença na pontuação foi de {diff} pontos.')
    else:
      print(f'A diferença de pontos foi de apenas {diff}.')    
  elif nota_final_tay < nota_final_bey:
    print(f'Fim da apresentação! O placar da rodada {i} foi {nota_final_bey}x{nota_final_tay} para os representantes da {cantora2}.')
    equipe_t += 0
    equipe_b += 1
    if diff > 20:
      print(f'A diferença na pontuação foi de {diff} pontos.')
    else:
      print(f'A diferença de pontos foi de apenas {diff}.')
  elif equipe_b == 3:
    print(f'Uuuh! Por um placar de {equipe_b} a {equipe_t}, a equipe da Beyoncé venceu a competição e mostrou que ela é a verdadeira diva do pop!')
  elif equipe_t == 3:
    print(f'Uuuh! Por um placar de {equipe_t} a {equipe_b}, a equipe da Taylor Swift venceu a competição e mostrou que ela é a verdadeira diva do pop!')