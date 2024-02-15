import http.client, colorama
from colorama import Fore

#Questo programma permette di verificare i metodi abilitati su un server.

host = "192.168.50.101"
print("Connessione all'host 192.168.50.101 in corso... ")  #IP target
port = input("Inserisci la porta target: (premere invio per porta 80) ") #richiesta input PORTA target
methods = ('GET', 'POST', 'OPTIONS', 'HEAD', 'TRACE', 'DELETE', 'PATCH', 'PUT')
count = 0
verbs = [i for i in range(len(methods))]

if (port == ''): #se non viene inserita una porta, verrà assegnata di default la porta 80.
	port = 80

try:
	path = input("Quale path vuoi esplorare?\n")
	for i in range(len(methods)):
		connection = http.client.HTTPConnection(host, port) #crea una connessione con l'IP e la PORTA target.
		connection.request(methods[i], path) #/' indica il path
		response = connection.getresponse()
		status = (response.status, response.reason)
		#print(response.reason)	
		#print("Connessione avvenuta con successo\n")

		if status[0] >= 200 and status[0] <= 226:
			data = response._method
			print(Fore.GREEN + "Il metodo " + data + " è abilitato")
			verbs[i] = data
			count += 1
			print(response.status)
			connection.close()
		elif status[0] >= 400:
			data = response._method
			print(Fore.RED + "Il metodo " + data + " non è abilitato")
			print(response.status)
			connection.close()
		elif status[0] >= 300 and status[0] < 400:
			data = response._method
			print(Fore.YELLOW + "Il metodo " + data + " è abilitato, ma verrai reindirizzato su un'altra pagina")
			verbs[i] = data
			count += 1
			print(response.status)
			connection.close()
	i += 1
	actives = [j for j in range(count)]
	i = 0
	for j in range(count):
		actives[j] = verbs[i]
		j += 1
		i += 1
	print(Fore.WHITE + "I metodi abilitati sono: ", actives)
except ConnectionRefusedError:
	print("Connessione fallita")
