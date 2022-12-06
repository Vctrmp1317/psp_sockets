
import socket, os
from pathlib import Path
from time import sleep
import re

def comprobarEmail(email):
    expresion_regular = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, email)

salir=False
logueado=False
registrado=False

def login():
    global logueado,salir
    email = input('---Login---\nEmail: ')
    password = input('Password: ')

    s.send(('login;' + email + ';' + password).encode())

    respuesta = s.recv(1024).decode()
    print(respuesta)
    if respuesta == 'True':
        print('Logueado con éxito')
        logueado = True
    else:
        print('Email o contraseña incorrecta')

def registro():
    global logueado,salir
    email = input('---Registro---\nEmail: ')
    password = input('Password: ')

   
    if comprobarEmail(email):
        s.send(('register;' + email + ';' + password).encode())
        respuesta = s.recv(1024).decode()
        if respuesta == 'False':
            print('Usuario registrado con exito')
        else:
            print('Email ya existente')
    else: 
        print('Email no valido')
    sleep(2)
        
    os.system('cls')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost',9004))

while not logueado and not salir:
    print(logueado)
    print('---MENU---')
    print('1 - Login')
    print('2 - Registro')
    print('3 -Salir')
    op= input('Introduce una opcion')

    if op == '1':
        login()
    elif  op == '2':
        registro()
    elif  op == '3':
        salir=True
        print('Saliendo...')
        sleep(2)
        os.system('cls')

nickname = input('Introduce tu nickname: >>>')
s.send(nickname.encode())


while not salir:
    enunciado = s.recv(1024).decode().split(';')
    if enunciado[0] == 'P':
        print(enunciado[1])
        respuesta = input("Respuesta >> ")
        s.send(respuesta.encode())
        acierto = s.recv(1024).decode()
        print(acierto)
        sleep(1)
        os.system('cls')
    elif enunciado[0] == 'FT':
        print(enunciado[1])
    elif enunciado[0] == 'FP':
        print(enunciado[1])
        salir = True
        break

puntiacion = s.recv(1024).decode().split(';')

s.close()