import socket
from builtins import range

import schedule
import time

for i in range(10):
# Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port to connect to
    server_address = ('192.168.102.177', 28938)


    # Connect to the server
    client_socket.connect(server_address)

    # Send data to the server
    message = "Halo Server Moonton, Saya mau echo...  "
    client_socket.send(message.encode())

    # Receive and print the server's response
    data = client_socket.recv(1024)
    print("Received from server: {}".format(data.decode()))
    time.sleep(3)

# schedule.every(10).seconds.do(automatic_send())

# while True:
    # automatic_send()


# Close the client socket
client_socket.close()