Rafael Nóbrega

# Feedback da Lista 1 - Comandos Condicionais

Olá, Rafael! Tudo certo?!
Sou **Flávio** e, durante esse período, vou ficar responsável por te mandar feedbacks das tuas listas. Esses feedbacks têm o intuito de te fazer melhorar ainda mais. A gente pode dar dicas de boas práticas, outras possíveis soluções e coisas do gênero.

Antes de começar, queria te **parabenizar** por ter conseguido fazer todas as questões! O importante é sempre tentar resolver todas, porque é isso que traz familiaridade com a linguagem.

Sem mais delongas, vamos ao **Feedback da Lista 1**.

---

## 1. Comentários no código
Queria começar falando sobre o uso de **comentários no código**.
Por questão de boa prática e **manutenção de código**, a utilização de comentários é fundamental. Hoje você sabe tudo o que está acontecendo no programa, mas daqui a 2 meses será que você vai se lembrar? Outra vantagem é que, na hora de tirar uma dúvida, a pessoa que for te ajudar terá muito mais facilidade em entender o que você escreveu.

---
## 2. Uso de str()
Percebi que vc usa muito **“str(input())”**, mas isso não é necessário pois em python a entrada já é uma string.

![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/L1/Captura%20de%20tela%202024-12-16%20112424.png)

---

## 3. Nomes das variáveis
Você está tendo um problema ao criar suas variáveis: elas são muito **grandes**. Tenho dicas específicas para você nos problemas **6** e **7**. Tente optar por nomes mais curtos e descritivos, que sejam claros mas não excessivamente longos.

---

## 4. Mistura de idiomas no código
Gostaria de pontuar sobre a questão **8**, onde você utilizou uma variável com o nome `"score"`.  
Neste caso específico, não houve impacto a curto prazo pela mistura de inglês e português. No entanto, caso você utilizasse a variável `"score"` em outra operação e tivesse mais variáveis em inglês, seu código poderia ficar **inconsistente** e com **déficit de legibilidade**.

![Var](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/L1/Captura%20de%20tela%202024-12-15%20204609.png)

Em contextos colaborativos, é essencial adotar um padrão consistente, escolhendo apenas **um idioma** para nomear variáveis. Isso será especialmente relevante no projeto final da cadeira.

---

## Conclusão
Bom, eram esses os comentários que eu tinha para fazer.  
Mais uma vez, **parabéns** por concluir a lista toda!  

Qualquer dúvida que você tiver sobre a lista ou algo que eu expliquei, pode me buscar no Discord. Meu login é **fagpaf**.  
**Tamo junto!**



Q4:
Você criou duas variáveis **voto1** e **voto2**, que não fazem diferença para o seu código. A **atribuição de 0** para representar votos inválidos não tem impacto prático, pois não há um momento em que os valores de **voto1** e **voto2** sejam usados para qualquer lógica adicional.

![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/L1/Captura%20de%20tela%202024-12-16%20111239.png)

A validação de votos inválidos já está sendo tratada pela não contagem nos totais **qtd_vinijr** e **qtd_rodri**.

Q5:
Na **linha 13** você usou novamente **gasto_convidado**, mas por questão de legibilidade você poderia ter feito na **linha 7** mesmo na primeira declaração.

Não precisava usar  **orcamento_total = float(orcamento_total / valor_euro)**, pois como essa variável já foi declarada como **float** anteriormente ela manterá o valor em float, sem precisar de conversão explícita.
![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/L1/Captura%20de%20tela%202024-12-16%20112806.png)

Q6:
Você deixou as suas variáveis com nomes muito grandes, o que dificulta a legibilidade do seu código.  
Uma solução seria retirar a parte **empresa**, ficando desse modo abaixo.

![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/L1/Captura%20de%20tela%202024-12-16%20113716.png)

Em vez de usar **“k”** como variável de distância, você poderia ter utilizado uma abreviação de distância para deixar seu código mais legível.

![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/L1/Captura%20de%20tela%202024-12-16%20113911.png)

Outra dica é ativar o **Word Wrap** no **VSCode**, que quebra automaticamente a linha para facilitar a leitura do código por completo.

Q7:
Você poderia ter feito as variáveis **menores**, isso deixaria seu código mais limpo e legível, segue um modo de se fazer isso.

![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/L1/Captura%20de%20tela%202024-12-16%20114527.png)