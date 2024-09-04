import ssl

def wrapSocket(sock, serverurl):
    purpose = ssl.Purpose.SERVER_AUTH
    context = ssl.create_default_context(purpose)

    # Cliente não validará identidade do servidor
    # Perigoso, mas é a forma de aceitar certificado autoassinados
    # Comentar as duas próximas linhas para casos reais
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    return context.wrap_socket(sock, server_hostname=serverurl)
