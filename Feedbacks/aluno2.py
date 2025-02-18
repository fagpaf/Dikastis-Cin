# Q8

num_gojo = input()
num_gojo = num_gojo.split("-")
for x in num_gojo:
    num_gojo[num_gojo.index(x)] = int(x)

maior_seq = []
seq_atual = [num_gojo[0]]
    
for i in range(1, len(num_gojo)):
    if num_gojo[i] == num_gojo[i - 1] + 1:
        seq_atual.append(num_gojo[i])
    else:
        if len(seq_atual) > len(maior_seq):
            maior_seq = seq_atual
        seq_atual = [num_gojo[i]]
    
if len(seq_atual) > len(maior_seq):
    maior_seq = seq_atual
seq_geto = int(input())
soma_geto = int(input())
if len(maior_seq) > seq_geto:
    print("Uma vitória avassaladora de Satoru Gojo. Nem mesmo o infinito pode pará-lo. Ele realmente é o melhor!")
elif seq_geto > len(maior_seq):
    print("Inesperado! Suguru Geto domina com maestria. Uma vitória indiscutível!")
elif sum(maior_seq) > soma_geto:
    print("Gojo vence por pouco. Mesmo com toda a pressão, ele continua no topo!")
elif soma_geto > sum(maior_seq):
    print("Geto vence por pouco. Sua estratégia foi impecável nesta batalha!")
else:
    print("Um empate absoluto! Quem diria que duas lendas podem ser tão iguais em poder?")