def conferir_bits(bit):
  bit = list(bit)
  if len(bit) == 32:
    return ''.join(bit)
  else:
    bit.insert(0, '0')
    return conferir_bits(bit)

def tentativa(chances):
  if chances > 0:
    def verificação_de_chave(firewall, byte, chances):
      nonlocal chances
      if byte == firewall[:8]:
        return "Muito bem! Estamos dentro! Vamos queimar essa cidade!!"
      else:
        if len(firewall) > 7:  
          firewall = firewall[1:]
          return verificação_de_chave(firewall, byte, chances)
        else:
          chances -= 1
          return "Não é essa a senha, estamos ficando sem tempo." 
  else:
    return "Corre Keanu! Eles nos descobriram!!"

palavra = input()
limite_tentativas = int(input())
senha = input()
parede_de_fogo = conferir_bits(palavra)
funcao_principal = tentativa(limite_tentativas)
acesso = funcao_principal(parede_de_fogo, senha, limite_tentativas)
print(acesso)

