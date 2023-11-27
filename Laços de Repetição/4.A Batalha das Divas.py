n = int(input())
nota_final_t = 0
nota_final_b = 0
cantora1 = 'Taylor Swift'
cantora2 = 'Beyoncé'
diff = int(abs(nota_final_b - nota_final_t))
print(f'Vai começar! Vamos ver quem é a verdadeira diva!')
for i in range(1, n+1):
    print(f'Vai começar a {i}º rodada!')
    nota_coreografia_taylor = int(input())
    nota_final_t = 4*nota_coreografia_taylor
    
    nota_figurino_taylor = int(input())
    nota_final_t = 3*nota_figurino_taylor
    
    nota_coreografia_beyonce = int(input())
    nota_final_b = 4*nota_coreografia_beyonce
    
    nota_figurino_beyonce = int(input())
    nota_final_b = 3*nota_figurino_beyonce
    
    if nota_final_b < nota_final_t:
        print(f'Fim da apresentação! O placar da rodada {i} foi {nota_final_t}x{nota_final_b} para os representantes da {cantora1}.')
        if diff > 20:
            print(f'A diferença na pontuação foi de {diff} pontos.')
        else:
            print(f'A diferença de pontos foi de apenas {diff}.')
        print(f'Uuuh! Por um placar de {nota_final_t} a {nota_final_b}, a equipe da Taylor Swift venceu a competição e mostrou que ela é a verdadeira diva do pop!')
    elif nota_final_t < nota_final_b:
        print(f'Fim da apresentação! O placar da rodada {n} foi {nota_final_t}x{nota_final_b} para os representantes da {cantora2}.')
        if diff > 20:
            print(f'A diferença na pontuação foi de {diff} pontos.')
        else:
            print(f'A diferença de pontos foi de apenas {diff}.')
        print(f'Uuuh! Por um placar de {nota_final_b} a {nota_final_t}, a equipe da Beyoncé venceu a competição e mostrou que ela é a verdadeira diva do pop!')