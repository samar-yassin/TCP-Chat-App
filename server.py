#!/usr/bin/env python3

import socket,_thread,os,sendFilesHandler


ip = "0.0.0.0"
port = 4444
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ip,port))
server.listen(5)
print ("$ listening on : %s:%s" %(ip , port))


def handler(client,ip,port):
	data=''
	while data != "exit" :
		data = client.recv(1024)
		data = data.decode('ascii')

		if data =="exit":
			break
		else :
			sendFilesHandler.isSending(data,ip,port,client,"server")

		message=input("$ ")

		cont = sendFilesHandler.handleFileTransfer(client,message)


	client.close()
	print("$ CONNECTION CLOSED with : %s:%s" %(ip , port))


while True:
	client,addr = server.accept()
	print ("$ ACCEPTED CONNECTION from : %s:%s" %(addr[0] , addr[1]))
	_thread.start_new_thread(handler ,(client,addr[0],addr[1],))


server.close()
