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

def remover_tarefa(tarefa_id: int) -> bool:
    """Remove uma tarefa específica pelo ID."""
    # 1. Carregamos o pacote inteiro de dados
    dados = carregar_dados()
    
    # 2. Pegamos só a lista de tarefas que está lá dentro
    tarefas_atuais = dados["tarefas"]
    
    # 3. Filtramos a lista (tirando o ID que queremos apagar)
    tarefas_filtradas = [t for t in tarefas_atuais if t["id"] != tarefa_id]
    
    # 4. Verificamos se o tamanho mudou (se não mudou, o ID não existia)
    if len(tarefas_atuais) == len(tarefas_filtradas):
        return False
        
    # 5. Colocamos a lista nova dentro do pacote de dados e salvamos
    dados["tarefas"] = tarefas_filtradas
    salvar_dados(dados)
    
    return True

def limpar_tarefas():
    """Apaga todas as tarefas do arquivo JSON."""
    dados = carregar_dados()
    dados["tarefas"] = [] # Esvazia a lista
    salvar_dados(dados)