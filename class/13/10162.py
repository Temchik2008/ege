from ipaddress import *
#
# ip = ip_address('192.128.6.0')
# net = ip_network(f'{ip}/255.255.240.0', False)
# net1 = ip_network(f'{ip}/20', False)
#
# net1.hosts()
# net1.broadcast_address
# net.network_address
# net.netmask
# net.num_addresses
#
# bin_ip = f'{int(ip):032b}'

ip1 = ip_address('112.117.10.70')
ip2 = ip_address('112.117.121.80')

for mask in range(16, 31)[::-1]:
    net1 = ip_network(f'{ip1}/{mask}', False)
    if ip1 in net1.hosts() and ip2 in net1.hosts():
        print(net1.netmask)
        break