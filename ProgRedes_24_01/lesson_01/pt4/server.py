from serverlib import *

print('SERVER HEARING UDP ...\n')

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.bind((HOST, PORT))

while True:
    response = hearUdp(64, udpSocket)

    userHost = response[1][0]
    client = response[1]

    if validadeHost(userHost) == False:
        msg = (f'Hello {userHost}, please send to us your firstname to continue.')
        sendMenssage(msg, client, udpSocket)
        response = hearUdp(64, udpSocket)
        createHost(response, userHost)
        
    userName = validadeHost(userHost)
    msg = (f'Hello again {userName}, this is a SERVER-FILES. Choose an option:\n1 = Upload archives.\n2 = Download archives.\n3 = List archives\n')
    sendMenssage(msg, client, udpSocket)

    response = hearUdp(64, udpSocket)
    if response[0] == '1':
        print(f'Starting file upload protocol for {userName}:{userHost}')
        msg = (f'000_UPLOAD')
        sendMenssage(msg, client, udpSocket)
        response = hearUdp(64, udpSocket)
        arcName = response[0][0]
        arcSize = response[0][1]
        uploadFile(arcName, arcSize, client, udpSocket)
    elif response[0] == '2':
        print(f'Starting file download protocol for {userName}:{userHost}')
        msg = (f'001_DOWNLOAD')
        sendMenssage(msg, client, udpSocket)
        response = hearUdp(64, udpSocket)
        arcName = response[0]
        downloadFile(arcName, client, udpSocket)
    elif response[0] == '3':
        print(f'Starting file list protocol for {userName}:{userHost}')
        msg = (f'002_LIST')
        sendMenssage(msg, client, udpSocket)
        files = listFile()
        sendMenssage(files, client, udpSocket)
