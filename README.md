# ipsubnetcheck
Takes a list of IP's and a list of IP Subnets (IPv4) and checks to see if the IP's are in the subnets

Requires netaddr module  

Syntax -  

python3 ipsubcheck.py \<options\> \<source file\> \<dest file\>   

Options:  
"-f", "--file" - "Use files as input"  
"-n", "--nomatch" - "Show IP's that don't have a match"  

"source" - Enter an IP to compare or a file with IP's using the -f option  
"dest"  - Enter a network to compare to, or a file of networks using the -f option
