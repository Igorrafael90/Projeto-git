arquivo = open("configuracao.txt", "w")
Alunos = []
matriculas = []
notas = []
medias = []

from modulos import *

while True:
    resp = menu(['Cadastrar aluno', 'Alterar aluno', 'Buscar aluno por matricula', 'Relatorios', 'Configuraçap', 'Sair'])
    if resp == 1:
        nome = input("Digite o nome do aluno: ")
        matricula = int(input("Digite sua matricula"))
        matriculas.append(matricula)
        for i in range(0,3):
            nota = float(input(f"Digite uma nota {i + 1} de 3:"))
            notas.append(nota)
