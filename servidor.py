from threading import Thread, Semaphore, Lock
import socket
import random
import os, os.path
from pathlib import Path
from time import sleep 
preguntas = open("preguntas.txt", "r", encoding="utf8").readlines()

players={}

#pregunta
class Trivial(Thread): 
    def __init__(self,socket_cliente, user_data,preguntas): 
        Thread.__init__(self)
        self.socket = socket_cliente
        self.user= user_data
        self.email=''
        self.nick = ''
        self.loged = False
        self.preguntas = preguntas  
        self.aciertos = 0
       
    def run(self):
        global turno, jugadores, numJugadores, tiempo, jugadoresOrdenados, cadena, listaPreguntas
        while self.loged == False:

                user = self.socket.recv(1024).decode().split(";")
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
                

        nick = self.nick = self.socket.recv(1024).decode()

        print(nick + " se ha conectado")

        turno.acquire

        numJugadores = numJugadores + 1
        print(numJugadores)

        while numJugadores != 1:
            pass

        print("Comenzamos!!")

        for pregunta in self.preguntas:
                
            self.socket.send(str('P;' + (pregunta[0] + '\n' + pregunta[1] + '\n' + pregunta[2] + '\n' + pregunta[3]+ '\n' + pregunta[4])).encode())
            
            playerR = self.socket.recv(1024).decode()
            if checkAnswer(pregunta[5], playerR):
                self.socket.send('Acierto'.encode())   
                self.aciertos += 1
                print(self.nick + " acerto")
            else:
                self.socket.send('Fallo'.encode())  
                print(self.nick +" fallo")
        
        self.socket.send(str('FT;>>> Puntuación: ' + str(self.aciertos) + ' pts\nEsperando a que acaben el resto de jugadores...').encode())

        listaJugadores.__setitem__(self.email,self.aciertos)

        numJugadores = numJugadores - 1

        if numJugadores == 0:
            mutex.acquire()

            dicc = getDicc()
            mutex.acquire
            for jugador in listaJugadores:
                if(jugador in dicc.keys()):
                    new = int((dicc[jugador]))
                    new += self.aciertos
                    dicc.update({jugador : new})
                else:
                    dicc.__setitem__(self.email,self.aciertos)
            

            file = open("./clasificacion.txt", "w")
            for key, value in dicc.items():
                jugador = str(key) + ";" + str(value)
                file.write(str(jugador) + "\n")
            file.close
                
            mutex.release()

        while numJugadores != 1:
            pass

        sleep(2)

        print('Finalizado ')
        self.socket.send(str('FP;\n>>> Fin de la partida <<<\n').encode())

        turno.release()

        print('Puntuacion ')
        self.socket.send(str('Mostrar toda las puntaciones\n').encode)
        for jugador in listaJugadores:
             self.socket.send(str(self.email,self.aciertos).encode)
       

        self.socket.close()

    
def getDicc():
    with open('clasificacion.txt', 'r') as archivo:
        data = {}
        for linea in archivo:
            key, value = linea.split(';')
            data[key.strip()] = value.strip()

        return data

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
    print("->" + question + "---" + answer)
    if(question == answer+"\n"):
        return True
    else:
        return False

def mostrarPuntos():
    with open('clasificacion.txt', 'r') as archivo:
        for jugador in archivo:
            puntacion += jugador.split('\n')
            preguntas.append(puntacion)


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









if __name__ == "__main__":
    listaPreguntas = getRandoms()
    numJugadores = 0
    listaJugadores = {}
    turno = Semaphore(2)
    mutex = Lock()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost",9004))
    server.listen(1)
    
    print("Iniciando Juego")
    while True:
        socket_cliente, datos_cliente = server.accept()
        jugador = Trivial(socket_cliente, datos_cliente,listaPreguntas)
        jugador.start()
    
