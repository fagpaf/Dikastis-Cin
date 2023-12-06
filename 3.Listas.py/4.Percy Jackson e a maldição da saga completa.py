colecao_sergio = input().split(', ')
qtd_total_edicoes = int(input())
livros_percy = ['O Ladrão de Raios', 'O Mar de Monstros', 'A Maldição do Titã', 'A Batalha do Labirinto', 'O Último Olimpiano']
lista_verificacao = []
for i in livros_percy:
  if i in colecao_sergio:
    lista_verificacao.append(i)
if lista_verificacao == livros_percy:
  print('Sua coleção está completa! Você pode ler à vontade.')
elif lista_verificacao 