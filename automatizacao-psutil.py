from ast import If
from tokenize import Double
import psutil
from psutil import virtual_memory
import os
from dashing import HSplit, VSplit, VGauge, HGauge, Text
from time import sleep
import pymysql
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# con = pymysql.connect(host='127.0.0.1',user='Leonardo Aguiar',database='db_MeusLivros',cursorclass=pymysql.cursors.DictCursor,password='123')

os.system('cls')
escolha = 0
while escolha != 5:
    os.system('cls')
    print('''Insira o número de acordo com o seu desejo: 
    [1] Memória RAM
    [2] Velocidade da CPU
    [3] Cores
    [4] Disco
    ''')
    escolha = float(input('Entrar: '))

    if escolha == 1:
        os.system('cls')
        # conversão memória virtual em GB
        # (bytes --> kb = total/1024)
        # (bytes --> mb = total/1024/1024)
        # (bytes --> gb = total/1024/1024/1024)

        # memória virtual

        def convert_gb(value):
            return f'{value /1024/1024/1024: .2f}GB' 

        ram = (virtual_memory().total)/1024/1024/1024
        ramU = (virtual_memory().used)/1024/1024/1024
        print("=-="*20)
        print("Memória RAM total na máquina:")
        print('{:.2f}'.format(ram),"GB") #total
        print("Memória RAM sendo utilizada:")
        print('{:.2f}'.format(ramU),'GB') #usando no momento
        print("=-="*20)

        def definirGraficoRAM(frame):
            valores.append(round(psutil.virtual_memory().used / psutil.virtual_memory().total *100, 2))
            valores.remove(valores[0])

            graficosRAM.cla()
            graficosRAM.plot(valores)
            graficosRAM.title.set_text(f'Memoria RAM - {valores[-1]}%')
            graficosRAM.set_ylim(0, 100)

        valores = [0]*50

        janelaGeral = plt.figure(figsize=(3*3, 2*2), facecolor='#EEE')

        graficosRAM = plt.subplot(311)

        graficosRAM.axes.get_xaxis().set_visible(False)
        graficosRAM.set_facecolor('#DDD')

        animacaoGeral = FuncAnimation(janelaGeral, definirGraficoRAM, interval=500)

        plt.show()


        conexao = pymysql.connect(db='dados', user='Leonardo Aguiar', passwd='P00senha')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO registro (ram, ramUtilizada) VALUES ('{:.2f}', '{:.2f}')".format(ram,ramU))
        conexao.commit()
        conexao.close()

        sleep(8)
        # memória virtual
        os.system('cls')
        print("Voltando ao menu...")
        sleep(2)

    elif escolha == 2:
        os.system('cls')
        freq = psutil.cpu_freq().current/1000

        print("=-="*20)
        #velocidade cpu
        print("Velocidade da CPU: ")
        print('{:.2f}'.format(freq),"GHz")
        
        #velocidade cpu
        print("=-="*20)

        def definirGraficoCPU(frame):
            valores.append('{:.3f}'.format(freq))
            valores.remove(valores[0])

            graficosCPU.cla()
            graficosCPU.plot(valores)
            graficosCPU.title.set_text(f'Velocidade CPU - {valores[-1]}GHz')
            graficosCPU.set_ylim(0, 10)

        valores = [0]*50

        janelaGeral = plt.figure(figsize=(3*3, 2*2), facecolor='#EEE')

        graficosCPU = plt.subplot(311)

        graficosCPU.axes.get_xaxis().set_visible(False)
        graficosCPU.set_facecolor('#DDD')

        animacaoGeral = FuncAnimation(janelaGeral, definirGraficoCPU, interval=500)

        plt.show()

        conexao = pymysql.connect(db='dados', user='Leonardo Aguiar', passwd='P00senha')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO registro (velocidadeCPU) VALUES ('{:.2f}')".format(freq))
        conexao.commit()
        conexao.close()

        sleep(8)
        os.system('cls')
        print("Voltando ao menu...")
        sleep(2)

    elif escolha == 3:
        os.system('cls')
        cores = psutil.cpu_count()
        cores_phy = psutil.cpu_count(logical=False)

        print("=-="*20)
        #qtd cores
        print("Quantidade de Cores lógicos: ")
        print(cores)

        print("Quantidade de Cores físicos:")
        print(cores_phy)
        #qtd cores
        print("=-="*20)

        conexao = pymysql.connect(db='dados', user='Leonardo Aguiar', passwd='P00senha')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO registro (qtdCoreLgc, qtdCorePhy) VALUES ('{:.2f}', '{:.2f}')".format(cores, cores_phy))
        conexao.commit()
        conexao.close()

        sleep(8)
        os.system('cls')
        print("Voltando ao menu...")
        sleep(2)

    elif escolha == 4:
        os.system('cls')
        free_disk=(psutil.disk_usage('C:\\').free)/1024/1024/1024
        percentage_disk=(psutil.disk_usage('C:\\').percent)
        print("=-="*20)
        print("Espaço livre no disco: ")
        print('{:.2f}'.format(free_disk),"GB")

        print("Porcentagem de espaço sendo usado no disco: ")
        print('{:.2f}'.format(percentage_disk),"%")
        print("=-="*20)

        def definirGraficoDisco(frame):
            valores.append('{:.2f}'.format(percentage_disk))
            valores.remove(valores[0])

            graficosDisco.cla()
            graficosDisco.plot(valores)
            graficosDisco.scatter(len(valores) - 1, valores[-1])
            graficosDisco.title.set_text(f'Quantidade ocupada no disco - {valores[-1]}%')
            graficosDisco.set_ylim(0, 100)

        valores = [0]*50

        janelaGeral = plt.figure(figsize=(3*3, 2*2), facecolor='#EEE')

        graficosDisco = plt.subplot(311)

        graficosDisco.axes.get_xaxis().set_visible(False)
        graficosDisco.set_facecolor('#DDD')

        animacaoGeral = FuncAnimation(janelaGeral, definirGraficoDisco, interval=500)

        plt.show()

        conexao = pymysql.connect(db='dados', user='Leonardo Aguiar', passwd='P00senha')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO registro (discoLivre, discoOcp_pct) VALUES ('{:.2f}', '{:.2f}')".format(free_disk, percentage_disk))
        conexao.commit()
        conexao.close()

        sleep(8)
        os.system('cls')
        print("Voltando ao menu...")
        sleep(2)

    else:
        print("Insira um dos números a cima!")
        sleep (1.5)



