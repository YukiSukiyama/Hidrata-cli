import pytest
from src import gerenciador

@pytest.fixture(autouse=True)
def usar_banco_de_dados_temporario(monkeypatch, tmp_path):
    arquivo_temp = tmp_path / "dados_teste.json"
    monkeypatch.setattr(gerenciador, "ARQUIVO_DADOS", str(arquivo_temp))
    yield

def test_adicionar_tarefa_caminho_feliz():
    """Testa se uma tarefa é adicionada e salva corretamente."""
    nova_tarefa = gerenciador.adicionar_tarefa("Fazer alongamento")
    
    assert nova_tarefa["descricao"] == "Fazer alongamento"
    assert nova_tarefa["concluida"] is False
    assert nova_tarefa["id"] == 1
    
    
    tarefas_salvas = gerenciador.listar_tarefas()
    assert len(tarefas_salvas) == 1


def test_concluir_tarefa_id_invalido():
    """Testa se o sistema lida bem ao tentar concluir um ID inexistente."""
    
    resultado = gerenciador.concluir_tarefa(99)
    
    
    assert resultado is False


def test_listar_tarefas_arquivo_inexistente():
    """Testa se o sistema consegue listar tarefas mesmo quando o JSON não existe."""
    
    tarefas = gerenciador.listar_tarefas()
    
    assert isinstance(tarefas, list)
    assert len(tarefas) == 0

from src import gerenciador

def test_obter_conselho_integracao():
    conselho = gerenciador.obter_conselho()
    
    assert isinstance(conselho, str)
    assert len(conselho) > 0