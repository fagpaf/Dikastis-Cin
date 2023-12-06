colecao_sergio = input().split(', ')
qtd_total_edicoes = int(input())
livros_percy = ['O Ladrão de Raios', 'O Mar de Monstros', 'A Maldição do Titã', 'A Batalha do Labirinto', 'O Último Olimpiano']
lista_verificacao = []
for i in livros_percy:
  if i in colecao_sergio:
    lista_verificacao.append(i)
livros_faltando = []
for j in colecao_sergio:
  if j not in livros_percy:
    livros_faltando.append(j)
if lista_verificacao == livros_percy:
  print('Sua coleção está completa! Você pode ler à vontade.')
elif 0 < lista_verificacao < (livros_percy):
  print(f'Infelizmente, sua coleção está incompleta. Falta(m) esse(s) livro(s): {livros_faltando}.')
