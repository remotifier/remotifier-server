import socket
import time
import controller

listensocket = socket.socket()
Port = 8005
maxConnections = 999
IP = socket.gethostbyname(socket.gethostname())
listensocket.bind(('', Port))

control = controller.PcController()

print("Server started at " + IP + " on port " + str(Port))



while True:
    listensocket.listen(maxConnections) 
    (clientsocket, address) = listensocket.accept()
    print("New connection made!!")
    running = True
    while running:

        message = clientsocket.recv(1024).decode()
        print(f"client : {message}")
        control.call(message)
    
        if not (message == ""):
            time.sleep(1)
        else:
            clientsocket.close()
            running = False