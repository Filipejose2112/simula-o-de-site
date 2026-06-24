import random
from arquivos_json.json_gerenciar_usuario import salvar_logins, encontrar_logins
from support_geral.utility import title


def trocar_senha(login_usuario):

    logins_salvos = encontrar_logins()

    while True:
        print("\nEscolha a sua nova senha (ou [V]oltar): ")
        nova_senha = input().strip()

        if nova_senha.upper() == 'V':
            break
        elif len(nova_senha) < 6:
            print("Senha curta demais. Tente novamente.")
            continue

        print("Confirme sua senha: ")
        confirmar_senha = input().strip()
        if confirmar_senha != nova_senha:
            print("Senhas não são iguais. Tente novamente.")
            continue

        logins_salvos[login_usuario]["senha"] = nova_senha
        salvar_logins(logins_salvos)
        print("Sua senha foi alterada com sucesso.")
        break


def gerenciar_duas_etapas(login_usuario):

    title("Sistema de verificação de duas etapas")

    while True:
        logins_salvos = encontrar_logins()
        print("0 - Retornar para privacidade")
        print("1 - Ativar duas etapas")
        print("2 - Desativar duas etapas")

        escolha = input("escolha um das opcões: ").strip()

        if escolha == '0':
            print("voltando pra privacidade. ")
            break

        if escolha == '1':
            logins_salvos[login_usuario]["duas_etapas"] = True
            salvar_logins(logins_salvos)
            print("Verificação de duas etapas foi ativada.")
            break
        elif escolha == '2':
            logins_salvos[login_usuario]["duas_etapas"] = False
            salvar_logins(logins_salvos)
            print("Verificação de duas etapas foi desativada.")
            break
        else:
            print("Opção inválida.")


opcoes_privacidade = {
    "0": ("Retornar para configurações", None),
    "1": ("Alterar senha", trocar_senha),
    "2": ("Verificação de duas etapas", gerenciar_duas_etapas),
    "3": ("Status", None),
    "4": ("Bloquear mensagem de desconhecidos", None)
}


def privacidade(login_usuario):
    while True:
        title("PRIVACIDADE")

        for numero, (texto, _) in opcoes_privacidade.items():
            print(f'{numero} - {texto}')
        escolha = input("Escolha uma das opções: ").strip()
        if escolha == '0':
            break

        opcao_escolhida = opcoes_privacidade.get(escolha)

        if opcao_escolhida:
            if opcao_escolhida[1] is not None:
                opcao_escolhida[1](login_usuario)
            else:
                print(
                    f"\nA opção '{opcao_escolhida[0]}' está em desenvolvimento...")
        else:
            print("Opção inválida.")


def verificar_duas_etapas(login_usuario, logins_salvos):
    if logins_salvos[login_usuario].get("duas_etapas") == True:
        codigo = str(random.randint(100000, 999999))
        print(f"\nCódigo de segurança gerado: {codigo}")
        codigo_digitado = input("Digite o código de verificação: ").strip()
        return codigo_digitado == codigo
    return True
