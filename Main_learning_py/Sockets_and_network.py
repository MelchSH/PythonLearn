import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("127.0.0.1",55555)) # Established the address and port

s.listen()

while True:
    client, address = s.accept()
    print("Connected to {}".format(address))
    client.send("You are connected!".format.encode("utf-8"))
    client.close()



