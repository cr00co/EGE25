from ipaddress import*

for m in range(33):
    net = ip_network(f'218.194.82.148/{m}', 0)
    if str(net.network_address) == '218.194.82.128':
        print(m)
 
