import os,socket
def sendFile(fileData,receiver):
	fileName =  os.path.basename(fileData)
	filePath= os.path.abspath(fileName)
	receiver.sendall(fileName.encode('ascii'))

	f = open(fileName,'rb')
	l = f.read(1024)
	while (l):
		receiver.send(l)
		l = f.read(1024)
	f.close()


	print("done")



def isFileTransfer(text):
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


def receiveFile(receiver):
	fileData = receiver.recv(1024)
	fileName = fileData.decode('ascii')

	with open(fileName, 'wb') as f:
		print ('file opened')
		print("$ Receiving...")
		while True:
			try:
				receiver.settimeout(5)
				data =receiver.recv(1024)
			except socket.timeout:
				receiver.settimeout(None)
				break

			f.write(data)
	print("file received")
		

