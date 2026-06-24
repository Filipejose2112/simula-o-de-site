from user_profile import friends_opcoes
from user_profile import status
from user_profile import foto_perfil
from support_geral.utility import title


opcoes_perfil = {
    "0": ("voltar para menu_principal", None),
    "1": ("Amigos", friends_opcoes.gerenciar_amigos),
    "2": ("Status", status.menu_status),
    "3": ("Foto de perfil", foto_perfil.menu_foto)
}


def perfil(usuario_logado):
    while True:
        title("Perfil")
        for numero, (texto, _) in opcoes_perfil.items():
            print(f'{numero} - {texto}')
        escolha = input("Escolha uma das opções: ").strip()

        if escolha == "0":
            break

        opcao_escolhida = opcoes_perfil.get(escolha)

        if opcao_escolhida and opcao_escolhida[1] is not None:

            opcao_escolhida[1](usuario_logado)

        else:
            print("Opção inválida.")
