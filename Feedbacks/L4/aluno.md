# Feedback da Lista 4 - Funções


Olá, **Raissa!** Tudo bem?
Espero que tenha aproveitado bem o Carnaval. **Parabéns** por ter concluído a Lista 4! Agora, vamos ao feedback.

---

## 1. Falta de parâmetros nas Funções
Nas questões **3** e **4** eu reparei que você não passou os parâmetros para essas funções, isso é uma má prática e que torna difícil de se ler o código. Imagine se você tivesse feito assim na **Q5**, prefira sempre fazer suas funções do jeito que você fez ela e tá tudo certo.
![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/2025/L4/Q3.png)
![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/2025/L4/Q4a.png)

**Raissa**, mais uma vez, ***parabéns*** pelo seu esforço e dedicação! Seu progresso é notável, e essas observações são apenas ajustes para tornar seu código ainda mais eficiente e claro.

A variável ``razaorecurso``
![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/2025/L4/Q2.png)


Q3 e Q4
falta de parâmetros na função
![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/2025/L4/Q3.png)
![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/2025/L4/Q4a.png)

Q5
Você poderia ter dividido a def ``decisao`` do modo a seguir fazendo com que ficasse mais legível e modularizado, com essas duas novas def's recebendo as linhas de código contidas originalmente.
![Código Corrigido](https://raw.githubusercontent.com/fagpaf/Images/refs/heads/main/2025/L4/Q5.png)

```python
def decisao(distancia_op, vida_op, velocidade_op, uso_missil): #Função para a decisão das armas
    resultado = []
    if defesa_op > 0: #Caso tenha defesa
        resultado = com_defesa(distancia_op, vida_op, velocidade_op, uso_missil)

    else: #Caso não tenha defesa
        resultado = sem_defesa(distancia_op, vida_op, velocidade_op, uso_missil)
    return resultado
