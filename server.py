import socket,_thread

ip = "0.0.0.0"
port = 4444


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((ip,port))

server.listen(5)

print ("$ listening on : %s:%s" %(ip , port))

def handler(client_socket,ip,port):
	data=''
	while data != "exit" :
		data = client_socket.recv(1024)
		data = data.decode('ascii')
		print ("$ %s:%s : %s" %(ip,port,data))
		if data !="exit":
			message=input()
			client_socket.sendall(message.encode('ascii'))
	client_socket.close()
	print("$ CONNECTION CLOSED with : %s:%s" %(addr[0] , addr[1]))

while True:
	client,addr = server.accept()
	print ("$ ACCEPTED CONNECTION from : %s:%s" %(addr[0] , addr[1]))
	_thread.start_new_thread(handler ,(client,addr[0],addr[1],))


server.close()