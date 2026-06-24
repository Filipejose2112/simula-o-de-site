import json
from pathlib import Path
import io
import requests
from PIL import Image
import climage 
from support_geral.utility import title 

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


def colocar_foto(link_foto):
    dados = carregar_dados_foto()
    if dados[FOTO] == link_foto:
        print("\n[!] Você já está usando esse link de foto atualmente.")
        return
        
    dados[FOTO] = link_foto
    salvar_foto(dados)
    print("\n[+] Link da foto adicionado com sucesso!")


def alterar_foto(mudar_foto):
    dados = carregar_dados_foto()
    if dados[FOTO] == mudar_foto:
        print("\n[!] Você não pode alterar colocando o mesmo link. Por favor, escolha outro.")
        return
        
    dados[FOTO] = mudar_foto
    salvar_foto(dados)
    print("\n[+] Foto alterada com sucesso!")


def remover_foto():
    dados = carregar_dados_foto()
    dados[FOTO] = ""
    salvar_foto(dados)
    print("\n[-] Foto removida com sucesso.")


def exibir_foto_no_terminal():
    """Busca o link do JSON e renderiza a imagem dentro do terminal do VS Code"""
    link_foto = ver_foto()
    
    if not link_foto:
        print("\n[!] Nenhuma foto cadastrada para exibir.")
        return

    try:
        print("\nCarregando imagem no terminal... Aguarde...")
        headers = {"User-Agent": "Mozilla/5.0"}
        resposta = requests.get(link_foto, headers=headers, timeout=10)

        if resposta.status_code == 200:
            imagem_bytes = io.BytesIO(resposta.content)
            img = Image.open(imagem_bytes)

     
            largura_terminal = 60 
            proporcao = img.height / img.width
            altura_terminal = int(largura_terminal * proporcao * 0.5) 
            img_redimensionada = img.resize((largura_terminal, altura_terminal))

          
            imagem_no_terminal = climage.convert_pil(img_redimensionada)
            print("\n" + imagem_no_terminal + "\n")
        else:
            print(f"\n[!] Erro ao acessar o link da imagem. Status: {resposta.status_code}")

    except Exception as e:
        print(f"\n[!] Erro ao renderizar imagem: {e}")


def menu_foto(usuario_logado):
    while True:
        title(f"Gerenciar Foto - {usuario_logado}")
        
      
        foto_atual = ver_foto()
        if foto_atual:
            print(f"Link atual: {foto_atual[:50]}...") 
        else:
            print("Status: Sem foto de perfil.")
        
        print("-" * 30)
        print("0 - Voltar ao perfil")
        print("1 - Adicionar/Colocar link de foto")
        print("2 - Alterar link de foto")
        print("3 - Remover foto")
        print("4 - VER FOTO NO TERMINAL")
        print("-" * 30)
        
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == "0":
            break
        elif escolha == "1":
            link = input("Cole o link da foto aqui: ").strip()
            colocar_foto(link)
        elif escolha == "2":
            link = input("Cole o NOVO link da foto aqui: ").strip()
            alterar_foto(link)
        elif escolha == "3":
            remover_foto()
        elif escolha == "4":
            exibir_foto_no_terminal()
        else:
            print("Opção inválida.")