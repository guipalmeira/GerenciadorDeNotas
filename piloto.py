
usuarios = {"prof1" : 123, "prof2": 1234}
notas = []

def acesso():
    while True:
        print("Bem vindo a Sistema de Notas Professor(a)")
        print("Faça seu Login")

        login = input("Login: ")

        if login not in usuarios:
            print("Login não encontrado no sistema.")
            print("Faça seu cadastro")
            novo_login = input("Novo Login: ").strip().lower()

            if novo_login in usuarios:
                print("Usuario ja Cadastrado")
                continue

            try:
                nova_senha = int(input("Nova senha: "))
                usuarios[novo_login] = nova_senha
                print("Professor(a) cadastrado com sucesso")

            except ValueError:
                print("A senha deve ser número.")
                return
        else:
            try:
                senha = int(input("Senha: "))
                if senha == usuarios[login]:
                    print("Acesso permitido")
                    tela_principal()
                else:
                    print("Senha incorreta")
            except ValueError:
                print("A senha deve ser número.")

def tela_principal():
    while True:
            
        print("Bem vindo a Tela Principal")
        print("1 - Cadastrar Nota \n2 - Consultar Notas \n3 - Atualizar Notas \n4 - Remover Notas \n0 - Encerrar Programa")
        
        try:
            opcao = int(input("Qual opção: "))

        except ValueError:
            print("A opção tem que ser um número válido")
            continue
        
        if opcao == 1:
            cadastro_notas()
        elif opcao == 2:
            consultar_notas()
        elif opcao == 3: 
            atualizar_notas()
        elif opcao == 4: 
            remover_notas()
        elif opcao == 0:
            print("Programa encerrado")
            break
        else:
            print("Digite uma opção válida!")

def cadastro_notas():
    print("Bem vindo ao Cadastrado de Notas")
    nome_aluno = input("Nome do Aluno: ").strip().lower()
    try:
        idade_aluno = int(input("Idade do Aluno: "))
    except ValueError:
        print("A idade deve ser um numero inteiro.")
        return
    
    try:
        nota_aluno1 = float(input("Digite a Primeira nota do aluno: "))
        nota_aluno2 = float(input("Digite a Segunda nota do aluno: "))
        nota_aluno3 = float(input("Digite a Terceira nota do aluno: "))
        nota_aluno4 = float(input("Digite a Quarta nota do aluno: "))
        media_final = (nota_aluno1 + nota_aluno2 + nota_aluno3 + nota_aluno4) / 4

    except ValueError:
        print("As notas devem ser somente número e não estar vazias.")
        return

    nota = {
        "nome": nome_aluno,
        "idade": idade_aluno,
        "nota1": nota_aluno1,
        "nota2": nota_aluno2,
        "nota3": nota_aluno3,
        "nota4": nota_aluno4,
        "media": media_final
    }

    notas.append(nota)
    print("Notas cadastradas com Sucesso")

def consultar_notas():
    print("Bem vindo a Consulta de Notas.")
    lista_aluno = input("Digite o nome do Aluno que queira consultar as notas: ")

    encontrado = False

    for i, n in enumerate(notas, start=1):
        if n["nome"].lower() == lista_aluno.lower():
            print(f"""
                Aluno: {n['nome'].title()}
                Idade: {n['idade']}
                Nota 1: {n['nota1']}
                Nota 2: {n['nota2']}
                Nota 3: {n['nota3']}
                Nota 4: {n['nota4']}
                Média: {n['media']:.2f}
                """)

            encontrado = True
        
    if not encontrado:
        print("Nenhum aluno com esse nome encontrados")

def atualizar_notas():
    print("=== Atualizar Notas ===")
    nome_doaluno = input("Digite o nome do aluno que deseja atualizar: ").strip().lower()

    for nota in notas:
        if nota["nome"] == nome_doaluno:
            print("Produto encontrado!")
            try:
                nova_nota1 = int(input("Digite a primeira nota nova: \n"))
                nova_nota2 = int(input("Digite a segunda nota nova: \n"))
                nova_nota3 = int(input("Digite a tericera nota nova: \n"))
                nova_nota4 = int(input("Digite a quarta nota nova: "))

                nota["nota1"] = nova_nota1
                nota["nota2"] = nova_nota2
                nota["nota3"] = nova_nota3
                nota["nota4"] = nova_nota4
                nota["media"] = (nova_nota1 + nova_nota2 + nova_nota3 + nova_nota4) / 4


                print("Produto atualizado com sucesso!")
                return
            except ValueError:
                print("Quantidade e valor precisam ser números válidos!")
                return



def remover_notas():
    print("Bem vindo à Tela de Remoção de Notas")
    aluno_nome = input("Digite o nome do Aluno que deseja remover as notas: ").strip().lower()

    for i, nota in enumerate(notas):
        if nota['nome'] == aluno_nome:
            print(f"Aluno encontrado: {nota['nome'].title()}")
            confirmacao = input("Deseja remover as notas do aluno? (s/n): ").strip().lower()
            if confirmacao == 's':
                del notas[i]
                print(f"Notas do aluno {nota['nome'].title()} removidas com sucesso.")
                return
            else:
                print("Remoção cancelada.")
                return
    print("Aluno não encontrado.")

acesso()







