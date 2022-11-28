import socket

s = socket.socket()
s.connect(("localhost", 9003))

correo = input('Introduce el correo electronico')
s.send(correo.encode())
password = input('Introduce la contraseña')
s.send(password.encode())
if(s.recv(1024).decode()==True):
    nick= input('Escribe tu nick de partida')
    s.send(nick.encode())

fin_partida=True
while fin_partida:
    print ('Partida empezada')
    fin_partida=False


s.close()