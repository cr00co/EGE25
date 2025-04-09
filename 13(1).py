from ipaddress import*

c = 0
net = ip_network('228.135.92.192/255.255.255.240', 0)

for ip in net:
    x = bin(int(ip))[2:].zfill(32)
    if x.count('0') > 15:
        c += 1
print(c)