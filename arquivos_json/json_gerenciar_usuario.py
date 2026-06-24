import json
from pathlib import Path

ARQUIVO_JSON = Path(__file__).parent.parent / "logins_criados.json"

DESCONECTAR = "desconectar"


def encontrar_logins():

    if not ARQUIVO_JSON.exists():
        return {}
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as usuarios:
            return json.load(usuarios)
    except json.JSONDecodeError:
        return {}


def salvar_logins(logins_salvos):

    with open(ARQUIVO_JSON, "w", encoding="utf-8") as usuarios:
        json.dump(logins_salvos, usuarios, indent=4, ensure_ascii=False)


def excluir_conta(usuario_atual):
    logins_salvos = encontrar_logins()

    if usuario_atual in logins_salvos:
        logins_salvos.pop(usuario_atual, None)
        salvar_logins(logins_salvos)
        print(F"\n A conta {usuario_atual} foi excluida com sucesso.")
        return DESCONECTAR
    else:
        print("Usuario não encontrado.")
        return None


def sair_conta():
    print("Desconectando da conta...")
    return DESCONECTAR
