import os, time, json, random, base64, threading, re, sys
try: import requests, colorama, cursor; from capmonster_python import HCaptchaTask
except: os.system('pip install -q capmonster-python websocket requests colorama cursor')
import requests, colorama, cursor; from capmonster_python import HCaptchaTask
from colorama import *
from pystyle import *
import hashlib
from os import system

green = {Fore.GREEN}
red = {Fore.RED}
yellow = {Fore.YELLOW}
white = {Fore.WHITE}



isis = """

                    
                    ▓█████▄  ▒█████  ▒██   ██▒   ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
                    ▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
                    ░██   █▌▒██░  ██▒░░  █   ░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
                    ░▓█▄   ▌▒██   ██░ ░ █ █ ▒    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
                    ░▒████▓ ░ ████▓▒░▒██▒ ▒██▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
                     ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
                     ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
                     ░ ░  ░ ░ ░ ░ ▒   ░    ░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
                       ░        ░ ░   ░    ░                  ░ ░      ░ ░      ░  ░
                     ░                                                              

                         ⌜――――――――――――――――――――――――――――――――――――――――――――――――――――⌝
                         ┇      [Discord] https://discord.gg/rjAzwtA5Y9       ┇
                         ┇      [Github]  https://github.com/isisv1           ┇
                         ⌞――――――――――――――――――――――――――――――――――――――――――――――――――――⌟
"""
System.Size(200,40)
Anime.Fade(Center.Center(isis), Colors.rainbow, Colorate.Vertical, interval=0.020, enter=True)


#----- About -----
FullName = input(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] Enter Full Name: ")
Address =  input(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] Enter Home Address: ")
City =     input(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] Enter City: ")
Zipcode =  input(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] Enter Zipcode: ")
State =    input(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] Enter State: ")
Country =  input(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] Enter Country: ")

#----- E-Mails -----
Email = input(f"[{Fore.RED}-] Enter Emails: ")

#----- ISP Information -----
IP =       input(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Enter IP Address: ")
Location = input(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Enter Location: ")
Latitude = input(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Enter Latitude & Longitude:")
ISP =      input(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Enter ISP: ")
Domain =   input(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Enter Domain: ")
NetSpeed = input(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Enter Net Speed: ")
IDD =      input(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Enter IDD: ")

#-----Print -----
print("──────────── About ────────────")
print(FullName + " ")
print(Address + " ")
print(City +" ")
print(Zipcode + " ")
print(State + " ")
print(Country + " ")

#----- E-Mails -----
print("──────────── E-Mails ────────────")
print(Email + " ")

#----- ISP Information -----
print("──────────── ISP Information ────────────")
print(IP + " ")
print(Location + " ")
print(Latitude + " ")
print(ISP + " ")
print(Domain + " ")
print(NetSpeed + " ")
print(IDD + " ")

os.system('pause')