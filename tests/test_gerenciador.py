import pytest
from src import gerenciador

# Configuração para criar um banco de dados temporário (fake)
# Assim, os testes não bagunçam o seu dados.json real.
@pytest.fixture(autouse=True)
def usar_banco_de_dados_temporario(monkeypatch, tmp_path):
    arquivo_temp = tmp_path / "dados_teste.json"
    monkeypatch.setattr(gerenciador, "ARQUIVO_DADOS", str(arquivo_temp))
    yield

# 1. Caminho Feliz (Testar funcionamento correto)
def test_adicionar_tarefa_caminho_feliz():
    """Testa se uma tarefa é adicionada e salva corretamente."""
    nova_tarefa = gerenciador.adicionar_tarefa("Fazer alongamento")
    
    assert nova_tarefa["descricao"] == "Fazer alongamento"
    assert nova_tarefa["concluida"] is False
    assert nova_tarefa["id"] == 1
    
    # Verifica se a tarefa realmente foi salva lendo o arquivo
    tarefas_salvas = gerenciador.listar_tarefas()
    assert len(tarefas_salvas) == 1

# 2. Entrada Inválida (Testar comportamento indevido)
def test_concluir_tarefa_id_invalido():
    """Testa se o sistema lida bem ao tentar concluir um ID inexistente."""
    # O banco de dados temporário começa vazio, então o ID 99 não existe
    resultado = gerenciador.concluir_tarefa(99)
    
    # Deve retornar False (não encontrou), em vez de dar erro/crash no sistema
    assert resultado is False

# 3. Caso Limite (Variação extrema)
def test_listar_tarefas_arquivo_inexistente():
    """Testa se o sistema consegue listar tarefas mesmo quando o JSON não existe."""
    # Sem adicionar nenhuma tarefa (o arquivo dados.json ainda nem foi criado)
    tarefas = gerenciador.listar_tarefas()
    
    # O sistema deve retornar uma lista vazia graciosamente
    assert isinstance(tarefas, list)
    assert len(tarefas) == 0