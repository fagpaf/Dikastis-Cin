Pedro

# Feedback da Lista 3 - Listas

Olá, Pedro! Tudo certo?  
Aqui é **Flávio**, **parabéns** por ter conseguido fazer todas as questões!
Vamos ao **Feedback da Lista 3**.

---

## 1. Comentários no código
Queria começar falando novamente sobre o uso de **comentários no código**. Chamando a atenção novamente, porque nas partes importantes do código onde você está **impondo sua lógica** é importante fazer isso. Caso isso se repita principalmente nessas últimas listas ***considerarei reduzir as notas***, pois será complicado avaliar as questões nas próximas listas.

---

## 2. Uso excessivo de Break
Você está tendo um problema ao utilizar **break**, aparentemente você não sabe como funciona. Recomendo você usar condicionais **booleanas** para aprender melhor como lidar com isso dei umas dicas de como fazer nas questões **1** e **2**. 
O uso excessivo de break pode ser considerado como um método **Go Horse**.

---

## Conclusão
Bom, eram esses os comentários que eu tinha para fazer.  
Mais uma vez, **parabéns** por concluir a lista toda!  

Qualquer dúvida que você tiver sobre a lista ou algo que eu expliquei, pode me buscar no Discord. Meu login é **fagpaf**.  
**Tamo junto!**

Q1 e Q2:
uso de break

Q2: Você utilizou **break** na linha 13, porém de maneira desnecessária, pois você poderia apenas identar o código. Quando ``dupla_alunos != 'Acabou!'`` o loop seria encerrado do modo desejado.

![Código Corrigido]()

Q3:
Você fez a questão utilizando as ideias de condicionais, o que não é mais viável, pois você tem uma funcionalidade poderosa disponível agora, as Listas veja como ficaria se você tivesse utilizado.

Melhorias:
1- Criar uma lista para armazenar os nomes dos monitores por categoria, assim:
    ``tipos = ["aprimoradores", "emissores", "transmutadores", "manipuladores", "conjuradores", "especialistas"]``
2- Lista de frases correspondentes:
``frases = ["O volume da água foi alterado.", "A cor da água foi alterada.", "O gosto da água foi alterado.", "A folha se moveu.", "Impurezas apareceram na água."]``

Fazer isso evitaria as condicionais da **linha 18** e deixaria mais legível seu código.
![Código Corrigido]()

3- Uma lista para fazer a remoção monitores:
``grupos = [aprimoradores, emissores, transmutadores, manipuladores, conjuradores, especialistas]``

Ao em vez de fazer como na **linha 14**, ficaria assim:
![Código Corrigido]()

Q4:
Mesmo ponto da Q2, era só colocar a condicional desse modo e identar o resto do código para dentro desse ``if`` que faria a mesma coisa do jeito que você fez:
``if tipo_item != 'Catalogação encerrada!':``

Q5: 
Na **linha 12** você utilizou ``continue``, mais uma vez e você tivesse feito um ``else``, seria o suficiente
![Código Corrigido]()


Q6:
Na **Linha 8** poderia ter feito assim:
``feiticeiros_principal.append([nome_feiticeiro, nivel_energia])``





Q7:
2 imagens para ser comentadas, >= e f.append
![Código Corrigido]()
![Código Corrigido]()

Q8:
Utilize **abreviações** para os nomes das variáveis.  
Por exemplo: `nome_jogador` pode ser reduzido para `nome_jgd1`, e assim por diante, substituindo "jogador" por "jgd".
![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/L1/Captura%20de%20tela%202024-12-15%20204556.png)

--------------------------------------------------------------------------------------------------------

