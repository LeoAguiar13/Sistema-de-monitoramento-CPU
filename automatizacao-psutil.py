from tokenize import Double
import psutil
from psutil import virtual_memory
import os

# conversão memória virtual em GB
# (bytes --> kb = total/1024)
# (bytes --> mb = total/1024/1024)
# (bytes --> gb = total/1024/1024/1024)

# memória virtual
os.system('cls')
def convert_gb(value):
    return f'{value /1024/1024/1024: .2f}GB' 

ram = (virtual_memory().total)/1024/1024/1024
ramU = (virtual_memory().used)/1024/1024/1024

print("Memória RAM total na máquina:")
print('{:.2f}'.format(ram),"GB") #total
print("Memória RAM sendo utilizada:")
print('{:.2f}'.format(ramU),'GB') #usando no momento
# memória virtual


print("=-"*20)
freq = psutil.cpu_freq().current/1000
cores = psutil.cpu_count()
cores_phy = psutil.cpu_count(logical=False)

#velocidade cpu
print("Velocidade da CPU: ")
print('{:.2f}'.format(freq),"GHz")
#velocidade cpu

#qtd cores
print("Quantidade de Cores lógicos: ")
print(cores)

print("Quantidade de Cores físicos:")
print(cores_phy)
#qtd cores


free_disk=(psutil.disk_usage('C:\\').free)/1024/1024/1024
percentage_disk=(psutil.disk_usage('C:\\').percent)
print("=-"*20)
print("Espaço livre no disco: ")
print('{:.2f}'.format(free_disk),"GB")

print("Porcentagem de espaço sendo usado no disco: ")
print('{:.2f}'.format(percentage_disk),"%")

