import socket
import threading


""""
To start off, we pass in the IP address and port we want the server to lis- ten on
Next, we tell the server to start listening with a maximum back- log of connections 
set to 5
"""
def main(IP_ADDRESS, PORT):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((IP_ADDRESS, PORT))		
	server.listen(5)
	print(f'[*] Listening on {IP_ADDRESS}:{PORT}')

	"""" 
	We then put the server into its main loop, where it waits for an incoming connection
	When a client connects, we receive the client socket in the client variable and the 
	remote connection details in the address variable.
	We then create a new thread object that points to our handle_client function, 
	and we pass it the client socket object as an argument and then we have started 
	to handle the client connection 
	"""

	while True:
		client, address = server.accept()	
		print(f'[*] Accepted connection from {address[0]}:{address[1]}')
		client_handler = threading.Thread(target=handle_client, args=(client,))
		client_handler.start()
"""
The handle_client function performs the recv() and then sends a simple message back 
to the client.
"""
def handle_client(client_socket):
	with client_socket as sock:
		request = sock.recv(1024)
		print(f'[*] Received: {request.decode("utf-8")}')
		sock.send(b'ACK')

if __name__ == '__main__':
    main('0.0.0.0', 9998)