def conferir_bits(bit):
    if len(bit) == 32:
        return bit
    else:
        bit.insert(0, '0')
        return conferir_bits(bit)
palavra = input()
lista = list(palavra)
resultado = conferir_bits(lista)
print(''.join(resultado))