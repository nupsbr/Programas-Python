import socket
import pyttsx3
engine = pyttsx3.init()

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(('localhost', 2023))  # mesma porta do sv

terminado = False
print('Digite tt para terminar a conversa')

while not terminado:
    cliente.send(input('Mensagem: ').encode('utf-8'))
    msg = cliente.recv(1024).decode('utf-8')
    engine.say(msg)
    if msg == 'tt':
        terminado = True
    else:
        print(msg)
    engine.runAndWait()        
cliente.close()
