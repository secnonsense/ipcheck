# ipsubnetcheck
Checks to see if the source IP or network is a member of the second IP or network. Requires netaddr module 

Either an individual objects can be entered at the command line or files containing IP/network objects can be used (IPv4). Networks should be entered in cidr notation (example - 1.1.1.0/24). 

Individual IP syntax:

python3 ipsubcheck.py [-n] \<source IP/network> \<dest IP/network\> 

Files syntax -  

python3 ipsubcheck.py [-n] -f \<source file\> \<dest file\>   

Options:  
"-f", "--file" - "Use files as input"  
"-n", "--nomatch" - "Show IP's that don't have a match" 
"-i", "--iponly" - "Only print out a list of matching IP's/networks"  

"source" - Enter an IP to compare or a file with IP's using the -f option  
"dest"  - Enter a network to compare to, or a file of networks using the -f option
