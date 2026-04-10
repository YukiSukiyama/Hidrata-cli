import json
import os

ARQUIVO_DADOS = "dados.json"

def carregar_dados():
    """Lê o arquivo JSON. Se não existir, retorna uma estrutura vazia."""
    if not os.path.exists(ARQUIVO_DADOS):
        return {"tarefas": []}
    
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # Se o arquivo estiver corrompido ou vazio, retorna padrão
            return {"tarefas": []}

def salvar_dados(dados):
    """Salva o dicionário de dados no arquivo JSON."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def adicionar_tarefa(descricao: str):
    """Adiciona uma nova tarefa de autocuidado ao JSON."""
    dados = carregar_dados()
    
    # Gera um ID simples baseado na quantidade de itens
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
    """Retorna a lista de tarefas atual."""
    dados = carregar_dados()
    return dados["tarefas"]

def concluir_tarefa(tarefa_id: int):
    """Marca uma tarefa como concluída buscando pelo ID."""
    dados = carregar_dados()
    for tarefa in dados["tarefas"]:
        if tarefa["id"] == tarefa_id:
            tarefa["concluida"] = True
            salvar_dados(dados)
            return True # Retorna True se encontrou e concluiu
    return False # Retorna False se o ID não existir (útil para testes de erro)