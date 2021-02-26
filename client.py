#!/usr/bin/env python3
import socket,os,sendFilesHandler

host = "192.168.1.1"		#change this with server ip
port = 4444
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
print ("$ connection established with : %s:%s" %(host , port))


messageBuffer=''
message = input("$ ")

while message != "exit" :
	cont = sendFilesHandler.handleFileTransfer(client,message)

	if(cont != "break"):
		message=input("$ ")
		continue

	while True :
		data = client.recv(1024)
		data = data.decode('ascii')

		cont=sendFilesHandler.isSending(data,host,port,client,"client")

		if cont=="break" :
			break


	message = input("$ ")


client.send(message.encode('ascii'))


client.close()
