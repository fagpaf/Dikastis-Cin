def conferir_bits(bit):
    bit = list(bit)
    if len(bit) == 32:
        return ''.join(bit)
    else:
        bit.insert(0, '0')
        return conferir_bits(bit)

def verificacao_de_chave(firewall, byte, chances):
    if chances > 0:
        if byte in firewall:
            return "Muito bem! Estamos dentro! Vamos queimar essa cidade!!"
        else:
            chances -= 1
            print("Não é essa a senha, estamos ficando sem tempo.")
            return verificacao_de_chave(firewall, byte, chances)
    else:
        print("Corre Keanu! Eles nos descobriram!!")
        return "Acesso negado"

palavra = input("Digite a palavra do firewall: ")
limite_tentativas = int(input("Digite o limite de tentativas: "))
senha = input("Digite a senha: ")
acesso = verificacao_de_chave(conferir_bits(palavra), senha, limite_tentativas)
print(acesso)
