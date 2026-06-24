import json
from pathlib import Path
import requests
import io
from PIL import Image

FOTO = "foto"

GERENCIAMENTO_DE_FOTO = Path(__file__).parent.parent / "Controle_de_fotos.json"


def carregar_dados_foto():
    if GERENCIAMENTO_DE_FOTO.exists():
        with open(GERENCIAMENTO_DE_FOTO, "r", encoding="utf-8") as gerenciar_foto:
            return json.load(gerenciar_foto)
    return {FOTO: ""}


def salvar_foto(dados):
    with open(GERENCIAMENTO_DE_FOTO, "w", encoding="utf-8") as genciar_foto:
        json.dump(dados, genciar_foto, indent=4, ensure_ascii=False)


def ver_foto():
    dados = carregar_dados_foto()
    return dados[FOTO]


def colocar_foto(foto_colocada):
    dados = carregar_dados_foto()

    if foto_colocada in dados[FOTO]:
        print("Você já está usando essa foto.")
        return
    dados[FOTO] = foto_colocada
    salvar_foto(dados)
    print(f"A foto {foto_colocada} foi colocada com sucesso.")


def remover_foto(foto_removida):
    dados = carregar_dados_foto()

    if foto_removida in dados[FOTO]:
        dados[FOTO] = ""
        salvar_foto(dados)
        print("foto removida.")


def alterar_foto(mudar_foto):
    dados = carregar_dados_foto()

    if dados[FOTO] == mudar_foto:
        print("VOcê não pode alterar colocando a mesma foto. Por favor, escolha outra.")
        return
    dados[FOTO] = mudar_foto
    salvar_foto(dados)
    print("Foto foi alterada com sucesso.")


def exibir_foto_atual():
    """Baixa o link salvo no JSON e exibe a imagem na tela"""
    link_foto = ver_foto()

    if not link_foto:
        print("Nenhum link de foto configurado.")
        return

    if not link_foto.startswith(("http://", "https://")):
        print("O caminho salvo não é um link válido da internet.")
        return

    try:
        print("Baixando imagem para exibição...")

        headers = {"User-Agent": "Mozilla/5.0"}
        resposta = requests.get(link_foto, headers=headers, timeout=10)

        if resposta.status_code == 200:

            imagem_bytes = io.BytesIO(resposta.content)
            with Image.open(imagem_bytes) as img:
                img.show()
        else:
            print(
                f"Não foi possível acessar a imagem. Erro do site: {resposta.status_code}")

    except Exception as e:
        print(f"Erro ao tentar baixar ou abrir a imagem: {e}")
