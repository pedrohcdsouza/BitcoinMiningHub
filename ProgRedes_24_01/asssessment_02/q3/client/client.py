# @pedrohcdsouza & @matheusluizsoares

import socket

HOST = '192.168.2.245'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))