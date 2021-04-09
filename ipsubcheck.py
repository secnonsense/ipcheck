from netaddr import IPNetwork, IPAddress
import argparse

def compare_ip(ip,network,nomatch=0,f=0):
    if IPAddress(ip) in IPNetwork(network):
        print(f"IP {ip} matches {network}")
        toggle=1
        if f==1:
            return toggle
    elif nomatch==1 and f==0:
        print(f"No match for {ip}")

def compare_files(file,file2,nomatch=0,f=1):
    count=0
    with open(file, 'r') as ip_file:
            for my_ip in ip_file:
                ip=str(my_ip.strip())
                with open(file2, 'r') as network_file:
                    match=0
                    for my_network in network_file:
                        network=str(my_network.strip())
                        toggle=compare_ip(ip,network,nomatch,f)
                        if toggle==1:
                            match=1
                            count+=1
                    if match==0 and nomatch==1:
                        print(f"No match for {ip}") 
    print(f"\nTotal Matches: {count}\n")    

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Use files as input", action="store_true")
    parser.add_argument("-n", "--nomatch", help="Show IP's that don't have a match", action="store_true")
    parser.add_argument("source", help="Enter an IP to compare or a file with IP's using the -f option")
    parser.add_argument("dest", help="Enter a network to compare to, or a file of networks using the -f option")
    return parser.parse_args()

def main():
    args=parse_args()
    if args.file:
        compare_files(args.source,args.dest,args.nomatch)
    else:
        compare_ip(args.source,args.dest,args.nomatch)

if __name__ == "__main__":
    main()

