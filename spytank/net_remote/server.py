import network
import remoteEvent

ADDRESS = "10.0.0.109"
PORT = 1111

socket = network.newServerSocket()
socket.bind((ADDRESS,PORT))

continuer = True
while continuer:
    socket.listen(10)
    print("en ecoute...")

    thread = network.newThread(socket.accept())
    thread.start()

    lettre = thread.clientsocket.recv(4096)
    lettre = lettre.decode()

    print("lettre recu : ", lettre)
    remoteEvent.commande(lettre)
    
    if lettre =="p":
        continuer = False
