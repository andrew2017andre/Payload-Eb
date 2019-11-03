


import requests
import socket
import time,os,sys
from termcolor import colored


try:
	os.system("clear")
	print(colored("""


{
                                                             
########                                                     
##      ## *************************************             
#       ##    __Tutorial/Channel__[youtube.com/anonymousbghh]
########                                                     
########                                                     
#       ##    __Repository__[https://github.com/josifkhan/]  
##      ##    __Author_Name__[MD Josif Khan]                 
########_______________}                                     
                                                             
_________                    ________________________________
                                        BANgLADESH           
                                           V1.0 """          
,"""blue"""))
	
	
	
	
	print(colored("[! NOTE:] URL WITHOUT \n htpp:// or https://","green"))
	inpp=input(colored("[Target Site]: ","red"))
	def option():
		time.sleep(0.5)
		print(colored("[1] Get IP Address","yellow"))
		time.sleep(0.5)
		print(colored("[2] Get Source codes","yellow"))
		time.sleep(0.5)
		print(colored("[3] Get Cookies (if available) ","yellow"))
		time.sleep(0.5)
		print(colored("[4] Get Response","blue"))
		time.sleep(0.5)
		print(colored("[0] Exit application","red"))
		time.sleep(0.5)
		inp=input("Choose option:>>")
		if inp is "1":
			so=socket.gethostbyname(inpp)
			print(colored(f"TARGET IP: {so} ","red"))
			if inpp.startswith("http://"):
				print(colored("[!] You cannot use http://  .","yellow"))
				sys.exit()
			if inpp.startswith("https://"):
				print(colored("[!] You cannot use https://  .","yellow"))
				sys.exit()
			sys.exit()
		if inp is "2":
			s=requests.get("http://"+inpp)
			sr=open('./Sources.txt', 'w')
			print(sr.write(str(s.text)))
			sys.exit(colored(f"[+] Web-Sources stored into {inpp}.txt file","green"))
		if inp is "3":
			c=requests.get("http://"+inpp)
			print(c.cookies.get_dict())
			sys.exit()
		elif inp is "4":
			r=requests.get("http://"+inpp)
			print(colored(f"\n [+] The Respond Code Is (:{r.status_code}) .\n","yellow"))
			sys.exit()
		elif inp is "0":
			sys.exit(colored("\n[!] The application shut down.","yellow"))
		elif inp=="clear":
			os.system("clear")
			option()
		else:
			print(colored(f"\n \n[!] '{inp}' Is Invalid Option.","yellow"))
			time.sleep(1)
			print("\n")
			option()
	option()

except Exception:
	sys.exit(colored(f"[°.°] The address 'http://{inpp}' is not connectable OR\n  check your internet connections,\n Thank you.","red"))

except KeyboardInterrupt:
	op=input(colored("\n \n [?] Did you just \ntry to quit application ? Y/n: ","blue"))
	if op is "Y" or op is "y":
		print(colored("[![ Thank you for using 'payload-eb' ]!] ","yellow"))
		time.sleep(0.7)
		print(colored("[!] Server disconnecting...","red"))
		time.sleep(2)
		print(colored("[!] disconnected.","yellow"))
		time.sleep(0.5)
		sys.exit()
	elif op is "N" or op is "n":
		print(colored("\n[°.°] Sorry, you are disconnected already.","red"))
		time.sleep(0.5)
		sys.exit()
	else:
		print(colored(f"[o_o] '{op}' Unkown Option ","red"))
		time.sleep(0.5)
		sys.exit()
	



