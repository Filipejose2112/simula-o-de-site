from support_geral.utility import title
from arquivos_json.json_gerenciar_usuario import excluir_conta, sair_conta, encontrar_logins, DESCONECTAR
from settings.privacy import verificar_duas_etapas


def executar_menu(titulo, escolhas, usuario_atual=None):
    """Gerenciar os menus a baixo"""
    while True:
        if titulo:
            title(titulo)

        for numero, (texto, _) in escolhas.items():
            print(f'{numero} - {texto}')

        escolha = input("Escolha uma dessas opções: ").strip()

        if escolha == '0':
            return

        opcao_escolhida = escolhas.get(escolha)

        if opcao_escolhida:
            funcao = opcao_escolhida[1]
            if funcao:

                resultado = funcao(
                    usuario_atual) if funcao.__name__ in ["excluir_conta", "menu_excluir_conta", "menu_sair_da_conta"] else funcao()

                if resultado == DESCONECTAR:
                    return DESCONECTAR

        else:
            print("Opção inválida.\n")


def confirmacao_de_senha(usuario_atual):

    logins_salvos = encontrar_logins()

    senha = input("Digite sua senha para confirmar: ").strip()

    return senha == logins_salvos[usuario_atual]["senha"]


def confirmacao_final(usuario_atual):

    if not confirmacao_de_senha(usuario_atual):
        print("Senha incorreta.")
        return False

    logins_salvos = encontrar_logins()
    if not verificar_duas_etapas(usuario_atual, logins_salvos):
        return False

    return True


def menu_excluir_conta(usuario_atual):

    escolhas = {
        "0":  ("Voltar para o menu de saida", None),
        "1": ("Excluir conta", excluir_conta)
    }

    if not confirmacao_final(usuario_atual):
        return

    return executar_menu(None, escolhas, usuario_atual)


def menu_sair_da_conta(usuario_atual):

    escolhas = {
        "0":  ("Voltar para o menu de saida", None),
        "1": ("Sair da conta", sair_conta)
    }

    if not confirmacao_final(usuario_atual):
        return

    return executar_menu(None, escolhas, usuario_atual)


def menu_saida(usuario_atual):

    opcoes_menu_de_saida = {
        "0": ("Retornar para configuração", None),
        "1": ("Sair da conta", menu_sair_da_conta),
        "2": ("Excluir conta", menu_excluir_conta),
        "3": ("Sair do site", exit)
    }
    return executar_menu("MENU DE SAIDA", opcoes_menu_de_saida, usuario_atual)
