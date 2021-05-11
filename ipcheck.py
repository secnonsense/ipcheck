#!/usr/local/bin/python3

from netaddr import IPNetwork
import argparse
import os.path

def compare_ip(ip,network,nomatch=0,i=0,f=0):
        if IPNetwork(ip) in IPNetwork(network):
            if i==1:
                print(ip)
            else:
                print(f"{ip} matches {network}")
            toggle=1
            if f==1:
                return toggle
        elif nomatch==1 and f==0:
            print(f"No match for {ip}")

def compare_file2(file,file2,count,nomatch,i,f):
    with open(file2, 'r') as network_file:
        match=0
        for my_network in network_file:
            network=str(my_network.strip())
            toggle=compare_ip(file,network,nomatch,i,f)
            if toggle==1:
                match=1
                count+=1
        if match==0 and nomatch==1:
            print(f"No match for {file}")
    return count

def compare_files(file,file2,nomatch=0,i=0,sip=0,f=1):
    count=0
    if sip==0:
        with open(file, 'r') as ip_file:
            for my_ip in ip_file:
                ip=str(my_ip.strip())
                count=compare_file2(ip,file2,count,nomatch,i,f)

    if sip==1:
        count=compare_file2(file,file2,count,nomatch,i,f)

    if i==1:
        print("\n")
    else:
        print(f"\nTotal Matches: {count}\n")    

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nomatch", help="Show IP's that don't have a match", action="store_true")
    parser.add_argument("-i", "--iponly", help="Print only a list of matching IP's/Networks", action="store_true")
    parser.add_argument("source", help="Enter an IP to compare or a file of IPs or networks")
    parser.add_argument("dest", help="Enter a network to compare to, or a file of networks")
    return parser.parse_args()

def test_ip(value):
    try:
        IPNetwork(value)
        return True
    except:
        return False

def test_file(file):
    return os.path.isfile(file)

def determine_output(sip,dip,sfile,dfile,args):
    if sip and dip:
        compare_ip(args.source,args.dest,args.nomatch,args.iponly)
    elif (dfile and sip) or (sfile and dfile):
        compare_files(args.source,args.dest,args.nomatch,args.iponly,sip)
    elif (sfile and dip):
        print("The Destinatin IP will be compared against entries in the source file\n")
        compare_files(args.dest,args.source,args.nomatch,args.iponly,dip)
    else:
        print("Invalid Input. Source and Dest must be a valid IP/Network or File name.")

def main():
    args=parse_args()
    sip,dip=test_ip(args.source),test_ip(args.dest)
    sfile,dfile=test_file(args.source),test_file(args.dest)
    determine_output(sip,dip,sfile,dfile,args)

if __name__ == "__main__":
    main()

