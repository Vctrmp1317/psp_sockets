from threading import Thread, Semaphore, Lock
import socket
import random
import operator
import os, os.path
from pathlib import Path
from time import sleep 
preguntas = open("preguntas.txt", "r", encoding="utf8").readlines()

players={}

class Trivial(Thread): 
    def __init__(self,socket_cliente, datos_cliente,pregunta): 
        Thread.__init__(self)
        self.socket = socket_cliente
        self.datos= datos_cliente
        self.nick = ''
        self.pregunta = pregunta;
        self.logueado = False
        # self.preguntas = preguntas  

    def run(self):
        self.nick = self.socket.recv(1024).decode()
        print(self.nick,'ha comenzado')
        #Inicio semafoto
        # semaphore.acquire


        choice = random.choice(preguntas).split("\n")
        lista = []
        for x in choice:
            pregunta = x.split(";")
        for x in pregunta:
            lista.append(x)
            print(x)
            # self.socket.send(x.encode())
        
        #Fin semaforo
        # semaphore.release
    
    

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



if __name__ == "__main__":

    turnos=Semaphore(2)
    mutex=Lock()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", 9003))
    server.listen(1)

    while True:
            socket_cliente, datos_cliente = server.accept()
            nom=socket_cliente.recv(1024).decode()

            print("Conectado " +str(datos_cliente))

            choice = random.choice(preguntas).split("\n")
            lista = []
            for x in choice:
                pregunta = x.split(";")
            for x in pregunta:
                lista.append(x)

            hilo = Trivial(socket_cliente, datos_cliente,lista)
            hilo.start()
    
    
