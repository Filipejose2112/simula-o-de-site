from support_geral.utility import title, artigos
from settings.privacy import verificar_duas_etapas
from arquivos_json.json_gerenciar_usuario import encontrar_logins


def login():
    logins_salvos = encontrar_logins()

    title("SEÇÃO DE LOGIN")

    while True:
        print("Digite seu usuário: ")
        login_usuario = input().strip()

        if login_usuario.lower() == 'sair':
            return False
        if login_usuario == '':
            print("O usuário não pode ser vazio.")
            continue

        if login_usuario not in logins_salvos:
            print("Usuário não cadastrado.")
            continue

        print("\nDigite sua senha: ")
        senha_usuario = input().strip()

        if logins_salvos[login_usuario]["senha"] == senha_usuario:

            if logins_salvos[login_usuario].get("duas_etapas"):
                while True:
                    if verificar_duas_etapas(login_usuario, logins_salvos):
                        break
                    else:
                        print("Código incorreto.")
                        opcao = input(
                            "Tentar novamente? [S/N]: ").strip().upper()
                        if opcao == 'N':
                            return False

            sexo = logins_salvos[login_usuario]["sexo"]
            artigo_uso = artigos(sexo)

            title(
                f"BEM VIND{artigo_uso} AO SITE {login_usuario.upper()}")

            return login_usuario
        else:
            print("Senha incorreta. Retornando ao início...")
            continue
