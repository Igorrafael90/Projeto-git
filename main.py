import os


def cadastrar_aluno():
    print("===== CADASTRAR ALUNO =====")
    matricula = input("Digite a matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    faltas = int(input("Digite a quantidade de faltas: "))
    media = round(((nota1 + nota2 + nota3) / 3), 2)
    dados_aluno = f"Matricula:{matricula};Nome:{nome};Nota1:{nota1};Nota2:{nota2};Nota3:{nota3};Faltas:{faltas};Media:{media}\n"
    with open("alunos.txt", "a") as arquivo:
        arquivo.write(dados_aluno)
    print("Aluno cadastrado com sucesso!\n")
    
def cadastro_disciplina():
    print("===== CADASTRAR DISCIPLINA =====")
    nome_d = input("Digite o nome da disciplina: ")
    nome_p = input("Digite o nome do professor: ")
    carga_h = float(input("Digite uma carga horaria: "))
    ano = int(input("Digite o ano de conclusão da disciplina: "))
    dados_disciplina = f"Disciplina: {nome_d};\nNome do professor: {nome_p};\nCarga horaria necessaria:{carga_h};\nAno de conclusao: {ano} anos;"
    with open("configuração.txt", "a") as arquivo:
        arquivo.write(dados_disciplina)
    print("Disciplina cadastrada com sucesso")

def listar_alunos():
    dados_aluno = None
    while True:
        print("===== LISTAGEM TODOS OS ALUNOS =====")
        with open("alunos.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                notas = []
                dados = linha.strip().split(';')
                dados_aluno = dados

                for dado in dados_aluno:
                    if 'Nota' in dado:
                        valor_nota = float(dado.split(':')[1])
                        notas.append(valor_nota)

                print(
                    f"{dados[0]}\n{dados[1]}\nNota1:{notas[0]}\nNota2:{notas[1]}\nNota:{notas[2]}\n{dados[5]}\n{dados[6]}\n")
        escolha = input("Pressione 0 para voltar ao menu: ")
        if (escolha == "0"):
            break
        else:
            print("Pressione 0 para voltar ao menu: ")


def listar_aluno_por_matricula():
    matricula = input("Digite a matrícula do aluno que deseja listar: ")
    aluno_encontrado = False
    with open("alunos.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(';')
            for dado in dados:
                matricula_dado = dado.split(':')[1]
                if matricula_dado == matricula:
                    notas = [float(dado.split(':')[1])
                             for dado in dados if 'Nota' in dado]
                    print(
                        f"{dados[0]}\n{dados[1]}\nNota1:{notas[0]}\nNota2:{notas[1]}\nNota3:{notas[2]}\n{dados[5]}\n{dados[6]}\n")
                    escolha = input("Pressione 0 para voltar ao menu: ")
                    aluno_encontrado = True
                    if (escolha == "0"):
                        break
                    else:
                        print("Pressione 0 para voltar ao menu: ")
    if not aluno_encontrado:
        print(f"Aluno com matrícula {matricula} não encontrado.")


while True:
    print("="*44)
    print("{:^44}".format("MENU"))
    print("="*44)
    print("{:<2} - {:<29}".format("1", "Cadastrar Aluno"))
    print("{:<2} - {:<29}".format("2", "Alterar Aluno"))
    print("{:<2} - {:<29}".format("3",
          "Buscar Aluno por matrícula (listando todos os dados desse aluno, inclusive a média)"))
    print("{:<2} - {:<29}".format("4", "Relatórios:"))
    print("{:<6} {:<28}".format("4.1", "Listar todos os alunos"))
    print("{:<6} {:<28}".format(
        "4.2", "Listar alunos aprovados (Critério de aprovação média >= 6,0 e frequência >= 75%)"))
    print("{:<6} {:<28}".format(
        "4.3", "Listar alunos reprovados por faltas (frequência < 75%)"))
    print("{:<6} {:<28}".format(
        "4.4", "Listar dados completos do aluno de maior média"))
    print("{:<6} {:<28}".format(
        "4.5", "Listar dados completos do aluno de menor média"))
    print("{:<2} - {:<29}".format("5",
          "Configurações (nome disciplina, professor, carga horaria, ano da disciplina)"))
    print("{:<2} - {:<29}".format("6", "Sair"))
    print("="*44)

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cadastrar_aluno()
    if escolha == "3":
        listar_aluno_por_matricula()
    if escolha == "4":
        listar_alunos()
    if escolha == "5":
        cadastro_disciplina()
    elif escolha == "6":
        break
