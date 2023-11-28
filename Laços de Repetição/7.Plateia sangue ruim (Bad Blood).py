num_versos = int(input())
acerto_plateia = 0
for i in range(1, num_versos + 1):
  input_plateia = input()
  digito = int(i)
  if input_plateia == input_plateia.upper():
    acerto_plateia += 1
  # 1° verso
  if digito == 1:
    print("Cause, baby, now we've got")
    print(f'{input_plateia.upper()}')
  # 2° verso 
  elif digito == 2:
    print('You know it used to be')
    print(f'{input_plateia.upper()}')
  # 3° verso 
  elif digito == 3:
    print('So take a look what')
    print(f'{input_plateia.upper()}')
  # 4° verso 
  elif digito == 4:
    print("Cause, baby, now we've got")
    print(f'{input_plateia.upper()}')
if acerto_plateia == num_versos:
    print('A plateia deu um show! Acertou tudo!')
elif (num_versos * 0.5) <= acerto_plateia:
    print('A plateia acertou a maior parte da música')
else:
    print('Foi um dia atípico e a plateia se esqueceu de grande da música')