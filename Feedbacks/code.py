jogador1 = input()
pontosj1 = int(input())
jogador2 = input()
pontosj2 = int(input())
jogador3 = input()
pontosj3 = int(input())

if jogador1 == "Lucas Lima" or jogador2 == "Lucas Lima" or jogador3 == "Lucas Lima":
  print("Deu a lógica! Acabou caô, o Lucas Lima ganhoooouuu, Lucas Lima ganhoooouu oohhh!!!")
elif pontosj3 < pontosj1 > pontosj2:  
  print(f"{jogador1} é eleito o bola de ouro!")
elif pontosj1<pontosj2>pontosj3:
  print(f"{jogador2} é eleito o bola de ouro!")
else:
  print(f"{jogador3} é eleito o bola de ouro!")