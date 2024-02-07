def conferir_bits(bit):
  bit = list(bit)
  if len(bit) == 32:
    return ''.join(bit)
  else:
    bit.insert(0, '0')
    return conferir_bits(bit)

def verificação_de_chave(firewall, byte, chances):
    if chances > 0:
      if byte in firewall:
        return "Muito bem! Estamos dentro! Vamos queimar essa cidade!!"
      else:
        chances -= 1
        print("Não é essa a senha, estamos ficando sem tempo.")
        return verificação_de_chave(firewall, byte)
    else:
      return ("Corre Keanu! Eles nos descobriram!!")


palavra = input()
limite_tentativas = int(input())
senha = input()
acesso = verificação_de_chave(conferir_bits(palavra), senha, chances)
print(acesso)