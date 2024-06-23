import matplotlib.pyplot as plt
import numpy as np
from colorama import Fore
import os
import random
import time
#Código feito por C0der_Z3r0

os.system('cls') or None
historico_jogador = []
historico_cpu = []
historico_media = []
historico_diferenca = []
historico_desvio = []
historico_variancia = []
coeficientePot = (3/100)*0.33
suaVez = " "
CPU = " "
jogarNovamente = 0
jogoRodando = True
contador = 0.000
contadorCPU = 0.000
contadorLOOP = 0

escolhas = ["Pedra","Papel","Tesoura"]
print("Regras: 1 Pedra, 2 Papel, 3 Tesoura\n")
time.sleep(1.5)

def exibirPontos(contadorCPU,contador):

    media = ((contadorCPU) +(contador))/2
    diferenca = contadorCPU - contador
    historico_media.append(media)
    historico_diferenca.append(diferenca)

    variancia = np.var(historico_jogador + historico_cpu)
    desvio = np.sqrt(variancia)
    historico_variancia.append(variancia)
    historico_desvio.append(desvio)

    print(Fore.GREEN,"Total de pontos do Jogador: ",contador,"....................pts")
    print(Fore.BLUE,"Pontos da CPU..............: ",contadorCPU,".................pts")
    print("Diferença............................: ,",diferenca,".....pts")
    print("Média................................: ",media,".......................pts")
    print("Variância............................: ", variancia)
    print("Desvio Padrão........................: ", desvio)

    labels = ['Jogador', 'CPU', 'Média','Diferença','Desvio P','Variância']
    values = [contador, contadorCPU, media, diferenca,desvio,variancia]

    plt.bar(labels, values, color=['green', 'blue','red','yellow','orange','purple'])
    plt.grid(True)
    plt.xlabel('Dados')
    plt.ylabel('Pontos')
    plt.title('Pontuação de Pedra, Papel e Tesoura')
    plt.show()

    x = np.arange(2)
    y = [contador, contadorCPU]
    y_media_diferenca = [media, diferenca] 
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='blue', label='Pontos')
    plt.plot(x, y_media_diferenca, marker='o', linestyle='--', color='red', label='Média e Diferença')
    plt.xticks(x, ['Jogador', 'CPU'])
    plt.grid(True)
    plt.xlabel('Dados')
    plt.ylabel('Pontos')
    plt.title('Pontuação, Média, Diferença, Desvio e Variância')
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(historico_jogador, marker='o', linestyle='-', color='green', label='Jogador')
    plt.plot(historico_cpu, marker='o', linestyle='-', color='blue', label='CPU')
    plt.plot(historico_media, marker='o', linestyle='-', color='red', label='Media')
    plt.plot(historico_diferenca, marker='o', linestyle='-', color='yellow', label='Diferença')
    plt.plot(historico_variancia, marker='o', linestyle='-', color='purple', label='Variância')
    plt.plot(historico_desvio, marker='o', linestyle='-', color='orange', label='Desvio Padrão')
    plt.grid(True)
    plt.xlabel('Rodadas')
    plt.ylabel('Pontos')
    plt.title('Evolução da Pontuação')
    plt.legend()
    plt.show()
    os.system('pause')

while jogoRodando:
    contadorLOOP += 1
    if contadorLOOP == 10:
        os.system('cls')
        print("Deseja jogar novamente 1(sim)/0(não)?: ")
        jogarNovamente = int(input())
        if jogarNovamente == 1:          
            contadorLOOP = 0 
            exibirPontos(contadorCPU,contador)
            continue
        else:
            jogoRodando = False
            exibirPontos(contadorCPU,contador)
            break   
    os.system('cls') or None
    suaVez = int(input("Sua Vez: "))
    CPU = random.choice(escolhas)
    
    if suaVez == 1:
        print("Você: ",escolhas[0])
        print("CPU.: ",CPU)
        if CPU == escolhas[0]:
            print("empate!")
            contador += 0.5
            contadorCPU += 0.5
            time.sleep(0.9)
        elif CPU == escolhas[1]:
            print("-1 ponto jogador")
            contador -= 1
            contadorCPU += 1
            contadorCPU + coeficientePot
            time.sleep(0.9)
        else:
            print("+1 ponto jogador")
            contador += 1
            contadorCPU -= 1
            contadorCPU + coeficientePot
            contador    + coeficientePot
            time.sleep(0.9)
    if suaVez == 2:
        print("Você: ",escolhas[1])
        print("CPU.: ",CPU)
        if CPU == escolhas[0]:
            print("+1 ponto jogador")
            contador += 1
            contadorCPU -= 1
            contadorCPU + coeficientePot
            contador    + coeficientePot
            time.sleep(0.9)
        elif CPU == escolhas[1]:
            print("empate")
            contadorCPU += 0.5
            contador += 0.5
            time.sleep(0.9)
        else:
            print("-1 ponto jogador")
            contador -= 1         
            time.sleep(0.9)
    if suaVez == 3:
        print("Você: ",escolhas[2])
        print("CPU.: ",CPU)
        if CPU == escolhas[0]:
            print("-1 ponto jogador")
            contador -= 1
            contadorCPU += 1
            contadorCPU + coeficientePot
            contador    + coeficientePot
            time.sleep(0.9)
        elif CPU == escolhas[1]:
            print("+1 ponto jogador")
            contador += 1
            contadorCPU -= 1
            contadorCPU + coeficientePot
            contador    + coeficientePot
            time.sleep(0.9)
        else:
            print("empate")
            contadorCPU += 0.5
            contador += 0.5
            time.sleep(0.9) 
    historico_jogador.append(contador)
    historico_cpu.append(contadorCPU)                         