from support_geral.utility import title
from arquivos_json import json_gerenciar_amigos


def menu_adicionar(usuario_logado):
    nome = input("Digite o nome do amigo que deseja adicionar: ").strip()
    if nome:
        json_gerenciar_amigos.adicionar_amigos(usuario_logado, nome)


def menu_remover(usuario_logado):
    nome = input("Digite o nome do amigo que deseja remover: ").strip()
    if nome:
        json_gerenciar_amigos.remover_amigos(usuario_logado, nome)


def menu_bloquear(usuario_logado):
    nome = input("Digite o nome de quem deseja bloquear: ").strip()
    if nome:
        json_gerenciar_amigos.bloquear_amigo(usuario_logado, nome)


def menu_desbloquear(usuario_logado):
    nome = input("Digite o nome de quem deseja desbloquear: ").strip()
    if nome:
        json_gerenciar_amigos.desbloquear_amigo(usuario_logado, nome)


def menu_listar_amigos(usuario_logado):
    amigos = json_gerenciar_amigos.ver_amigos(usuario_logado)
    print("\n--- SEUS AMIGOS ---")
    for amigo in amigos:
        print(f"- {amigo}")


def menu_listar_bloqueados(usuario_logado):
    bloqueados = json_gerenciar_amigos.ver_bloqueados(usuario_logado)
    print("\n--- BLOQUEADOS ---")
    for b in bloqueados:
        print(f"- {b}")


def gerenciar_amigos(usuario_logado):

    opcoes_amigos = {
        "0": ("Voltar para perfil", None),
        "1": ("Procurar amigos", menu_adicionar),
        "2": ("Remover amigo", menu_remover),
        "3": ("Lista de amigos", menu_listar_amigos),
        "4": ("Lista de bloqueados", menu_listar_bloqueados),
        "5": ("Bloquear amigos", menu_bloquear),
        "6": ("Desbloquear amigos", menu_desbloquear)
    }

    while True:
        title("GERENCIAMENTO DE AMIGOS")
        for numero, (texto, _) in opcoes_amigos.items():
            print(f'{numero} - {texto}')
        escolha = input("Escolha uma das opções: ").strip()

        if escolha == '0':
            break

        opcao_escolhida = opcoes_amigos.get(escolha)

        if opcao_escolhida:
            funcao = opcao_escolhida[1]
            if funcao:
                funcao(usuario_logado)
        else:
            print("Opção inválida.")
