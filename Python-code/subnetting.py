

def subnetting(question='192.168.10.5/16'):
    ip = question.split('/')[0]
    netmask = question.split('/')[1]
    
    print('IP Address :', ip)
    total_ip = 2 ** (32 - (int(netmask) + 8))
    print('Total IP :', total_ip)

    netmask = '255.255.' + str(256 - total_ip) + '.0'
    print('Netmask :', netmask)

    ip_network = '.'.join(ip.split('.')[:2]) + '.' + str(total_ip * (int(ip.split('.')[2]) // total_ip)) + '.0'
    ip_broadcast = '.'.join(ip.split('.')[:2]) + '.' + str(total_ip * ((int(ip.split('.')[2]) // total_ip) + 1) - 1) + '.255'
    print('IP Network :', ip_network)
    print('IP Broadcast :', ip_broadcast)
    print('IP Range :', '.'.join(ip_network.split('.')[:3]) + '.1', '-', '.'.join(ip_broadcast.split('.')[:3]) + '.254')

print(subnetting())