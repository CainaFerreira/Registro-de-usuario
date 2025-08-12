## Importação das Bibliotecas ##
import os, json, csv
limpa_tela = lambda: os.system('cls')
limpa_tela()

from entrada_dados import verificar_json_vazio_por_leitura,garantir_arquivo_json_existe,ler_arquivo_json,escrever_arquivo_json,pega_inteiro_positivo,pega_string_nao_vazia

## Variáveis Globais ## 

nome_arquivo = "usuarios.json"

## menu ##
#========#

def menu():
    print("===== Menu de Opções =====\n")
    print("1. Adicionar usuário")
    print("2. Listar usuários")
    print("3. Buscar usuário")
    print("4. Atualizar usuário")
    print("5. Deletar usuário")
    print("6. Exporta json para csv")
    print("7. Sair")

# Adicionar um novo registro #
#============================#

def adicionar_usuario(dados,id_usuario,nome,idade,cidade):
    novo_usuario = {"ID": id_usuario, "Nome": nome, "Idade": idade, "Cidade": cidade}
    dados.append(novo_usuario)
    escrever_arquivo_json(nome_arquivo,dados)
    print(f"Usuário {nome} adicionado com sucesso com ID {id_usuario}.")

## Listar todos os registros ##
#=============================#

def listar_usuarios(nome_arquivo):
    print("\n=========== Lista de usuários ===========")
    print(f"{'ID': <3} {'Nome': <20} {'Idade': <6} {'Cidade': <30}")
    dados = ler_arquivo_json(nome_arquivo)
    for usuario in dados:
        print(f"{usuario['ID']: <3} {usuario['Nome']: <20} {usuario['Idade']: <6} {usuario['Cidade']: <30}")

## Buscar um usuário pelo ID ##
#=============================#

def buscar_usuario(nome_arquivo,id_usuario):
    try:        
        dados = ler_arquivo_json(nome_arquivo)
        for usuario in dados:
            if usuario["ID"] == id_usuario:
                print(f"ID:{usuario['ID']: <3}  Nome:{usuario['Nome']: <20}  Idade:{usuario['Idade']: <6} Cidade:{usuario['Cidade']: <30}")
                return
        print(f"Usuário com ID {id_usuario} não encontrado.")
    except ValueError:
        print("Erro: Entrada inválida. O ID deve ser um número.")

## Atualizar um usuário pelo ID com validação ##
#==============================================#

def atualizar_usuario(nome_arquivo,id_usuario):
    try:        
        dados = ler_arquivo_json(nome_arquivo)
        for usuario in dados:
            if usuario["ID"] == id_usuario:
                print(f"Nome:{usuario['Nome']: <20}  Idade:{usuario['Idade']: <6} Cidade:{usuario['Cidade']: <30}")
                nome = input("Digite o novo Nome (ou pressione Enter para manter o atual): ").strip()
                nome = nome if nome else usuario["Nome"]
                idade = input("Digite a nova Idade (ou pressione Enter para manter a atual): ").strip()
                if idade: #verifica se a idade não é nula ou vazio
                    idade = int(idade) if idade.isdigit() else usuario["Idade"]
                else:
                    idade = usuario["Idade"]
                cidade = input("Digite a nova Cidade (ou pressione Enter para manter a atual): ").strip()
                cidade = cidade if cidade else usuario["Cidade"]
                usuario.update({"ID": id_usuario,"Nome": nome, "Idade": idade, "Cidade": cidade})
                escrever_arquivo_json(nome_arquivo,dados)
                print(f"Usuário {id_usuario} atualizado com sucesso.")
                return
        print(f"Usuário com ID {id_usuario} não encontrado.")
    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de digitar valores corretos.")

## Deletar um usuário pelo ID ##
#==============================#

def deletar_usuario(nome_arquivo,id_usuario):
    try:
        dados = ler_arquivo_json(nome_arquivo)
        for usuario in dados:
            if int(usuario["ID"]) == id_usuario:
                dados.remove(usuario)
                escrever_arquivo_json(nome_arquivo,dados)
                print(f"Usuário com ID {id_usuario} removido com sucesso.")
                return
        print(f"Usuário com ID {id_usuario} não encontrado.")
    except ValueError:
        print("Erro: Entrada inválida. O ID deve ser um número.")

#Exportar os dados do JSON para um arquivo CSV
def exportar_para_csv(nome_arquivo, nome_csv="usuarios_exportados.csv"):
    dados = ler_arquivo_json(nome_arquivo)
    with open(nome_csv, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        campos = ["ID", "Nome", "Idade", "Cidade"]
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(dados)
    print(f"Dados exportados com sucesso para o arquivo {nome_csv}.")

#======================#
## Programa Principal ##
#======================#

garantir_arquivo_json_existe(nome_arquivo)

while True:
    dados = ler_arquivo_json(nome_arquivo)
    limpa_tela()
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        id_usuario = max([usuario['ID'] for usuario in dados], default=0) + 1
        nome = pega_string_nao_vazia("Digite o Nome: ")
        idade = pega_inteiro_positivo("Digite a Idade: ")
        cidade = pega_string_nao_vazia("Digite a Cidade: ")
        adicionar_usuario(dados,id_usuario,nome,idade,cidade)
        input("<enter> para continuar...")
    elif opcao == "2":
        if not verificar_json_vazio_por_leitura(dados): 
            listar_usuarios(nome_arquivo)
        else:
            print("Arquivo está vazio !")
        input("<enter> para continuar...")
    elif opcao == "3":
        if not verificar_json_vazio_por_leitura(dados):
            id_usuario = pega_inteiro_positivo("Digite o ID do usuário : ")
            buscar_usuario(nome_arquivo,id_usuario)
        else:
            print("Arquivo está vazio !")
        input("<enter> para continuar...")
    elif opcao == "4":
        if not verificar_json_vazio_por_leitura(dados):
            id_usuario = pega_inteiro_positivo("Digite o ID do usuário : ")
            atualizar_usuario(nome_arquivo,id_usuario)
        else:
            print("Arquivo está vazio !")
        input("<enter> para continuar...")
    elif opcao == "5":
        if not verificar_json_vazio_por_leitura(dados):
            id_usuario = pega_inteiro_positivo("Digite o ID do usuário : ")
            deletar_usuario(nome_arquivo,id_usuario)
        else:
            print("Arquivo está vazio !") 
        input("<enter> para continuar...")
    elif opcao == "6":
        if not verificar_json_vazio_por_leitura(dados):
            exportar_para_csv(nome_arquivo, nome_csv="arquivo_exportados.csv")    
        else:
            print("Arquivo está vazio !") 
        input("<enter> para continuar...")
    elif opcao == "7":
        limpa_tela()
        break
    else:
        print("Opção inválida. Tente novamente.")