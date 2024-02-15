Escolas_de_Samba = ("Porto da Pedra",
"Beija-flor",
"Salgueiro",
"Grande Rio",
"Unidos da Tijuca",
"Imperatriz",
"Mocidade",
"Portela",
"Vila Isabel",
"Mangueira",
"Paraíso do Tuiuti",
"Viradouro")

lista_escolas = {}
encerrar = False
while not encerrar:
  escola = input()
  if escola == "Fim":
    encerrar = True
  else:
    lista.append(escola)
