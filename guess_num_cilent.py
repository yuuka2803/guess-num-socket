from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print('Welcome to the number guessing game')
print('Please input a 4-digit number:0000-9999')
while True:
    sentence = input('Input number:')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024).decode()
    if sentence.startswith('000'):
        clientSocket.close()
        break
    if modifiedSentence.startswith('200'):
        print('Congratulations! You have guessed the number')
        clientSocket.close()
        break
    else:
        if  modifiedSentence.startswith('400'):
            print('Please input a 4-digit number:0000-9999')
        else :
            if modifiedSentence.startswith('401'):
                clientSocket.send("index".encode())
                detailSentence = clientSocket.recv(1024).decode()
                print('Number of correct digits: %s'%detailSentence)
clientSocket.close()