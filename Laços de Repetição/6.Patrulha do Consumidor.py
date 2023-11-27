numero_compradores = int(input())
contador_criterios = 0
total_suspeitos = 0
impar = 0
for i in range(1, numero_compradores + 1):
  nome_comprador = input()
  cpf_comprador = input()
  nome_identidade = input()
  cpf_identidade = input()
  qtd_ingressos = int(input())
  preco_total_ingressos = float(input())
  codigo_compra = input()
  if nome_comprador == nome_identidade:
    contador_criterios += 0
  elif nome_comprador != nome_identidade:
    contador_criterios += 1
  elif cpf_comprador == cpf_identidade:
    contador_criterios += 0
  elif cpf_comprador != cpf_identidade:
    contador_criterios += 1
  elif qtd_ingressos > 12:
    contador_criterios += 1
  elif qtd_ingressos < 12:
    contador_criterios += 0
  elif preco_total_ingressos > 1500:
    contador_criterios += 1
  elif preco_total_ingressos < 1500:
    contador_criterios += 0
  for i in str(codigo_compra):
    digito = int(i)
    if digito % 2 != 0:
      impar += 1
      if 7 <= impar:
        contador_criterios += 1
      else:
        contador_criterios += 0
    else:
      impar += 0
if 3 <= contador_criterios:
  total_suspeitos += 1
else:
  total_suspeitos += 0
print(f'Total de compradores analisados: {numero_compradores}') 
print(f'Total de suspeitas de cambistas: {total_suspeitos}')
