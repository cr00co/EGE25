from ipaddress import*

с = 0

net = ip_network('218.194.82.148/255.255.255.192', 0)

for ip in net.hosts():
    с += 1
print(с)
    