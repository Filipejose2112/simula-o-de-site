from settings.privacy import privacidade
from support_geral.utility import title
from settings.exit import menu_saida, DESCONECTAR

opcoes_configuracoes = {
    "0": ("Voltar para o menu principal", None),
    "1": ("Privacidade", privacidade),
    "2": ("Gerenciamento de conta", menu_saida)
    # "3": ("Notificações", None),
    #  "4": ("Ajuda", None)
}


def configuracoes(login_usuario):

    while True:
        title("CONFIGURAÇÕES")

        for numero, (texto, _) in opcoes_configuracoes.items():
            print(f'{numero} - {texto}')

        escolha = input("Escolha uma das opções: ").strip()

        if escolha == '0':
            print("Voltando para o menu principal...")
            break

        opcao_escolhida = opcoes_configuracoes.get(escolha)

        if opcao_escolhida:
            opcao = opcao_escolhida[1]
            if opcao:
                resultado = opcao(login_usuario)
                if resultado == DESCONECTAR:
                    return DESCONECTAR

        else:
            print("Opção inválida.")
