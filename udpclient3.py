import socket

msgFromClient = "Discovery: Who is out there?\0\n"

bytesToSend = str.encode(msgFromClient)

serverAddressPort = ('255.255.255.255', 30303)

bufferSize = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
UDPClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
UDPClientSocket.bind(('0.0.0.0', 30303))
# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

#msgFromServer = UDPClientSocket.recvfrom(bufferSize)

#msg = "Message from Server {}".format(msgFromServer[0])

#print(msg)