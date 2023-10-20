from scapy.all import *

# pac = constructed packet
ipAdd = input("Please enter an IP address to check whether the host is up: ")

pac = IP(dst=ipAdd) / ICMP()
re = sr1(pac, timeout=0.5, retry=1, verbose=0)
if re == None:
    print("No response for {}. Host down.".format(pac[IP].dst))
else:
    print(re.summary())
