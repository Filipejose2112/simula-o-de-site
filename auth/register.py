from support_geral.utility import title
from arquivos_json.json_gerenciar_usuario import encontrar_logins, salvar_logins


def pegar_telefone():
    while True:
        print("\nDigite seu número de telefone (com DDD): ")
        numero_telefone = input().strip()
        if numero_telefone.isdigit() and len(numero_telefone) == 11:
            return numero_telefone
        print("Erro: Digite um telefone válido contendo apenas números com 11 dígitos.")


def cadastrar_nome(logins_salvos):
    while True:
        print("\nDigite um nome para ser cadastrado como seu nome de usuário: ")
        print("ou digite 'sair' para voltar à tela anterior ")
        cadastro_usuario_nome = input().strip()

        if cadastro_usuario_nome.lower() == 'sair':
            return None
        if cadastro_usuario_nome == '':
            print("O nome de usuário não pode estar vazio.")
            continue
        if cadastro_usuario_nome in logins_salvos:
            print(
                "Já existe um nome de usuário igual a esse. Por favor, tente outro nome.")
            continue
        return cadastro_usuario_nome


def cadastrar_senha():
    while True:
        print("\nCrie uma senha com no mínimo 6 dígitos.")
        cadastro_senha_usuario = input().strip()
        if len(cadastro_senha_usuario) < 6:
            print(
                "Número de dígitos insuficientes. Crie uma senha com pelo menos 6 dígitos, por favor.")
            continue
        return cadastro_senha_usuario


def informar_sexo():
    while True:
        print("\nInforme seu sexo sendo M para masculino e F feminino: ")
        sexo = input("").upper().strip()
        if sexo in ['M', 'F']:
            return sexo
        print("Por favor, informe M ou F para dizer seu sexo.")


def cadastro():
    title("SEÇÃO DE CADASTRO")

    logins_salvos = encontrar_logins()

    nome = cadastrar_nome(logins_salvos)
    if nome is None:
        return
    numero_telefone = pegar_telefone()
    senha = cadastrar_senha()
    sexo = informar_sexo()

    logins_salvos[nome] = {
        "senha": senha,
        "telefone": numero_telefone,
        "sexo": sexo,
        "duas_etapas": False
    }

    salvar_logins(logins_salvos)
    print("\nCadastro foi realizado com sucesso!")
