# TCP-Chat-App


## usage :
**WINDOWS** :

**on server machine**

`python3 server.py`

**on client machine**

1. get your server IP address
    1. go to your server machine and open CMD and run this command
    
        `ipconfig`
        
    2. copy the IP address
2. change host variable in client.py with your server IP address
        ![](https://i.imgur.com/IWnlM2O.png)
3. run the client script

      `python3 client.py`


**LINUX**:

1. make them executable
`chmod +x server.py`

`chmod +x client.py`

2. run them
**on server machine**

`./server.py`

**on client machine**

1. get your server IP address
    1. go to your server machine and open your terminal and run this command
    
        `ifconfig`
        
    2. copy the IP address
2. change host variable in client.py with your server IP address
        ![](https://i.imgur.com/IWnlM2O.png)
3. run the client script

      `./client.py`

**you can run any number of client as the server is multithreaded**


## Features :
- **sending file**

`send -f filename`


## Examples of result:

![alt text](https://i.imgur.com/35WxOwC.png)
![](https://i.imgur.com/hQeBqqh.jpg)

## software requirements
- python3


