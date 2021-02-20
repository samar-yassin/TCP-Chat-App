#!/usr/bin/env python

import socket,_thread,os,time


ip = "0.0.0.0"
port = 4444
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ip,port))
server.listen(5)
print ("$ listening on : %s:%s" %(ip , port))

def sendFile(fileData,client_socket):
	fileName =  os.path.basename(fileData)
	filePath= os.path.abspath(fileName)
	client_socket.sendall(fileName.encode('ascii'))

	f = open(fileName,'rb')
	l = f.read(1024)
	while (l):
		client_socket.send(l)
		l = f.read(1024)
	f.close()


	print("done")



def isFileTransfer(client_socket,text):
	fileName = ""
	found = text.find("send -f ")
	if found != -1 :
		fileName=text[8:]
		fileName = fileName.strip()
		isFile=os.path.isfile(fileName)
		if isFile:
			filePath= os.path.abspath(fileName)
			return fileName
		else :
			print(f"$ WRONG FILE NAME : {fileName}")
			return "notExist"
	else :
		return "notSending"





def receiveFile():
	fileData = client.recv(1024)
	fileName = fileData.decode('ascii')

	with open(fileName, 'wb') as f:
		print ('file opened')
		print("$ Receiving...")
		while True:
			try:
				client.settimeout(5)
				data =client.recv(1024)
			except socket.timeout:
				client.settimeout(None)
				break

			f.write(data)
	print("file received")



def handler(client_socket,ip,port):
	data=''
	message=''
	while data != "exit" :
		data = client_socket.recv(1024)
		data = data.decode('ascii')
		if data =="exit":
			break
		elif(data == "Sending a file"):
			receiveFile()
			message=input("$ ")

		else:
				print ("$ %s:%s : %s" %(ip,port,data))
				message=input("$ ")



		transfer = isFileTransfer(client_socket,message)
		if(transfer=="notExist"):
				message=input("$ ")
				continue

		elif transfer == "notSending" :
				client_socket.send(message.encode('ascii'))
		else :
				print('$ Sending...')
				message="Sending a file"
				client_socket.send(message.encode('ascii'))	
				time.sleep(3)		
				sendFile(transfer,client_socket);



	client_socket.close()
	print("$ CONNECTION CLOSED with : %s:%s" %(ip , port))

while True:
	client,addr = server.accept()
	print ("$ ACCEPTED CONNECTION from : %s:%s" %(addr[0] , addr[1]))
	_thread.start_new_thread(handler ,(client,addr[0],addr[1],))


server.close()
