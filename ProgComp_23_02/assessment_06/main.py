import sys, os, mylib

# Limpando a tela do terminal
os.system('cls')

# Dicionário que irá armazenar as cartelas
dictCartelas = dict()

while True:
    # Exibindo as opções
    print('1 - Gerar Cartelas')
    print('2 - Salvar Cartelas em Arquivo')
    print('3 - Ler Arquivo de Cartelas')
    print('4 - Imprimir Cartela')
    print('0 - Sair do Programa')

    # Solicitando ao usuário a opção desejada
    try:
        opcao = int(input('Escolha a Opção: '))
    except ValueError:
        print('ERRO: Valor Informado não é um Inteiro...\n\n')
        continue
    except KeyboardInterrupt:
        print('\nAVISO: Foi Pressionado CTRL+C... Abortando o Programa\n\n')
        sys.exit()
    except:
        print(f'ERRO: {sys.exc_info()[0]}\n\n')
        continue
    else:
        # Testando a opção digitada pelo usuário
        if opcao == 0:
            print('Saindo do Programa...\n\n')
            sys.exit()
        elif opcao < 0 or opcao > 4:
            print('Opcão Inválida...\n\n')
        elif opcao == 1:
            print(mylib.escolherOPCAO(opcao, dictCartelas))
            break
        #     ...
        # elif opcao == 2:
        #     #Implementar a questão 02 do roteiro
        #     ...
        # elif opcao == 3:
        #     #Implementar a questão 03 do roteiro
        #     ...
        # elif opcao == 4:
        #     #Implementar a questão 04 do roteiro
        #     ...