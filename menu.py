def ler_opcao(mensagem):
    while True:
        try:
            escolha = int(input(mensagem))
        except ValueError:
            print("Escolha inválida, digite novamente.")
        except KeyboardInterrupt:
            print("Nenhuma escolha foi feita, encerrando...")
            return 0
        else:
            return escolha


def exibir_menu(lista_opcoes, titulo_menu):
    print(f"======= {titulo_menu} =======")
    for indice, opcao in enumerate(lista_opcoes, start=1):
        print(f"{indice}. {opcao}")
    print("=============================")


def menu_principal():
    opcoes = ["Opção 1", "Opção 2", "Opção 3", "Configurações", "Sair"]
    exibir_menu(opcoes, "MENU PRINCIPAL")
    escolha = ler_opcao("Digite a opção desejada: ")
    return escolha


def menu_configuracoes():
    opcoes = ["Opção 1", "Opção 2", "Opção 3", "Voltar"]
    exibir_menu(opcoes, "CONFIGURAÇÕES")
    escolha = ler_opcao("Digite a opção desejada: ")
    return escolha


if __name__ == "__main__":
    while True:
        escolha_menu_principal = menu_principal()

        if escolha_menu_principal == 1:
            print("Você escolheu a opção 1.")
        elif escolha_menu_principal == 2:
            print("Você escolheu a opção 2.")
        elif escolha_menu_principal == 3:
            print("Você escolheu a opção 3.")
        elif escolha_menu_principal == 4:
            while True:
                escolha_menu_config = menu_configuracoes()
                if escolha_menu_config == 1:
                    print("Você escolheu a opção 1 de configurações.")
                elif escolha_menu_config == 2:
                    print("Você escolheu a opção 2 de configurações.")
                elif escolha_menu_config == 3:
                    print("Você escolheu a opção 3 de configurações.")
                elif escolha_menu_config == 4:
                    break
                else:
                    print("Escolha inválida, digite novamente.")
        elif escolha_menu_principal == 5:
            print("Encerrando programa...")
            break
        else:
            print("Escolha inválida, digite novamente.")
