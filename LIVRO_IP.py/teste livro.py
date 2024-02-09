def conferir_bits(bit):
  bit = list(bit)
  if len(bit) == 32:
    return ''.join(bit)
  else:
    bit.insert(0, '0')
    return conferir_bits(bit)


def verificacao_de_chave(firewall, byte, chances, repeticao):
  global chances
  if byte == firewall[:8]:
    return "Muito bem! Estamos dentro! Vamos queimar essa cidade!!"
  else:
    if len(firewall) > 7:  
      firewall = firewall[1:]
      return verificação_de_chave(firewall, byte, chances)
    else:
      repeticao = False
      chances -= 1
      return "Não é essa a senha, estamos ficando sem tempo." 


palavra = input()
limite_tentativas = int(input())
senha = input()
parede_de_fogo = conferir_bits(palavra)
acesso = verificação_de_chave(parede_de_fogo, senha, limite_tentativas, loop)

while loop:
  if limite_tentativas > 0:
    print(acesso)
  else:
    print("Corre Keanu! Eles nos descobriram!!")
    loop = False

if limite_tentativas != 0:
  print(acesso)

