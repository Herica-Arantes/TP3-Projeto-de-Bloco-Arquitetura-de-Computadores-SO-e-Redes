import platform
import psutil, time
import cpuinfo

info = cpuinfo.get_cpu_info()

print("Marca do processador:", platform.processor())
print("Nome da máquina:", platform.node())
print("Versão do SO:", platform.platform())
print("SO:", platform.system())
print("Arquitetura:", info["arch"])
print("Processador:", info["brand_raw"])
print("Registradores:", info["bits"], "bits")
print("Número de núcleos:", psutil.cpu_count())
print("Número de núcleos físicos:", psutil.cpu_count(logical=False))
print("Frequência do processador:", psutil.cpu_freq().current, "MHz")

print(type(info))
for i in info:
    print(i, ":", info[i])

for i in range(10):
    print("Uso de CPU:", psutil.cpu_percent(), "%")
    time.sleep(1)

