arquivo = open("configuracao.txt", "w")
Nomes = []
Enderecos = []
matriculas = []
p = 0

while p  != 4:
    print("=========Menu=========")
    print("1-Cadastrar")
    print("2-Listar")
    print("3-Configurar")
    print("4-sair")
    print("======================")
    p = int(input("Digite sua Escolha:"))

    if p == 1:
        Nome = input("Digite seu nome: ")
        Nomes.append(Nome)
        Endereco = input("Digite o seu curso:")
        Enderecos.append(Endereco)
        matricula = int(input("Digite sua matricula:"))
        matriculas.append(matricula)

    if p == 2:
        print(f"Aluno:{Nomes}")
        print(f"Curso:{Enderecos}")
        print(f"Matricula:{matriculas}")

    if p == 3:
        disciplina = input("Nome da disciplina:")
        gestor = input("Nome do gestor:")
        qda = int(input("Quantidade de alunos no curso:"))
        ch = int(input("Carga horaria necessaria:"))


arquivo.write("=======Cadastro=======")
arquivo.write(f"\nNome:{Nomes[0]}")
arquivo.write(f"\nCurso: {Enderecos[0]}")
arquivo.write(f"\nMatricula: {matriculas[0]}")
arquivo.write("\n=======Lista=======")
arquivo.write(f"\nNomes:{Nomes}")
arquivo.write(f"\nCursos: {Enderecos}")
arquivo.write(f"\nMatriculas: {matriculas}")
arquivo.write("\n=======Config=======")
arquivo.write(f"\nDisciplina:{disciplina}")
arquivo.write(f"\nCoordenador: {gestor}")
arquivo.write(f"\nQuantidade de alunos: {qda}")
arquivo.write(f"\nCarga horaria: {ch}")
arquivo.close()
