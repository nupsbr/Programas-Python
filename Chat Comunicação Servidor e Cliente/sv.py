#execute esse primeiro e o cliente execute como terminal dedicado

import socket  # prove comunicação em 2 portas (servidor e cliente)
import pyttsx3
#--------voz--------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #0 e 1

# "AF_INET" usa pra ip "SOCK_STREAM" comunicação strem entre servidor e cliente
sv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sv.bind(('localhost', 2023))  # porta: 2023

sv.listen()  # ficar online
cliente, end = sv.accept()  # aceitar conexão

terminado = False

while not terminado:
    msg = cliente.recv(1024).decode('utf-8')
    engine.say(msg)
    if msg == 'tt':  # 'tt' termina conversa
        terminado = True
    else:
        print(msg)
    cliente.send(input('Mensagem: ').encode('utf-8'))
    engine.runAndWait() 
cliente.close()
sv.close()
