def conferir_bits(bit):
  bit = list(bit)
  if len(bit) == 32:
    return ''.join(bit)
  else:
    bit.insert(0, '0')
    return conferir_bits(bit)


def fatiamento(firewall, byte, chances):
  if len(firewall) > 7:  
    firewall = firewall[1:]
    return verificacao_de_chave(firewall, byte, chances)
  else:
    x = chances - 1 
    if chances > 0:
      print("Não é essa a senha, estamos ficando sem tempo.")
      return x
    else:
      return "Corre Keanu! Eles nos descobriram!!"


def verificacao_de_chave(firewall, byte, chances):
  if byte == firewall[:8]:
    return "Muito bem! Estamos dentro! Vamos queimar essa cidade!!"
  else:
    return fatiamento(firewall, byte, chances)

palavra = input()
limite_tentativas = int(input())
senha = input()
parede_de_fogo = conferir_bits(palavra)
acesso = verificacao_de_chave(parede_de_fogo, senha, limite_tentativas)
print(acesso)
