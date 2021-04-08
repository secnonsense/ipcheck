from netaddr import IPNetwork, IPAddress
import sys

if len(sys.argv) < 2:
    print("\nUsage: python3 ipsubnetcheck.py <file with list of IP's> <file with list of subnets to check>\n")
    quit()
else:
    file=sys.argv[1]
    file2=sys.argv[2]

count=0

with open(file, 'r') as ip_file:
        for my_ip in ip_file:
            ip=str(my_ip.strip())
            with open(file2, 'r') as network_file:
                for my_network in network_file:
                    network=str(my_network.strip())
                    if IPAddress(ip) in IPNetwork(network):
                        print(f"IP {ip} matches network {network}")
                        count+=1
print(f"\nTotal matches is {count}\n")
