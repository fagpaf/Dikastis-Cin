loop = True
while loop:
  nome_pretendente = input()
  palavra_pretendente = input()
  palavra_taylor = input()
  if palavra_taylor == 'vou dormir':
    loop = False
  for i in(palavra_taylor):
    palavra_pretendente = palavra_taylor.replace('1', '', 1)
    print(palavra_pretendente)
    print(f'você acertou, estreou na lista! {nome_pretendente}')
  else:
    print(f'perdeu covarde!')