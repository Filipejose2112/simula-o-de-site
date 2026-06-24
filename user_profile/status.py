from support_geral.utility import title
from arquivos_json import json_status_gerenciamento


def criar_status():
    status = input("Digite o que você deseja colocar no status: ").strip()
    if not status:
        print("Status não pode ficar vazio.")
        return

    json_status_gerenciamento.criar_um_status(status)
    print("Status criado com sucesso.")


def remover_status():
    json_status_gerenciamento.apagar_status()
    print("Status removido.")


def ver_status():
    status = json_status_gerenciamento.ver_status()

    print("\nSEU STATUS")

    if status:
        print(f'\nSeu status - {status}')
    else:
        print("você não possue um status.")


def menu_status(usuario_logado):

    opcoes_status = {
        "0": ("Voltar para perfil", None),
        "1": ("Criar status", criar_status),
        "2": ("Remover status", remover_status),
        "3": ("Ver status atual", ver_status)
    }

    while True:
        title("Status")
        for numero, (texto, _) in opcoes_status.items():
            print(f'{numero} - {texto}')
        escolha = input("Escolha uma dessas opções: ").strip()

        if escolha == "0":
            break

        opcoes_escolhida = opcoes_status.get(escolha)

        if opcoes_escolhida:
            opcoes_escolhida[1]()

        else:
            print("Opção inválida.")
