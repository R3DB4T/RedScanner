import socket  # Communicate with other machines with TCP/UDP Protocols 
import termcolor  # Print some statements in color :)

print(termcolor.colored("Ⓒ RedScanner Ⓒ", "red"))
def scan(target, ports):
    print(termcolor.colored(f"\n[*] Scanning Target : {str(target)}", "magenta"))
    for port in range(1, ports):
        red_scan(target, port)

def red_scan(ipaddress, port):
    try:
        sock = socket.socket()     # Whenever I need to connect to machine using TCP/UDP, I need socket object to connect to internet (internet communication)
        sock.connect((ipaddress, port))    # connect needs 2 parameters:ipaddress and port
        print(termcolor.colored(f"[+] Port Opened! {str(port)}", "green", attrs=["bold"]))
        sock.close()
    except:
        pass


targets = input("[*] Enter Targets To Scan (split them by ','): ")
ports = int(input("[*] How Many Ports Do You Want REDSCAN To Scan: "))
 
if ',' in targets:
    print(termcolor.colored("[*] Scanning Multiple Targets:", "red", attrs=["bold", "dark", "underline"]))
    for ip_address in targets.split(','):
        scan(ip_address.strip(' '), ports)
else:
    scan(targets, ports)