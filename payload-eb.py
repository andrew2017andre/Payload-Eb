import requests,sys,termcolor
from termcolor import colored
import os

os.system("clear")
print(colored('============WELCOME TO BANgLADESH============','green'))
print(colored('               ===============','green'))
print(colored('                  BANgLADESH','green'))
print(colored('                     V1.O', 'green'))
print(colored("\n URL WITHOUT http/https:", "yellow"))
inp=input(colored("Target URL: ", "red"))
x=input(colored("\n (1) Get Sources:\n (2) Get Response \n (3) Get Cookies (If Available)\n >> ", "cyan"))
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
def cookie():
	k=requests.get("http://"+inp)
	cookied=open('./Cookies.txt', 'w')
	if x=="3":
		k.encoding='ISO-8859-1'
		print(cookied.write(str(k.cookies.get_dict())))
		print(colored("Successfully Cracked Cookies ! \n Check Cookies.txt ", "green"))
	if x=="exit":
		sys.exit(colored("Shutting down...", "red"))
cookie()
