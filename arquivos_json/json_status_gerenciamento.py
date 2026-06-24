import json
from pathlib import Path

STATUS = "status"

STATUS_GERENCIAMENTO_JSON = Path(__file__).parent.parent / "controle_de_status.json"


def carregar_dados_status():
    if STATUS_GERENCIAMENTO_JSON.exists():
        with open(STATUS_GERENCIAMENTO_JSON, "r", encoding="utf-8") as controlar_status:
            return json.load(controlar_status)
    return {STATUS: ""}


def salvar_status(dados):
    with open(STATUS_GERENCIAMENTO_JSON, "w", encoding="utf-8") as controlar_status:
        json.dump(dados, controlar_status, indent=4, ensure_ascii=False)


def ver_status():
    dados = carregar_dados_status()
    return dados[STATUS]


def criar_um_status(status_adicionado):
    dados = carregar_dados_status()

    if status_adicionado in dados[STATUS]:
        print("Você já está usando esse status atualmente.")
        return

    dados[STATUS] = status_adicionado
    salvar_status(dados)


def apagar_status():
    dados = carregar_dados_status()

    dados[STATUS] = ""
    salvar_status(dados)
