def zap_vida(vida): #Função para a arma zap, possui duas funções separadas para retornar em uma a vida na outra a velocidade
    vida -= 5
    return vida

def zap_velocidade(velocidade):
    velocidade -= 1
    return velocidade

def powpow(vida): #Função arma powpow
    vida -= 15
    return vida

def fishbones_vida(vida): #Função para a arma zap, uma para a vida outra para a velocidade
    vida -= 30
    return vida

def fishbones_defesa(defesa):
    defesa = 0
    return defesa

def lanca_missil(uso, vida): #Função para o missil, variavel uso, pois só pode ser usado uma vez
    if uso == 0:
        vida -= 100
    return vida

def com_defesa(distancia_op, vida_op, velocidade_op, uso_missil):
    if distancia_op>= 30:
        vida = vida_op 
        defesa = fishbones_defesa(defesa_op)
        velocidade_ = velocidade_op   
        uso = uso_missil
        print('A defesa dele foi destruída com o poder da Fishbones!')
            
    else:
        vida = vida_op 
        velocidade_ = zap_velocidade(velocidade_op)
        defesa = defesa_op
        uso = uso_missil
        print('Ele está com defesa e está muito perto!')

    vida_velocidade = [vida, velocidade_, defesa, uso]
    return vida_velocidade

def sem_defesa(distancia_op, vida_op, velocidade_op, uso_missil):
    if distancia_op >= 50 and uso_missil == 0:
            vida = lanca_missil(uso_missil, vida_op)
            uso = 1
            velocidade_ = velocidade_op
            defesa = defesa_op
            print('Ele vai ser transformado em cinzas pelo SUPER MÍSSIL!')
            
    elif distancia_op>=30:
        vida =fishbones_vida(vida_op)
        velocidade_ = velocidade_op   
        defesa = defesa_op
        uso = uso_missil
        print('Vamos derretê-lo com a Fishbones!')
        
    elif distancia_op >= 15:
        vida = powpow(vida_op)
        velocidade_ = velocidade_op  
        defesa = defesa_op
        uso = uso_missil
        print('Jinx vai encher esse cara de buracos agora.')
        
    else:
        vida = zap_vida(vida_op)
        velocidade_ = zap_velocidade(velocidade_op)
        defesa = defesa_op
        uso = uso_missil
        print('Você foi zapeado hahaha.')
        
    vida_velocidade = [vida, velocidade_, defesa, uso]
    return vida_velocidade

def decisao(distancia_op, vida_op, velocidade_op, uso_missil): #Função para a decisão das armas
    resultado = []
    if defesa_op > 0: #Caso tenha defesa
        resultado = com_defesa(distancia_op, vida_op, velocidade_op, uso_missil)

    else: #Caso não tenha defesa
        resultado = sem_defesa(distancia_op, vida_op, velocidade_op, uso_missil)
    return resultado


entrada = input()

lista_info = entrada.split(' - ') #Receber e separar as informações do oponente
oponente = lista_info[0]
vida_op = int(lista_info[1])
distancia_op = int(lista_info[2])
velocidade_op = int(lista_info[3])
defesa_op =  int(lista_info[4])
uso_missil = 0

print(f'Andando pelas ruas de Zaun, jinx dá de cara com um {oponente} e agora vão lutar.')

while vida_op>0 and distancia_op>0: #Condição para que ainda haja ataque 
    informacoes = decisao(defesa_op, distancia_op)
    vida_op = informacoes[0]
    velocidade_op = informacoes[1]
    defesa_op = informacoes[2]
    uso_missil = informacoes[3]
    if velocidade_op > 0:
        distancia_op -= velocidade_op
    else:
        distancia_op -=1

if vida_op <= 0: #Jinx ganhe
    print('Ninguem é capaz de derrotar a Jinx!!!')

else: #Jinx perca
    print('Ah não, A Jinx foi PEGA!')