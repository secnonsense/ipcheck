# ipcheck
Checks to see if the source IP or network is a member of the second IP or network. Requires netaddr module 

Either individual objects can be entered at the command line or files containing IP/network objects can be used (IPv4). Networks should be entered in cidr notation (example - 1.1.1.0/24). 

Syntax:

python3 ipcheck.py [-n][-i] \<source> \<dest>   

Options:  
"-n", "--nomatch" - "Show IP's that don't have a match"    
"-i", "--iponly" - "Only print out a list of matching IP's/networks"  

"source" - Enter an IP/network or file of IP's/Networks to compare   
"dest"  - Enter an IP/network or file of IP's/Networks to compare to  
