import os, csv, socket

baseDir = os.path.abspath(__file__)
baseDir = os.path.dirname(baseDir)
HOST = ''
PORT = 1010

def hearUdp(bytes, udpSocket):
    data, client = udpSocket.recvfrom(bytes)
    return data.decode('utf-8'), client

def sendMenssage(msg, client, udpSocket):
    msg = msg.encode('utf-8')
    udpSocket.sendto(msg, client)

def validadeHost(client_ip):
    with open(baseDir + '\\database.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        host_list = list(csv_reader)
        for data in host_list:
            name, ip_address = data
            if client_ip == ip_address:
                return name
        return False

def createHost(data, client_ip):
    with open(baseDir + '\\database.csv', 'w', encoding='utf-8') as csv_file:
        csv_file.write(f'\n{data[0]},{client_ip}')

def uploadFile(arcName, arcSize, client, udpSocket):
    with open(baseDir + '\\server_files' + f'\\{arcName}', 'wb') as client_file:
        currentSize = 0
        while currentSize < arcSize:
            response = hearUdp(128, udpSocket)
            client_file.write(response[0].encode('utf-8'))
            currentSize += 128
        print(f'Archive {arcName} uploaded on Server by: {client}')
        msg = f'Archive {arcName} uploaded on Server.'
        sendMenssage(msg, client, udpSocket)

def downloadFile(arcName, client, udpSocket):
    filePath = baseDir + '\\server_files' + f'\\{arcName}'
    if not os.path.exists(filePath):
        return False
    else:
        with open(filePath, 'rb') as client_file:
            size = os.path.getsize(filePath)
            currentSize = 0
            while currentSize < size:
                quad = client_file.read(128)
                sendMenssage(quad.decode('utf-8'), client, udpSocket)
                currentSize += len(quad)
            print(f'Archive {arcName} downloaded by: {client}')
            msg = f'Archive {arcName} downloaded.'
            sendMenssage(msg, client, udpSocket)

def listFile():
    filesdir = os.listdir(baseDir + '\\server_files')
    return ', '.join(filesdir)
