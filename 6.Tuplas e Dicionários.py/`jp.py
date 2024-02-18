def calcular_penalidade(tempo_desfile):
  penalidade_por_minuto = 0.1
  tempo_minimo = 65
  tempo_maximo = 75
  if tempo_desfile < tempo_minimo:
    return (tempo_minimo - tempo_desfile) * penalidade_por_minuto
  elif tempo_desfile > tempo_maximo:
    return (tempo_desfile - tempo_maximo) * penalidade_por_minuto
  else:
    return 0
  
escolas = []

condicao = True
while condicao:
  nome = input()
  if nome != "Não há mais escolas":
    tema = input()
    tempo_desfile = int(input())
    escolas.append({"nome": nome, "tema": tema, "tempo_desfile": tempo_desfile})
  else:
    condicao = False

qtd_escolas = len(escolas)
notas_por_quesito = {}

condicao_2 = True
while condicao_2:
  quesito = input()
  if quesito != "Não há mais quesitos":
    for i in range(qtd_escolas):
      entrada = input().split(" - ")
      escola = entrada[0]
      nota = float(entrada[1])
      notas_por_quesito[quesito] = notas_por_quesito.get(quesito, []) + [nota]
  else:
    condicao_2 = False

print("Desfile de samba do Rio de janeiro 2024")

notas_por_escola = {}
for escola in escolas:
  notas_por_escola[escola["nome"]] = []
  for quesito, notas in notas_por_quesito.items():
    nota = notas[escolas.index(escola)]
    notas_por_escola[escola["nome"]].append(nota)

for quesito, notas in notas_por_quesito.items():
  print(f"Vamos às notas para o quesito {quesito}:")
  for i, escola in enumerate(escolas):
    nota = notas[i]
    if nota == int(nota):
      nota = int(nota)
    print(f"{escola['nome']}: {nota}")

notas_finais = {}
for escola in escolas:
  notas = notas_por_escola[escola["nome"]]
  nota_final = sum(notas) / len(notas) - calcular_penalidade(escola["tempo_desfile"])
  notas_finais[escola["nome"]] = nota_final

vencedor = max(notas_finais, key=notas_finais.get)
nota_vencedor = round(notas_finais[vencedor], 2)

print(f"E o vencedor do desfile de escola de samba do Rio de Janeiro de 2024 é:")
print(f"{vencedor} com uma nota final de {nota_vencedor}!")