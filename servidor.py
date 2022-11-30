from threading import Thread, Semaphore, Lock
import socket
import random
import operator
import os, os.path
from pathlib import Path
from time import sleep 
preguntas = open("preguntas.txt", "r", encoding="utf8").readlines()

players={}

#pregunta
class Trivial(Thread): 
    def __init__(self,socket_cliente, user_data): 
        Thread.__init__(self)
        self.socket = socket_cliente
        self.user= user_data
        self.email=''
        self.nick = ''
       # self.pregunta = pregunta;
        self.loged = False
        # self.preguntas = preguntas  

    def run(self):
        global turno, jugadores, numJugadores, tiempo, jugadoresOrdenados, cadena, listaPreguntas 
       
        init(self)




        #Inicio semafoto
        # semaphore.acquire


        # choice = random.choice(preguntas).split("\n")
        # lista = []
        # for x in choice:
        #     pregunta = x.split(";")
        # for x in pregunta:
        #     lista.append(x)
        #     print(x)
            # self.socket.send(x.encode())
        
        #Fin semaforo
        # semaphore.release
    
    
def init(self):
    while self.loged == False:
            user = self.socket.recv(1024).decode.split(";")

            if(user[0]=='login'):
                if(login(user[1],user[2])):
                    self.socket.send("True".encode())
                    self.email=user[1]
                    self.loged = True
                else:
                    self.socket.send("False".encode())
            elif(user[0]=='register'):
                if (register(user[1],user[2])):
                    self.socket.send("True".encode())
                else:
                    self.socket.send("False".encode())
            else:
                    self.socket.send("False".encode())
            
            self.nick = self.socket.recv(1024).decode

def getPreguntas():
    archivo = open("preguntas.txt","r")
    preguntas = []
    for pregunta in archivo:
        splitted = pregunta.split(';')
        preguntas.append(splitted)
    return preguntas

def getRandoms():
    preguntas = getPreguntas()
    preguntasRandom=[]
    for x in range(0,5):
        pregunta = random.choice(preguntas)
        preguntasRandom.append(pregunta)
        preguntas.remove(pregunta)
    return preguntasRandom

def checkAnswer(question, answer):
    splitted = question.split(';')
    if(splitted[5] == answer):
        return True
    else:
        return False


def login(email, password):
    logueado=False
    usuarios=open('./usuarios.txt','r')
    for usuario in usuarios:
        datos=usuario.split(';')
        if datos[0] == email and datos[1].strip() == password:
            logueado=True

    usuarios.close()
    return logueado

def register(email, password):
    existe=False
    
    if (os.path.isfile('./usuarios.txt') == False):
        file = Path('./usuarios.txt')
        file.touch(exist_ok=True)

    usuarios = open('./usuarios.txt')
    for usuario in usuarios:   
        datos=usuario.split(';') 
        if (datos[0] == email):
            print('El email ya esta siendo utilizado, pruebe con otro')
            existe=True
            usuarios.close()
            sleep(2) 
            break
    
    if existe==False: 
        usuarios = open('./usuarios.txt','a')
        usuarios.write(email+ ';' + password+"\n")
        print('usuario registrado correctamente')
        existe=False
        usuarios.close()
        
    return existe










server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("",9004))
server.listen(1 )



if __name__ == "__main__":
    print("Iniciando Juego")
    socket_cliente, datos_cliente = server.accept()
    jugador = Trivial(socket_cliente, datos_cliente)
    jugador.start()
    
