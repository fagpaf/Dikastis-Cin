def preencher_zeros(p):
  if len(p) == 32:
    return "".join(p)
  else:
    p = list(p)
    p.insert(0,"0")
    return preencher_zeros(p)

def verificar_chave(b, firewall,t):
  if t <= 0:
    return "Corre Keanu! Eles nos descobriram!!"
  else:
    if len(firewall) < 8:
      t -= 1  
      print("Não é essa a senha, estamos ficando sem tempo.") 

  if b == firewall[:8]:
    return "Muito bem! Estamos dentro! Vamos queimar essa cidade!!"
  else:
    return verificar_chave(b, firewall[1:],t)
  
palavra = preencher_zeros(input())
qtd_tentativas = int(input())
byte = input()
resultado = verificar_chave(byte, palavra, qtd_tentativas)
print(resultado)