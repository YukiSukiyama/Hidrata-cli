# HidraCLI 💧 - v1.0.0

Um assistente de linha de comando (CLI) elegante e minimalista para te ajudar a lembrar de beber água e praticar o autocuidado durante longas jornadas de estudo ou trabalho.

## 🎯 O Problema (Dor Real)
Profissionais de tecnologia e estudantes passam horas na frente do computador e frequentemente esquecem de hábitos básicos de saúde física e mental. O **HidraCLI** resolve essa dor permitindo o gerenciamento rápido de metas diárias de autocuidado (como hidratação, pausas e alongamentos) sem precisar sair do terminal.

## 📸 Evidência de Funcionamento

<img width="980" height="596" alt="image" src="https://github.com/user-attachments/assets/758c23f6-6640-4707-be70-dc2cdb81ded6" />
<img width="772" height="567" alt="image" src="https://github.com/user-attachments/assets/7d8dc5f6-9d9e-46c8-a0bc-835dde561fbe" />


## 🚀 Tecnologias Utilizadas
* **Python 3** - Linguagem principal do projeto.
* **Typer** - Para a construção da interface de linha de comando (CLI).
* **Rich** - Para a formatação elegante e colorida das tabelas no terminal.
* **Pytest** - Para a criação e execução dos testes automatizados.
* **Ruff** - Para a análise estática (linting) e garantia da qualidade do código.
* **GitHub Actions** - Para a esteira de Integração Contínua (CI).

---

## ⚙️ Passo a Passo (Como Executar)

Siga os comandos abaixo no terminal para rodar o projeto localmente:

**1. Clone o repositório e acesse a pasta:**
```bash 
git clone [https://github.com/SEU-USUARIO/hidra-cli.git](https://github.com/SEU-USUARIO/hidra-cli.git)
cd hidra-cli
````
**2. Crie e ative o ambiente virtual:**
```bash 
python -m venv venv

# Ativação no Windows:
.\venv\Scripts\activate

# Ativação no Linux/Mac:
source venv/bin/activate
````
**3. Instale as dependências:**
```bash 
pip install -r requirements.txt
````
## ⚙️ Passo a Passo (Como Executar)
Com o ambiente ativado, você pode testar as funcionalidades da aplicação utilizando os seguintes comandos:

**Adicionar uma nova tarefa:**
```bash 
python src/main.py adicionar "Beber 500ml de água"
python src/main.py adicionar "Alongar o pescoço e os pulsos"
````
**Listar todas as tarefas (Gera a tabela interativa):**
```bash 
python src/main.py listar
````
**Concluir uma tarefa (Substitua o '1' pelo ID desejado):**
```bash 
python src/main.py concluir 1
````
**Remover uma tarefa (Substitua o '2' pelo ID desejado):**
```bash 
python src/main.py remover 2
````
**Limpar TODAS as tarefas da lista:**
```bash 
python src/main.py limpar
````
## 🧪 Validando a Qualidade (Testes e Linting)
Este projeto cumpre os requisitos de qualidade de software exigidos. Para verificar as validações, rode:
**Para executar a suíte de testes automatizados (Pytest):**
```bash 
python -m pytest tests/
````
**Para executar a análise estática (Ruff):**
```bash 
python -m ruff check .
````
Desenvolvido por Murilo Yuki Sukiyama
