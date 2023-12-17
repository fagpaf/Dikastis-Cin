grego_antigo = input()
lista = []
# Verifica se a Mensagem é um Espaço Vazio
if grego_antigo == " ":
  print('Ué não tem nada para me decifrar aqui')
# Iterando o Input para Somar com o ord()
else:
  for char in grego_antigo:
    lista.append(char)
# Descobrir o Valor Decimal e o Caractere da Tabela ASCII
    frase_decifrada = []
for char in grego_antigo:
    if char == " ":
        frase_decifrada.append(" ")       
    else:
        n = ord(char)
        soma = n + len(lista)
        caractere = chr(soma)
        frase_decifrada.append(caractere)
print('Descobri o que a mensagem significa: ' + "".join(frase_decifrada))