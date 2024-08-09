import random
from socket import *
def generate_number():
    num=random.randint(0, 9999)
    x = str(num)
    if num == 0:
        x = '0000'
    elif num<10:
        x = '000'+x
    elif num<100:
        x = '00'+x
    elif num<1000:
        x = '0'+x
    return x

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
connectionSocket, addr = serverSocket.accept()
x = generate_number()
while True:
    sentence = connectionSocket.recv(1024).decode()
    print('Received number:', sentence)
    if(sentence == 'exit'):
        codeStatus = '000  EXIT'
        print('Code status: ',codeStatus)
        connectionSocket.send(codeStatus.encode())
        break
    if (sentence.isdigit == False or len(sentence) != 4):
        codeStatus = '400 BAD REQUEST'
        print('Code status: ',codeStatus)
    else :
        y=[int(i) for i in str(x)]
        z=[int(i) for i in str(sentence)]
        index = ''
        num = 0
        for i in range(4):
            if(y[i] == z[i]):
                num += 1
                index  = '%s%d'%(index, y[i])
            else:
                index  = '%s%s'%(index, '-')
        if (num == 4):
            codeStatus = '200 OK'
            print('Code status: ',codeStatus)
            connectionSocket.send(codeStatus.encode())
            break
        else:
            codeStatus = '401 WRONG NUMBER'
            connectionSocket.send(codeStatus.encode())
            request = connectionSocket.recv(1024).decode()
            detail= '[%s]'%(index)
            print('Code status: ',codeStatus, detail)
            connectionSocket.send(detail.encode())
            continue
    connectionSocket.send(codeStatus.encode())
connectionSocket.close()
serverSocket.close()