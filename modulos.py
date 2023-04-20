def leropc(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("O usuario digitou um escolha fora dos parametros, volte e escolha um deles")
            continue
        except (KeyboardInterrupt):
            print("O usuario não digitou nenhuma esolha entre os parametros, volte e escolha um deles")
            return 0
        else:
            return n
        
def menu(lista):
    print("=====MENU======")
    c = 1
    for item in lista:
        print(f"{c} > {item}")
        c += 1
    print("===============")
    opc = leropc("Digite sua escolha: ")
    return opc