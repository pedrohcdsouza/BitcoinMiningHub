import os, csv
baseDir = os.path.abspath(__file__)
baseDir= os.path.dirname(baseDir)

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

def createHost(name, client_ip):
    with open(baseDir, '\\database.csv', 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow([name, client_ip])

def uploadArc()
            
            





