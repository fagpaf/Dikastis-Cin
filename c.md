# Classificação de Energia Amaldiçoada

Em *Jujutsu Kaisen*, os seres (maldições e feiticeiros) possuem diferentes classes de poder com base em seu nível de energia amaldiçoada. Escreva um programa em Python que classifique um ser com base no nível de energia amaldiçoada fornecido pelo usuário.

### O programa deve:
1. Solicitar ao usuário um número inteiro positivo que represente o nível de energia amaldiçoada do ser.
2. Com base no nível de energia, classifique o ser nas seguintes categorias:
   - **Classe Baixa**: nível entre 1 e 10
   - **Classe Média**: nível entre 11 e 30
   - **Classe Alta**: nível entre 31 e 50
   - **Classe Especial**: nível acima de 50
3. Se o número fornecido for menor que 0, exiba a mensagem:
   - `"Energia insuficiente para classificação."`
4. O programa será encerrado quando a entrada for igual a **0**.

Input
- O programa deve receber um único valor:
  - **`nível_energia`**: um número inteiro que representa o nível de energia amaldiçoada do ser.
  - **Condições**: 
    - Deve ser um número inteiro positivo. 
    - Se o valor for menor que 0, a energia é considerada insuficiente.

Output
- Com base no valor de `nível_energia`, o programa deve imprimir uma mensagem que indica a classe do ser:
  - Se `nível_energia` está entre **1 e 10**: Imprimir `"Classe Baixa"`
  - Se `nível_energia` está entre **11 e 30**: Imprimir `"Classe Média"`
  - Se `nível_energia` está entre **31 e 50**: Imprimir `"Classe Alta"`
  - Se `nível_energia` é **maior que 50**: Imprimir `"Classe Especial"`
  - Se `nível_energia` é **menor que 0**: Imprimir `"Energia insuficiente para classificação."`

### Exemplo de entrada e saída:
Case 1:
Input:
5
25
45
60
0

Output:
Classe Baixa
Classe Média
Classe Alta
Classe Especial

Case 2:
Input:
-1
0

Output:
Energia insuficiente para classificação.

### Escreva seu código abaixo:

# Inicializa a variável de controle
var = True
while var:
    nivel_energia = int(input())
    
    # Verificando o nível de energia
    if nivel_energia == 0:
      var = False
    elif nivel_energia < 0:
      print("Energia insuficiente para classificação.")
    elif 1 <= nivel_energia <= 10:
      print("Classe Baixa")
    elif 11 <= nivel_energia <= 30:
      print("Classe Média")
    elif 31 <= nivel_energia <= 50:
      print("Classe Alta")
    else:
      print("Classe Especial")