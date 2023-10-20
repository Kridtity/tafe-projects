#!/usr/bin/env python
"""
SYNOPSIS

    TODO helloworld [-h,--help] [-v,--verbose] [--version]

DESCRIPTION

    TODO This describes how to use this script.

EXAMPLES

    TODO: Show some examples of how to use this script.

AUTHOR

    Kridtity Lawang <30082530@tafe.wa.edu.au>

LICENSE

    This script is the exclusive and proprietary property of
    TiO2 Minerals Consultants Pty Ltd. It is only for use and
    distribution within the stated organisation and its
    undertakings.

VERSION

    0.0
"""
# Import modules to be used: sys and scapy
from scapy.all import *
import sys

# Program version
version = 0.0

# Set help message
help_message = """
TiO2 Minerals Consultants Pty Ltd.

Port Scanner {version} Help:
Run this program by running "python port_scanner.py "destination_ips" [optional_flags]"
Accepted IP formats are IPv4 dot notation addresses and domain names, including CIDR notation.

Flags:
Port Scanner {version} includes several flags or switches that can be toggled for use during operation.

[-h,--help]
Displays this help screen

[-v,--verbose]
Set program mode to verbose

[--version]
Print program version

[-c,--closed]
Output closed ports

[-o,--open]
Output open ports

[-f,--filtered]
Output filtered ports

[-e,--error]
Output ports encountering errors

Examples:
    python port_scanner.py "127.0.0.1" -o
    python port_scanner.py "www.google.com/30, 1.1.1.1/24" -v -o -f --version
"""

# Define initial states of switches
help = False
closed_ports = False
open_ports = False
filtered_ports = False
error_ports = False
verbosity = 0

# Set destination ports to be scanned and associated port names
dports = [21, 22, 23, 25, 53, 80, 110, 135, 137, 138, 139, 443, 1433, 1434, 8080]
# Port names currently unused
"""port_names = [
    "FTP",
    "SSH",
    "Telnet",
    "SMTP",
    "DNS",
    "HTTP",
    "POP3",
    "Windows RPC",
    "Windows NetBIOS over TCP",
    "Windows NetBIOS over TCP",
    "Windows NetBIOS over TCP",
    "HTTPS",
    "Microsoft SQL Server",
    "Microsoft SQL Server",
    "HTTP Alternative",
]"""

# Receive program inputs from sys CLI
cmd_input = sys.argv

# Clean IP input and set destination IPs from cmd_input
# Rudimentary check if arg one in cmd input is a quote mark to see if command contains IPs
if sys.argv[1] == '"':
    dips = list(sys.argv[1].replace(" ", "").split(","))
else:
    dips = None

# Change switch states according to cmd_input
if ("?" or "-h" or "--help") in cmd_input:
    help = True
if ("-v" or "--verbose") in cmd_input:
    verbosity = 1
if ("-c" or "--closed") in cmd_input:
    closed_ports = True
if ("-o" or "--open") in cmd_input:
    open_ports = True
if ("-f" or "--filtered") in cmd_input:
    filtered_ports = True
if ("-e" or "--errors") in cmd_input:
    error_ports = True

# Define empty list to hold scan results
open_port_results = []
closed_port_results = []
filtered_port_results = []
errors = []

# Print program version if true
if "--version" in cmd_input:
    print("Version {version}")

# Print help info if true
if help:
    print(help_message)

# Proceed with scan only if IPs list is not empty
if dips != None:
    # Print scanning notification to console
    print("Scanning...")

    # Disable scapy outputs
    if verbosity == 0:
        # Save object sys.stdout to variable as backup
        old_stdout = sys.stdout
        # Replace sys.stdout with nonexistent object to prevent scapy outputs
        sys.stdout = open(os.devnull, "w")

    # Run port scan
    for ip in dips:
        for port in dports:
            pac = IP(dst=ip) / TCP(sport=RandShort(), dport=port, flags="S")
            response = sr1(pac, timeout=1.0, retry=1, verbose=verbosity)
            print(response)

            # Configure outputs for port scan
            # If open port response
            if (response == None) or (response == "None: Filtered"):
                # If verbose, print real-time output
                if verbosity == 1:
                    print(
                        "Port {} for host {} filtered.".format(
                            pac[TCP].dport, pac[IP].dst
                        )
                    )

                # Append port filtered results to filtered_port_results
                filtered_port_results.append(
                    "Port {} for host {} filtered.".format(pac[TCP].dport, pac[IP].dst)
                )

                # Check if firewall/ACL/router block etc.
                if pac.haslayer(ICMP):
                    # If verbose, print real-time output
                    if verbosity == 1:
                        print("Packet likely dropped by firewall/ACL/router etc.")

                    # Append notice into filtered_port_results
                    filtered_port_results.append(
                        "Packet likely dropped by firewall/ACL/router etc."
                    )
            elif response[TCP].flags == "SA":
                # If verbose, print real-time output
                if verbosity == 1:
                    print(
                        "Port {} for host {} open.".format(pac[TCP].dport, pac[IP].dst)
                    )

                # Append port open results to open_port_results
                open_port_results.append(
                    "Port {} for host {} open.".format(pac[TCP].dport, pac[IP].dst)
                )
            elif (response[TCP].flags == "R") or (response[TCP].flags == "RA"):
                # If verbose, print real-time output
                if verbosity == 1:
                    print(
                        "Port {} for host {} closed.".format(
                            pac[TCP].dport, pac[IP].dst
                        )
                    )

                # Append port closed results to closed_port_results
                closed_port_results.append(
                    "Port {} for host {} closed.".format(pac[TCP].dport, pac[IP].dst)
                )
            else:
                # If verbose, print real-time output
                if verbosity == 1:
                    print(
                        "Encountered error for port {} for host {}.".format(
                            pac[TCP].dport, pac[IP].dst
                        )
                    )

                # Append error to errors
                errors.append(
                    "Encountered error for port {} for host {}.".format(
                        pac[TCP].dport, pac[IP].dst
                    )
                )

    # Restore sys.stdout for our own outputs
    if (verbosity == 0) and (sys.stdout != old_stdout):
        sys.stdout = old_stdout

# Print scan results
if closed_ports:
    for result in closed_port_results:
        print(result)
    print()

if open_ports:
    for result in open_port_results:
        print(result)
    print()

if filtered_ports:
    for result in filtered_port_results:
        print(result)
    print()

if error_ports:
    for error in errors:
        print(result)
    print()