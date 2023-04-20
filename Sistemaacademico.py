arquivo = open("configuracao.txt", "w")
Alunos = []
matriculas = []
notas = []
medias = []

from modulos import *

resp = 0
while resp != 6:
    resp = menu(['Cadastrar aluno', 'Alterar aluno', 'Buscar aluno por matricula', 'Relatorios', 'Configuraçao', 'Sair'])
    if resp == 1:
        nome = input("Digite o nome do aluno: ")
        matricula = int(input("Digite sua matricula"))
        matriculas.append(matricula)
        for i in range(0,3):
            nota = float(input(f"Digite uma nota {i + 1} de 3:"))
            notas.append(nota)
    if resp == 5:
        resp_config = 0
        while resp_config != 7:
            resp_config = menu_config(['Listar todos alunos', 'Listar todos os alunos', 'Listar alunos aprovados', 'Listar alunos reprovados por faltas','Listar dados completos do aluno de maior media', 'Listar dados completos do aluno de menor media', 'sair'])
            if resp_config == 1:
                print(f"{Alunos}")
    
