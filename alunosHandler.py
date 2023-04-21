from menu import *

ARQUIVO_CONFIG = "configuracao.txt"

def cadastrar_aluno(alunos, matriculas):
    nome = input("Digite o nome do aluno: ")
    while True:
        try:
            matricula = int(input("Digite a matricula do aluno: "))
            if matricula in matriculas:
                print("Matricula ja cadastrada.")
            else:
                break
        except ValueError:
            print("Matricula invalida. Digite novamente.")
    matriculas.append(matricula)
    notas_aluno = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Digite a nota {i} de 3: "))
                if nota < 0 or nota > 10:
                    print("Nota invalida. Digite novamente.")
                else:
                    notas_aluno.append(nota)
                    break
            except ValueError:
                print("Nota invalida. Digite novamente.")
    alunos.append({'nome': nome, 'matricula': matricula, 'notas': notas_aluno})
    print("Aluno cadastrado com sucesso.")


def listar_todos(alunos):
    print("==== TODOS ALUNOS ====")
    for aluno in alunos:
        print(aluno['nome'])


def listar_aprovados(alunos):
    print("==== ALUNOS APROVADOS ====")
    for aluno in alunos:
        media = sum(aluno['notas']) / len(aluno['notas'])
        if media >= 7:
            print(aluno['nome'], f"(media: {media:.2f})")


def listar_reprovados_faltas(alunos):
    print("==== ALUNOS REPROVADOS POR FALTAS ====")
    for aluno in alunos:
        if 'faltas' in aluno and aluno['faltas'] > 10:
            print(aluno['nome'])


def aluno_maior_media(alunos):
    maior_media = 0
    aluno_maior_media = None
    for aluno in alunos:
        media = sum(aluno['notas']) / len(aluno['notas'])
        if media > maior_media:
            maior_media = media
            aluno_maior_media = aluno
    return aluno_maior_media
