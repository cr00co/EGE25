from ipaddress import*

for m in range(0, 33):
    net1 = ip_network(f'157.127.172.56/{m}', 0)
    net2 = ip_network(f'157.127.191.78/{m}', 0)
    if str(net1.network_address) != str(net2.network_address):
        print(m)
        break