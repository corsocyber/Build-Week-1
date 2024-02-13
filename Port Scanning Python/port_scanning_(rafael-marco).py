import socket

ip_target = input("Inserire indirizzo IP target: ")
port_range = input("Inserire range di porte da scansionare (es. 78-1203): ")
port_status = {}

low_port = int(port_range.split("-")[0])
high_port = int(port_range.split("-")[1])

def scan_port(ip, port):
    try:
    	   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	   status = s.connect_ex((ip_target, port))
    except:
        print("Errore durante la scansione della porta ", port)
        status = 404
    finally:
        s.close()
    return (status)
   
print("Scansioniamo l'indirizzo IP target",ip_target,"dalla porta", low_port,"alla porta",high_port)

for port in range(low_port,high_port+1):
	status = scan_port(ip_target, port)
	if (status == 0):
		port_status.update({port:"APERTA"})
		print("Porta",port,"- APERTA")
	else:
		port_status.update({port:"CHIUSA"})
		print("Porta",port,"- CHIUSA")
print(port_status)

	
			
		
