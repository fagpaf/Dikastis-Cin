def conferir_bits(bit):
  bit = list(bit)
  if len(bit) == 32:
    return ''.join(bit)
  else:
    bit.insert(0, '0')
    return conferir_bits(bit)

def verificação_de_chave(firewall, byte, chances):
    if byte == firewall[:8]:
      return "Muito bem! Estamos dentro! Vamos queimar essa cidade!!"


palavra = input()
limite_tentativas = int(input())
senha = input()
acesso = verificação_de_chave(conferir_bits(palavra), senha, chances)
print(acesso)