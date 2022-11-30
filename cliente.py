
import socket, os
from pathlib import Path
from time import sleep
import re

def comprobarEmail(email):
    expresion_regular = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, email)

def login():
    global salir, logueado, server

    email = input('---Login---\nEmail: ')
    password = input('Password: ')

    server.send(('login;' + email + ';' + password).encode())

    respuesta = server.recv(1024).decode()

    if respuesta == 'True':
        print('Logueado con éxito')
        logueado = True
    else:
        print('Email o contraseña incorrecta')

def registro():
    global salir, registrado, server

    email = input('---Registro---\nEmail: ')
    password = input('Password: ')

   
    if comprobarEmail(email):
        server.send(('registro;' + email + ';' + password).encode())
        respuesta = server.recv(1024).decode()
        if respuesta == 'False':
            print('Usuario registrado con exito')
            registrado=True
        else:
            print('Email ya existente')
    else: 
        print('Email no valido')
    sleep(2)
        
    os.system('cls')

salir=False
logueado=False
s = socket.socket()
s.connect(('localhost',9004))

while not logueado and not salir:

    print('---MENU---')
    print('1 - Login')
    print('2 - Registro')
    print('3 -Salir')
    op= input('Introduce una opcion')

    if op == 1:
        login()
    elif  op == 2:
        registro()
    elif  op == 3:
        salir=True
        print('Saliendo...')
        sleep(2)
        os.system('cls')

nickname = input('Introduce tu nickname: >>>')
s.send(nickname.encode())

# correo = input('Introduce el correo electronico')
# s.send(correo.encode())
# password = input('Introduce la contraseña')
# s.send(password.encode())

# if(s.recv(1024).decode()==True):
#     nick= input('Escribe tu nick de partida')
#     s.send(nick.encode())



# import socket

# s = socket.socket()
# s.connect(("localhost", 9003))
# fin_login=True

# # Un bucle por si se equivoca al introducir los datos o no existe
# while fin_login:
#     correo = input('Introduce el correo electronico')
#     s.send(correo.encode())
#     password = input('Introduce la contraseña')
#     s.send(password.encode())
#     # Un if para comprobar que el usuaio y contraseña son correctos 
#     if(s.recv(1024).decode()==True):
#         fin_login=False
#     else:
#         print('ERROR AL INICIAR SESION... Repita los datos')

# nick= input('Escribe tu nick de partida')
# s.send(nick.encode())

# fin_partida=True
# contPregun=0
# contAciert=0

# print('Esperando a los demas jugadores')
# # Recibe el nick de los demas usuario de la partida
# print(s.recv(1024).decode())
# print ('Empezando partida empezada..')

# while fin_partida:
#     # Contador de las preguntas para no hacer mas de 5
#     contPregun+=1
    
#     print('PREGUNTA '+str(contPregun)+'!')
    
#     # Falta como va ha recibir los datos y como los va a seleccionar
#     op = input ('Elija la respuesta correcta.(a,b,c,d)')
    
#     # El serve enviara la respuesta correcta y se compara con la respuesta del usuario
#     opCorrecta=s.recv(1024).decode()
    
#     if(op==opCorrecta):
#         print('HAS ACERTADO')
#         contAciert+=1
    
#     else:
#         print('HAS FALLADO! La respuesta correcta era '+str(opCorrecta))
    
#     if(contPregun==5):
#         fin_partida=False


# print('JUEGO ACABADO...\n Has acertado '+str(contAciert)+' de '+str(contPregun)+' preguntas')
# s.close()
