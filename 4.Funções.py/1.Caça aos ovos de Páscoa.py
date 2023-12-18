qtd_dias = int(input())
ovos_escondidos_dia = input()
horoscopo_dia = input()
ovos_encontrados = 0
numero_dia
ovos_encontrados_dia
# Cálculo Ovos Encontrados 
if horoscopo_dia == "Os astros estão radiantes hoje! Eles farão o possível para abençoar a todos com boa sorte.":
    ovos_encontrados = ovos_escondidos_dia
if horoscopo_dia == "Os astros estão de bom humor hoje. Acho que você terá um pouco de sorte extra.":
    ovos_encontrados = (ovos_escondidos_dia * 0.7)
if horoscopo_dia == "As estrelas estão neutras hoje. O dia está em suas mãos.":
    ovos_encontrados = max(ovos_escondidos_dia * 0.7, ovos_escondidos_dia / ((ovos_escondidos_dia % numero_dia) + 1))
if horoscopo_dia == "Isso é raro. As estrelas estão absolutamente neutras hoje.":
    ovos_encontrados = (ovos_escondidos_dia % numero_dia) + 1
if horoscopo_dia == "Hoje, Kiq não pôde consultar as estrelas. Sem a orientação astrológica, a busca por ovos fica à mercê do destino.":


aproveitamento = (total_ovos_encontrados / total_ovos_escondidos) * 100

    print(f"Dia {i}")
    print(f"Hoje Carlos encontrou {ovos_encontrados_dia} ovos!!")