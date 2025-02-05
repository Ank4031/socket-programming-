# Import the socket module to enable networking functionalities
import socket

# Create a TCP socket (SOCK_STREAM) using IPv4 addressing (AF_INET)
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at "127.0.0.1" (localhost) on port 12345
c.connect(("127.0.0.1", 12345))

# Initial message to be sent to the server
payl = "hey server"

try:
    # Infinite loop to keep sending and receiving messages
    while True:
        # Send the encoded message to the server
        c.send(payl.encode('utf-8'))
        
        # Receive data from the server (maximum 1024 bytes at a time)
        data1 = c.recv(1024)
        
        # Print the received message after decoding it from bytes to a string
        print("Data received from server: %s" % data1.decode('utf-8'))

        # Ask the user if they want to send more data
        more = input("Want to send more data? (y/n): ")
        
        if more.lower() == 'y':
            # Get the next message input from the user
            payl = input("Enter the text: ")
        else:
            # Exit the loop if the user doesn't want to send more data
            break

# Handle the case where the user interrupts the program (Ctrl+C)
except KeyboardInterrupt:
    print("Exited by user")

# Close the client socket after communication ends
c.close()

