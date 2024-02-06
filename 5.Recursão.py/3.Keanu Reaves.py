def conferir_bits(bit):
    if len(lista) == 32:
        return lista
    else:
        lista.insert(0, '0')
        return conferir_bits(lista)


def verificação_de_chave(senha, firewall):




palavra = input()
lista = [] 
limite_tentativas = int(input())
byte = input()