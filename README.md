# TCP-Chat-App



## usage :
### first you should make them executable
`chmod +x server.py`

`chmod +x client.py`

### then you can run them
##### on server machine

`./server.py`

##### on client machine

1. get your server IP address
    1. go to your server machine and run this command
    
        `ifconfig`
        
    2. copy the IP address
2. change host variable in client.py with your server IP address
        ![](https://i.imgur.com/IWnlM2O.png)
3. run the client script

      `./client.py`


### sending file
`send -f filename`

**you can run any number of client as the server is multithreaded**

## Examples of result:

![alt text](https://i.imgur.com/35WxOwC.png)
![](https://i.imgur.com/hQeBqqh.jpg)

## software requirements
- python3


