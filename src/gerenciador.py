import json
import os
import urllib.request

ARQUIVO_DADOS = "dados.json"

def carregar_dados():
   
    if not os.path.exists(ARQUIVO_DADOS):
        return {"tarefas": []}
    
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            
            return {"tarefas": []}

def salvar_dados(dados):
    
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def adicionar_tarefa(descricao: str):
   
    dados = carregar_dados()
    
    
    novo_id = len(dados["tarefas"]) + 1
    
    nova_tarefa = {
        "id": novo_id,
        "descricao": descricao,
        "concluida": False
    }
    
    dados["tarefas"].append(nova_tarefa)
    salvar_dados(dados)
    return nova_tarefa

def listar_tarefas():
    
    dados = carregar_dados()
    return dados["tarefas"]

def concluir_tarefa(tarefa_id: int):

    dados = carregar_dados()
    for tarefa in dados["tarefas"]:
        if tarefa["id"] == tarefa_id:
            tarefa["concluida"] = True
            salvar_dados(dados)
            return True 
    return False 

def remover_tarefa(tarefa_id: int) -> bool:

    dados = carregar_dados()
    
   
    tarefas_atuais = dados["tarefas"]
    
   
    tarefas_filtradas = [t for t in tarefas_atuais if t["id"] != tarefa_id]
    
   
    if len(tarefas_atuais) == len(tarefas_filtradas):
        return False
        
   
    dados["tarefas"] = tarefas_filtradas
    salvar_dados(dados)
    
    return True

def limpar_tarefas():
    dados = carregar_dados()
    dados["tarefas"] = [] 
    salvar_dados(dados)


def obter_conselho() -> str:
    url = "https://api.adviceslip.com/advice"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            dados = json.loads(response.read().decode())
            return dados["slip"]["advice"]
    except Exception:
        return "Aproveite a pausa para respirar fundo e beber água!"