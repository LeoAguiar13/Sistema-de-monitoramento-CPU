from ast import If
from tokenize import Double
import psutil
from psutil import virtual_memory
import os
from dashing import HSplit, VSplit, VGauge, HGauge, Text
from time import sleep

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

        sleep(12)
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
        sleep(12)
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
        sleep(12)
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
        sleep(12)
        os.system('cls')
        print("Voltando ao menu...")
        sleep(2)

    else:
        print("Insira um dos números a cima!")
        sleep (1.5)



