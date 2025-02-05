
# Import the socket module to enable networking functionalities
import socket

# Create a TCP socket (SOCK_STREAM) using IPv4 addressing (AF_INET)
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port number
# "127.0.0.1" refers to the localhost (only accessible on this machine)
# 4443 is the port where the server will listen for incoming connections
sc.bind(("127.0.0.1", 4443)) 

# Start listening for incoming connections
# The argument 5 means that up to 5 connection requests can wait in the queue before being refused
sc.listen(5)

# Infinite loop to keep the server running and accept multiple clients
while True:
    print("Server waiting for a connection >>>>>>")
    
    # Accept a new connection when a client tries to connect
    # cs (client socket) is used to communicate with the client
    # add (address) contains the client's IP and port
    cs, add = sc.accept()
    print("Client connected :) ", add)

    # Loop to continuously receive and send messages to the connected client
    while True:
        # Receive data from the client (maximum 1024 bytes at a time)
        data = cs.recv(1024)
        
        # If no data is received or the client sends 'END', break the loop
        if not data or data.decode('utf-8') == 'END':
            break
        
        # Print the received message after decoding it from bytes to a string
        print("Data received: %s" % data.decode("utf-8"))

        try:
            # Send a response message back to the client
            cs.send(bytes("Hey client", 'utf-8'))
        except:
            # Handle any exceptions (e.g., client disconnecting abruptly)
            print("Exited by the user")

    # Close the client connection when communication ends
    cs.close()

# Close the server socket (this line will only be reached if the server loop exits)
sc.close()
