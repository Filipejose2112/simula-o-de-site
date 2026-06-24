import json
from pathlib import Path

AMIGOS = "amigos"
BLOQUEADOS = "bloqueados"

GERENCIANDO_AMIGOS_JSON = Path(
    __file__).parent.parent / "controle_de_amigos.json"


def carregar_dados():
    if GERENCIANDO_AMIGOS_JSON.exists():
        with open(GERENCIANDO_AMIGOS_JSON, "r", encoding="utf-8") as controlar_amigos:
            try:
                return json.load(controlar_amigos)
            except json.JSONDecodeError:
                return {}
    return {}


def salvamento_de_informacoes(dados):
    with open(GERENCIANDO_AMIGOS_JSON, "w", encoding="utf-8") as controlar_amigos:
        json.dump(dados, controlar_amigos, indent=4, ensure_ascii=False)


def dados_de_usuario(dados, usuario_logado):
    if usuario_logado not in dados:
        dados[usuario_logado] = {AMIGOS: [], BLOQUEADOS: []}
    return dados[usuario_logado]


def ver_amigos(usuario_logado):
    dados = carregar_dados()

    return dados_de_usuario.sort(dados, usuario_logado)[AMIGOS]


def ver_bloqueados(usuario_logado):
    dados = carregar_dados()
    return dados_de_usuario(dados, usuario_logado)[BLOQUEADOS]


def adicionar_amigos(usuario_logado, amigo_adicionado):
    dados = carregar_dados()
    perfil = dados_de_usuario(dados, usuario_logado)
    if amigo_adicionado in perfil[BLOQUEADOS]:
        print(
            f'o usuário {amigo_adicionado} está bloqueado. Desbloqueie ele primeiro.')
        return
    if amigo_adicionado not in perfil[AMIGOS]:
        perfil[AMIGOS].append(amigo_adicionado)
        salvamento_de_informacoes(dados)


def remover_amigos(usuario_logado, amigo_removido):
    dados = carregar_dados()
    perfil = dados_de_usuario(dados, usuario_logado)
    if amigo_removido in perfil[AMIGOS]:
        perfil[AMIGOS].remove(amigo_removido)
        salvamento_de_informacoes(dados)


def bloquear_amigo(usuario_logado, nome):
    dados = carregar_dados()
    perfil = dados_de_usuario(dados, usuario_logado)
    if nome in perfil[AMIGOS]:
        perfil[AMIGOS].remove(nome)
    if nome not in perfil[BLOQUEADOS]:
        perfil[BLOQUEADOS].append(nome)
        salvamento_de_informacoes(dados)


def desbloquear_amigo(usuario_logado, nome):
    dados = carregar_dados()
    perfil = dados_de_usuario(dados, usuario_logado)
    if nome in perfil[BLOQUEADOS]:
        perfil[BLOQUEADOS].remove(nome)
        if nome not in perfil[AMIGOS]:
            perfil[AMIGOS].append(nome)
        salvamento_de_informacoes(dados)
