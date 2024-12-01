#!/usr/bin/python3
import socket
import pyfiglet
from termcolor import colored
banner = colored(pyfiglet.figlet_format("Domain to ip Easyly"), 'blue')
print(banner)
domain = input("Enter Your Domain Name: ")

ip = socket.gethostbyname(domain)

print(ip)