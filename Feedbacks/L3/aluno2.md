Rafael Victor

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

## 2. Variáveis
Você teve alguns problemas ao criar suas variáveis: elas são **grandes**. Tenho uma dica para você no problema **6**. Tente optar por nomes mais curtos e descritivos, que sejam claros mas não excessivamente longos.
A falta de variáveis também precisa de ajuste como na questão **5**.

---

## 3. Mistura de idiomas no código
Gostaria de pontuar sobre a questão **8**, onde você utilizou uma variável com o nome `"score"`.  
Neste caso específico, não houve impacto a curto prazo pela mistura de inglês e português. No entanto, caso você utilizasse a variável `"score"` em outra operação e tivesse mais variáveis em inglês, seu código poderia ficar **inconsistente** e com **déficit de legibilidade**.

![Var](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/L1/Captura%20de%20tela%202024-12-15%20204609.png)

Em contextos colaborativos, é essencial adotar um padrão consistente, escolhendo apenas **um idioma** para nomear variáveis. Isso será especialmente relevante no projeto final da cadeira.


## 4. Ótimas resoluções
Queria enfatizar aqui o seu domínio com os **Comandos Condicionais**, com resoluções mais avançadas como na primeira questão.

![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/L1/Captura%20de%20tela%202024-12-16%20125338.png)

---

## Conclusão
Bom, eram esses os comentários que eu tinha para fazer.  
Mais uma vez, **parabéns** por concluir a lista toda!  

Qualquer dúvida que você tiver sobre a lista ou algo que eu expliquei, pode me buscar no Discord. Meu login é **fagpaf**.  
**Tamo junto!**


Q5:
Na declaração das variáveis você poderia ter criado duas variáveis uma chamada **gasto_convidado** e a outra **conversao** elas deixariam seu código mais legível e bem estruturado, sem a necessidade de usar várias vezes **"orcamento_total"**.

![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/L1/Captura%20de%20tela%202024-12-16%20124729.png)

Q6:
Você deixou as suas variáveis com nomes muito grandes, o que dificulta a legibilidade do seu código.  
Uma solução seria retirar a parte **empresa**, ficando desse modo abaixo.

![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/L1/Captura%20de%20tela%202024-12-16%20113716.png)

Em vez de usar **“k”** como variável de distância, você poderia ter utilizado uma abreviação de distância para deixar seu código mais legível.

![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/L1/Captura%20de%20tela%202024-12-16%20113911.png)

Outra dica é ativar o **Word Wrap** no **VSCode**, que quebra automaticamente a linha para facilitar a leitura do código por completo.

Q10:
Vi que você utilizou **{int(vini)}** no print da **linha 75** o que não é um problema, porém você poderia ter resolvido isso na **linha 21**. Aqui vai duas maneiras de se fazer isso explicitamente:

![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/L1/Captura%20de%20tela%202024-12-16%20122743.png)