entrada = 'inicio'
qtd_bonecos = 0
qtd_videogames = 0
qtd_bicicletas = 0
qtd_outros = 0

# Entrada de presentes

while (entrada != 'FIM'):
    entrada = input()
    if entrada != 'FIM':
        if entrada == 'Boneco':
            qtd_bonecos +=1
            print('Mais um presente saindo!')
        elif entrada == 'Videogame':
            qtd_videogames +=1
            print('Mais um presente saindo!')
        elif entrada == 'Bicicleta':
            qtd_bicicletas +=1
            print('Mais um presente saindo!')
        else:
            qtd_outros +=1
            print('Esse presente não está sendo fabricado nesse momento')

#pct presentes 

pct_boneco = (qtd_bonecos/(qtd_bonecos + qtd_bicicletas + qtd_videogames + qtd_outros))*100
pct_videogames = (qtd_videogames/(qtd_bonecos + qtd_bicicletas + qtd_videogames + qtd_outros))*100
pct_bicicleta = (qtd_bicicletas/(qtd_bonecos + qtd_bicicletas + qtd_videogames + qtd_outros))*100
pct_outros = (qtd_outros/(qtd_bonecos + qtd_bicicletas + qtd_videogames + qtd_outros))*100

# Relatório dos presentes

print('Vamos agora ao relatório dos presentes!\n')
print(f'Boneco - {qtd_bonecos} unidades - {pct_boneco:.2f}%')
print(f'Videogame - {qtd_videogames} unidades - {pct_videogames:.2f}%')
print(f'Bicicleta - {qtd_bicicletas} unidades - {pct_bicicleta:.2f}%')
print(f'Outros - {qtd_outros} unidades - {pct_outros:.2f}%')

if qtd_outros == 0:
    print('A demanda está muito alta! Teremos que fazer mais uma fábrica!')
elif pct_outros > 50:
    print('Parece que o Papai Noel terá que fechar a fábrica :(')
elif pct_boneco <= 50 and pct_bicicleta <= 50 and pct_videogames <= 50 and pct_outros <= 50:
    print('A fábrica está cumprindo seu papel, porém não precisa ser expandida')
elif pct_boneco > 50:
    print('Boneco está sendo muito desejado! A fábrica terá que ser expandida!')
elif pct_bicicleta > 50:
    print('Bicicleta está sendo muito desejado! A fábrica terá que ser expandida!')
elif pct_videogames > 50:
    print('Videogame está sendo muito desejado! A fábrica terá que ser expandida!')