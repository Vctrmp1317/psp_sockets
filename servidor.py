from threading import Thread
import socket
import random
import operator
import os, os.path
from pathlib import Path
from time import sleep 

class Trivial(Thread): 
    def __init__(self,socket_cliente, datos_cliente, preguntas): 
        Thread.__init__(self)
        self.socket = socket_cliente
        self.datos= datos_cliente
        self.email = ''
        self.nombre= ''
        self.logueado = False
        self.aciertos = 0
        self.preguntas = preguntas  

def login(email, password):
    
    logueado=False
    usuarios=open('./usuarios.txt','r')
    for usuario in usuarios:
        datos=usuario.split(';')
        if datos[0] == email and datos[1].strip() == password:
            logueado=True
    usuarios.close()


    return logueado

def registro(email, password):
    existe=False
    
    if (os.path.isfile('./usuarios.txt') == False):
        file = Path('./usuarios.txt')
        file.touch(exist_ok=True)
    
    usuarios = open('./usuarios.txt').readlines()
  
    
    for usuario in usuarios:
        datos=usuario.split(';')
        if datos[0] == email:
            print('El email ya esta siendo utilizado, pruebe con otro')
            existe=True
            usuarios.close()
            sleep(2) 
            break
       

        else:
            usuarios.write(email+ ';' + password)
            print('usuario registrado correctamente')
            existe=False
            usuarios.close()
        
    return existe

print(registro('juanito','1234'))
    
