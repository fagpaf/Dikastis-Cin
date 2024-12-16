orcamento_total = float(input())
numero_convidados = int(input())
local_festa = input()
cantor_convidado = input()
valor_euro = float(input())
conversao = orcamento_total/valor_euro
gasto_convidado = conversao/numero_convidados
if conversao < 1000000:
  print('Acabei de receber a informação que o orçamento total da festa será {:.2f} de euros. Poxa, com um orçamento desses vai ser difícil fazer a festa bombar! Vou divulgar essa informação pros sites de fofocas pra flopar a festa.'.format(conversao))
else:
  print('Poxa, esse cara tá podendo! Vai ser um festão, mas eu vou encontrar alguma coisa para que flope.')
if gasto_convidado >= 5000:
  print('Eita, cancela o repasse da informação pros sites de fofocas! Gastando isso tudo por pessoa, vai continuar sendo um luxo.')
else:
  print('Que vergonha, viu? O povo vai passar fome. Divulgue isso agora!')
if local_festa == 'Hotel Pera Palace' or local_festa == 'Hotel Copacabana Palace':
  print('Eu conheço os donos e são meus amigos! Vou pedir pra recusarem a oferta!')
else:
  print('Poxa, não vou conseguir fazer nada!')
if cantor_convidado == 'Anitta' or cantor_convidado == 'Thiaguinho':
  print(f'Duvido que aceite, Rodri fez isso pra me estressar! Claro que {cantor_convidado} não vai fazer isso comigo!')
else:
  print('Vou fazer uma oferta maior! Isso precisa flopar!')
