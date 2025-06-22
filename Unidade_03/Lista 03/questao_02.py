N = int(input("Quantidade de jogadores? "))
print("Digite os dados para cada jogador")

nome = []
s = []
b = []
a =[]
s1 = []
b1 = []
a1 = []

for i in range(N):
    info = input().split()
    nome.append(info[0])
    s.append(int(info[1]))
    b.append(int(info[2]))
    a.append(int(info[3]))
    s1.append(int(info[4]))
    b1.append(int(info[5]))
    a1.append(int(info[6]))

porcentagem_saques = (sum(s1)/sum(s)) * 100
porcentagem_bloqueio = (sum(b1)/sum(b)) * 100
porcentagem_ataque = (sum(a1)/sum(a)) * 100

print("As estatísticas do jogo são as seguintes: ")
print(f'Pontos de Saque: {porcentagem_saques:.2f}%')
print(f'Pontos de Bloqueio: {porcentagem_bloqueio:.2f}%')
print(f'Pontos de Ataque: {porcentagem_ataque:.2f}%')