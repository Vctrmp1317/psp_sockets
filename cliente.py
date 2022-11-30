
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
s.connect('localhost')

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
        print('Saliendo...')
        os.system('cls')
    

# correo = input('Introduce el correo electronico')
# s.send(correo.encode())
# password = input('Introduce la contraseña')
# s.send(password.encode())

# if(s.recv(1024).decode()==True):
#     nick= input('Escribe tu nick de partida')
#     s.send(nick.encode())

