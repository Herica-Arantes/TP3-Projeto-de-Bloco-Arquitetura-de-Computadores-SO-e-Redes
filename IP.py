import psutil

interfaces = psutil.net_if_addrs()

for inter in interfaces:
    print(inter)
print("\nInformações sobre a interface Wi-Fi")
print("Endereço físico:", interfaces["Wi-Fi"][0].address)
print("Endereço IP:", interfaces["Wi-Fi"][1].address)
print("Endereço IPv6:", interfaces["Wi-Fi"][2].address)

