import psutil

mem = psutil.virtual_memory()

total = mem.total / pow(2, 30)
print("Total de memória:", round(total, 1), "GB")
disponivel = mem.available / pow(2, 30)
print("Memória disponível:", round(disponivel, 1), "GB")
print("Percentual de mem. utilizado:", mem.percent, "%")
usada = mem.used / pow(2, 30)
print("Memória utilizada:", round(usada, 1), "GB")
livre = mem.free / pow(2, 30)
print("Memória livre:", round(livre, 1), "GB")