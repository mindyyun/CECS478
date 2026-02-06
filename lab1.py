# Mindy Yun
# HW and Lab 1: Review Network

# imports
import socket
from getmac import get_mac_address 

# find and display IP address
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(f"IP Address: {ip}")  

# display MAC address
print(f"MAC Address: {get_mac_address()}")   

# find and display physical address

# tried using ip2geotools, couldn't complete install 
# tried using ipinfo, incorrectly identified location (said Mountain View, CA which is about 300 miles from here)

physical_address = input("Enter address: ")
print(f"Physical Address: {physical_address}")

