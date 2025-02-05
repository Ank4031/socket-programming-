socket programmimg -
Socket programming is how computers talk to each other over a network—whether it’s your home Wi-Fi, a big corporate network, or the internet. It lets two applications send and receive data using different communication methods, like TCP (which ensures data gets delivered properly) or UDP (which is faster but doesn’t guarantee delivery). Basically, it’s the foundation for things like web browsing, online gaming, and chatting apps

socket.AF_INET (Address Family - Internet)
It tells the socket that we’re using IPv4 addresses (like 192.168.1.1).
If you want to use IPv6, you’d use socket.AF_INET6.

socket.SOCK_STREAM (Socket Type - Stream)
It specifies that we’re using TCP (Transmission Control Protocol), which is a connection-oriented protocol.
TCP ensures reliable communication, meaning data is sent in order and without loss.

In this we have create a TCP client and server for the puepose of message passing.
The connection between client and server is terminated when a empty message is send by the client or when 'y' is send by the client to the server
