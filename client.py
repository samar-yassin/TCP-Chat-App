#!/usr/bin/env python3
import socket,os,time

host = "192.168.0.0"		#change this with server ip
port = 4444

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))



def sendFile(fileData,client):
	fileName =  os.path.basename(fileData)
	filePath= os.path.abspath(fileName)
	client.sendall(fileName.encode('ascii'))

	f = open(fileName,'rb')
	l = f.read(1024)
	while (l):
		client.send(l)
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
		






message = input("$ ")

while message != "exit" :
	transfer = isFileTransfer(client,message)
	if(transfer=="notExist"):
				message=input("$ ")
				continue

	elif transfer == "notSending" :
				client.send(message.encode('ascii'))
	else :
				print('$ Sending...')
				message="Sending a file"
				client.send(message.encode('ascii'))	
				time.sleep(3)		
				sendFile(transfer,client);

	data = client.recv(1024)
	data = data.decode('ascii')
	if(data == "Sending a file"):
		receiveFile()
	else:
		print ("$ Server : %s" %data)

	message = input("$ ")


client.send(message.encode('ascii'))


client.close()
