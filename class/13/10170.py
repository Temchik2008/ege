from ipaddress import *

ip1 = ip_address('193.175.175.231')
ip2 = ip_address('193.175.176.118')

for mask in range(16, 31):
    net1 = ip_network(f'{ip1}/{mask}', False)
    if ip1 in net1.hosts() and ip2 not in net1.hosts():
        print(net1.netmask)
        break