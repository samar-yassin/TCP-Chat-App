import sendFiles,socket,time
def handleFileTransfer(client,message):
	transfer = sendFiles.isFileTransfer(message)
	if(transfer=="notExist"):
				message=input("$ ")
				return "continue"

	elif transfer == "notSending" :
				client.send(message.encode('ascii'))
	else :
				print('$ Sending...')
				message="Sending a file"
				client.send(message.encode('ascii'))	
				time.sleep(3)		
				sendFiles.sendFile(transfer,client);

def isSending(data,ip,port,client,src):
	if(data == "Sending a file"):
			sendFiles.receiveFile(client)

	else:
		if(src == "server"):
			print ("$ %s:%s : %s" %(ip,port,data))
		elif(src == "client"):
			print ("$ Server : %s" %data)

