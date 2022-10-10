import socket
import termcolor


def scan(target, ports):
    print('\n' + 'Starting Scan For ' + str(target))
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ip_address,port):
    try:
        sock = socket.socket()
        sock.connect((ip_address,port))
        print(termcolor.colored(("[+] Port Opened "+str(port)),'green'))
        sock.close()
    except:
        pass


targets = input("[*] Enter Target To Scan: ")
ports = int(input("[*] Enter How many ports you want to scan(use comma to separate ip address): "))
print("Processing..........")


if ',' in targets:
    print(termcolor.colored(("[*] Scaning Multiple Targets..."),'green'))
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(' '),ports)

else:
    scan(targets,ports)











