import psutil

disco = psutil.disk_usage(".")
print(disco)
print("Total:", disco.total, "bytes")
print("Em uso:", disco.used, "bytes")
print("Livre:", disco.free, "bytes")
print()
print("Total:", round(disco.total / pow(2, 30), 0), "GB")
print("Em uso:", round(disco.used / pow(2, 30), 0), "GB")
print("Livre:", round(disco.free / pow(2, 30), 0), "GB")
print("Percentual de uso:", disco.percent, "%")