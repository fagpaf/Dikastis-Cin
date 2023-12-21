def max(a, b):
  if a> b:
    return a
  else:
    return b
qtd_dias = int(input())
numero_dia = 1
total_ovos_encontrados = 0
total_ovos_escondidos = 0
for i in range(1, qtd_dias + 1):
  ovos_escondidos_dia = int(input())
  horoscopo_dia = input()
  ovos_encontrados = 0 
  if horoscopo_dia == "Os astros estão radiantes hoje! Eles farão o possível para abençoar a todos com boa sorte.":
    ovos_encontrados = ovos_escondidos_dia
  if horoscopo_dia == "Os astros estão de bom humor hoje. Acho que você terá um pouco de sorte extra.":
    ovos_encontrados = (ovos_escondidos_dia * 0.7)
  if horoscopo_dia == "As estrelas estão neutras hoje. O dia está em suas mãos.":
    ovos_encontrados = int(max(ovos_escondidos_dia * 0.7, ovos_escondidos_dia / ((ovos_escondidos_dia % numero_dia) + 1)))
  if horoscopo_dia == "Isso é raro. As estrelas estão absolutamente neutras hoje.":
    ovos_encontrados = (ovos_escondidos_dia % numero_dia) + 1
  if horoscopo_dia == "Hoje, Kiq não pôde consultar as estrelas. Sem a orientação astrológica, a busca por ovos fica à mercê do destino.":
    numero_dia += 1
  total_ovos_encontrados += ovos_encontrados
  total_ovos_escondidos += ovos_escondidos_dia
  print(f"Dia {i}")
  print(f"Hoje Carlos encontrou {ovos_encontrados} ovos!!")
print(f"Kiq encontrou {total_ovos_encontrados} de um total de {total_ovos_escondidos}")
aproveitamento = (total_ovos_encontrados / total_ovos_escondidos) * 100
if aproveitamento == 
 print("Incrível! Seu signo está em alta. Você encontrou todos os ovos!")