from ipaddress import *

ip = ip_address('218.48.192.0')
ip_host = ip_address('218.48.192.56')

for mask in range(18, 25):
    net = ip_network(f'{ip}/{mask}', False)
    if ip_host in net.hosts() and ip == net.network_address:
        if net.num_addresses - 2 >= 500:
            print(net.netmask)
