def conferir_bits(bit):
  bit = list(bit)
  if len(bit) == 10:
    return ''.join(bit)
  else:
    bit.insert(0, '0')
    return conferir_bits(bit)


def fatiamento(firewall, byte, chances):
  if len(firewall) > 7:
    firewall = firewall[1:]
    return verificacao_de_chave(firewall, byte, chances)
  else:
    if chances > 0: 
      parede_copia = parede_de_fogo[:]
      return "Não é essa a senha, estamos ficando sem tempo."
    else:
      return "Corre Keanu! Eles nos descobriram!!"


def verificacao_de_chave(parede_copia, byte, chances):
  if byte == parede_copia[:8]:
    global senha_correta
    senha_correta = True
    return "Muito bem! Estamos dentro! Vamos queimar essa cidade!!"
  else:
    return fatiamento(parede_copia, byte, chances)

palavra = input()
limite_tentativas = int(input())
senha_correta = False
while limite_tentativas > 0 and not senha_correta:
  senha = input()
  parede_de_fogo = conferir_bits(palavra)
  parede_copia = parede_de_fogo[:]
  acesso = verificacao_de_chave(parede_de_fogo, senha, limite_tentativas)
  print(acesso)
  limite_tentativas -= 1