def conferir_bits(bit):
  bit = list(bit)
  if len(bit) == 32:
    return ''.join(bit)
  else:
    bit.insert(0, '0')
    return conferir_bits(bit)

def fatiamento(firewall, byte, chances):
  if chances > 0:
    
    def():
        if byte == firewall[:7]:
        return "Muito bem! Estamos dentro! Vamos queimar essa cidade!!"
        else:
        if len(firewall) > 7:  
            firewall = firewall[1:]
            return fatiamento(firewall, byte, chances)
        else:


        print("Não é essa a senha, estamos ficando sem tempo.")
        chances -= 1
        
  else:
    return "Corre Keanu! Eles nos descobriram!!"

palavra = input()
limite_tentativas = int(input())
senha = input()
acesso = fatiamento(conferir_bits(palavra), senha, limite_tentativas)
print(acesso)

def verificação_de_chave():