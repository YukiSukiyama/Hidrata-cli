import typer
from rich.console import Console
from rich.table import Table

# Importa o "cérebro" que criamos no outro arquivo
import gerenciador 

app = typer.Typer(help="HidraCLI - Seu assistente de autocuidado e hidratação.")
console = Console()

@app.command()
def adicionar(descricao: str):
    """Adiciona uma nova tarefa de autocuidado."""
    tarefa = gerenciador.adicionar_tarefa(descricao)
    console.print(f"[green]✔ Tarefa '{tarefa['descricao']}' adicionada com sucesso![/green]")

@app.command()
def listar():
    """Lista todas as tarefas de autocuidado."""
    tarefas = gerenciador.listar_tarefas()
    
    if not tarefas:
        console.print("[yellow]Nenhuma tarefa registrada ainda. Que tal adicionar 'Beber 500ml de água'?[/yellow]")
        return

    # Cria uma tabela bonita com a biblioteca Rich
    tabela = Table(title="💧 Suas Tarefas de Autocuidado")
    tabela.add_column("ID", style="cyan", justify="center")
    tabela.add_column("Descrição", style="magenta")
    tabela.add_column("Status", justify="center")

    for t in tarefas:
        status = "[green]✅ Concluído[/green]" if t["concluida"] else "[yellow]⏳ Pendente[/yellow]"
        tabela.add_row(str(t["id"]), t["descricao"], status)

    console.print(tabela)

@app.command()
def concluir(tarefa_id: int):
    """Marca uma tarefa como concluída pelo seu ID."""
    sucesso = gerenciador.concluir_tarefa(tarefa_id)
    if sucesso:
        console.print(f"[green]✔ Parabéns! Tarefa {tarefa_id} concluída![/green]")
    else:
        console.print(f"[red]✖ Erro: Tarefa com ID {tarefa_id} não encontrada.[/red]")

if __name__ == "__main__":
    app()