
import requests,sys,termcolor
from termcolor import colored
import os,socket
import time



os.system("clear")

if sys.version_info[0] !=3: 
	print("""
************REQUIRED PYTHON 3.x *************
            This script was written in python3
        	Example: python3 payload-eb.py                                               """)
	time.sleep(5)
	sys.exit(colored("Automatic Shutting down...", "green"))

print(colored('============WELCOME TO BANgLADESH============','green'))
print(colored('               ===============','green'))
print(colored('                  BANgLADESH','green'))
print(colored('                     V1.O', 'green'))
time.sleep(1)
print(colored("\n URL WITHOUT http/https:", "yellow"))
inp=input(colored("Target URL: ", "red"))
time.sleep(0.4)
x=input(colored("\n (1) Get Sources \n (2) Get Response \n (3) Get Cookies (If Available)\n (4) Get IP Address\n (5) Exit Program \n >> ", "cyan"))
if x=="5":
	
	print(colored("                   Shutting down... \n", "red"))
	
	time.sleep(3)
	sys.exit("Done!")
	
if x=="":
	os.system("clear")
	print(colored(f"""
		                
	              
	              
	                               
                   Invalid typed !""", "red"))
	time.sleep(3)
	os.system("clear")
	print(colored("""
	
	                 
	             
	                              
                   Shutting down...""", "red"))
	time.sleep(3)
	sys.exit(colored("Done", "green"))
	
	
	
try:
	def source():
		s=requests.get("http://"+inp)
		sources=open('./LastUrl-Source.txt','w')

		if x=="1":
			s.encoding='ISO-8859-1'
			print(sources.write(str(s.text)))
			print(colored('Successfully Cracked ! \n Check LastUrl-Source.txt ', 'green'))
	source()

	def get():
		gett=requests.get("http://"+inp)
		if x=="2":
			print(colored("Respond code: ", "red"),gett.status_code)
	get()

	def socks():
#	socket.socket()
		host=socket.gethostbyname(inp)
		if x=="4":
			print(colored(f"IP OF ADDRESS: {host} ", "red"))
	socks()

	def cookie():
		k=requests.get("http://"+inp)
		cookied=open('./Cookies.txt', 'w')
		if x=="3":
			k.encoding='ISO-8859-1'
			print(cookied.write(str(k.cookies.get_dict())))
			print(colored("Successfully Cracked Cookies ! \n Check Cookies.txt ", "green"))
		if x=='':
			os.system('clear')
			sys.exit("Shutting down... \n Done!")
	cookie()
except Exception:
	print(colored(f"""The webpage at '{'http://'+inp}'  might be temporarily down or it may have moved permanently to a new web address.

Suggestions:

Make sure you have a data connection
Reload this website later
Check the address you entered""", "red"))
