#!/usr/bin/env python3
import socket,os,sendFilesHandler

host = "192.168.0.0"		#change this with server ip
port = 4444
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
print ("$ connection established with : %s:%s" %(host , port))



message = input("$ ")

while message != "exit" :
	cont = sendFilesHandler.handleFileTransfer(client,message)

	if(cont == "continue"):
		continue

	data = client.recv(1024)
	data = data.decode('ascii')

	sendFilesHandler.isSending(data,host,port,client,"client")

	message = input("$ ")


client.send(message.encode('ascii'))


client.close()
