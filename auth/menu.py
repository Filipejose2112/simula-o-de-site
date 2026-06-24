from support_geral.utility import title, artigos
from auth.login import login
from auth.register import cadastro
from arquivos_json.json_gerenciar_usuario import encontrar_logins
from settings.settings_menu import configuracoes
from user_profile.perfil import perfil
from settings.exit import DESCONECTAR

logins_salvos = encontrar_logins()


def menu_de_entrada():
    menu_de_entrada_opcoes = {
        "0": ("Fechar programa", None),
        "1": ("Fazer login", login),
        "2": ("Fazer cadastro", cadastro)
    }

    while True:
        title("BEM-VINDO AO SISTEMA")
        for numero, (texto, _) in menu_de_entrada_opcoes.items():
            print(f'{numero} - {texto}')
        escolha = input("Escolha uma dessas opções: ").strip()

        if escolha == '0':
            return 'sair'

        opcao_escolhida = menu_de_entrada_opcoes.get(escolha)
        if opcao_escolhida:
            if escolha == "1":

                sucesso_login = opcao_escolhida[1]()

                if sucesso_login:

                    if isinstance(sucesso_login, str):
                        usuario_atual = sucesso_login
                        sexo_atual = encontrar_logins()[usuario_atual]["sexo"]
                        controle_do_menu_principal(usuario_atual, sexo_atual)
                        continue
                    else:
                        print(
                            "Erro de arquitetura: Altere o final do seu login.py para retornar 'login_usuario' em vez de True.")
            else:
                opcao_escolhida[1]()
        else:
            print("Opção inválida.")


def menu_principal(login_usuario, sexo):
    menu_principal_opcoes = {
        "0": ("Voltar", None),
        "1": ("Abrir perfil", perfil),
        "2": ("Abrir configurações", configuracoes)
    }

    while True:
        artigos(sexo)
        title("MENU PRINCIPAL")
        for numero, (texto, _) in menu_principal_opcoes.items():
            print(f'{numero} - {texto}')
        escolha = input("Escolha uma dessas opções: ").strip()
        if escolha == '0':
            return "voltar"
        opcao_escolhida = menu_principal_opcoes.get(escolha)
        if opcao_escolhida:
            if escolha == "1":
                opcao_escolhida[1](login_usuario)
            elif escolha == "2":
                resultado = opcao_escolhida[1](login_usuario, sexo)
                if resultado == DESCONECTAR:
                    return DESCONECTAR
            else:
                opcao_escolhida[1]()
        else:
            print("Opção inválida.")


def controle_do_menu_principal(login_usuario, sexo):
    while True:
        escolha_principal = menu_principal(login_usuario, sexo)
        if escolha_principal in ("voltar", DESCONECTAR):
            print("Desconectando usuário...")
            break


def inciar_todo_sistema():
    while True:
        resultado = menu_de_entrada()
        if resultado == 'sair':
            print("Fechando o programa de vez...")
            break
