
import socket

s = socket.socket()


# correo = input('Introduce el correo electronico')
# s.send(correo.encode())
# password = input('Introduce la contraseña')
# s.send(password.encode())

# if(s.recv(1024).decode()==True):
#     nick= input('Escribe tu nick de partida')
#     s.send(nick.encode())

nick= input('Escribe tu nick de partida')
s.connect(("localhost", 9003))
s.send(nick.encode())

fin_partida=True
while fin_partida:
    a = 1
    # fin_partida=False


s.close()

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
    
#     print('PREGUNTA '+str(1+contPregun)+'!')
    
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