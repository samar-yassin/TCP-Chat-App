import socket

host = socket.gethostname()
port = 4444

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))


message = input()

while message != "exit" :
	client.send(message.encode('ascii'))
	data = client.recv(1024)
	print ("$ Received : %s" %data.decode('ascii'))
	message = input()


client.send(message.encode('ascii'))


client.close()