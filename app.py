from flask import Flask, render_template, request, redirect, url_for
from models.tarefa import Tarefa
from models.database import init_db

app = Flask(__name__)  # Cria a aplicação Flask

init_db()  # Cria a tabela no banco se ainda não existir

@app.route('/')  # Rota raiz
def home():
    return redirect(url_for('agenda'))  # Redireciona para agenda

@app.route('/agenda', methods=['GET', 'POST'])  # Rota principal de tarefas
def agenda():
    tarefas = None
    
    if request.method == 'POST':  # Verifica se o formulário foi enviado
        titulo_tarefa = request.form['titulo-tarefa']
        data_conclusao = request.form['data-conclusao']
        tarefa = Tarefa(titulo_tarefa, data_conclusao)
        tarefa.salvar_tarefa()  # Salva a nova tarefa no banco

    tarefas = Tarefa.obter_tarefas()  # Busca todas as tarefas
    return render_template('agenda.html', titulo='Nova tarefa', tarefas=tarefas)

@app.route('/delete/<int:idTarefa>')  # Excluir tarefa
def delete(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    tarefa.excluir_tarefa()
    return redirect(url_for('agenda'))

@app.route('/update/<int:idTarefa>', methods = ['GET', 'POST'])  # Editar tarefa
def update(idTarefa):
    if request.method == 'POST':
        titulo = request.form['titulo-tarefa']
        data = request.form['data-conclusao']
        tarefa = Tarefa(titulo, data, idTarefa)
        tarefa.atualizar_tarefa()
        return redirect(url_for('agenda'))

    tarefas = Tarefa.obter_tarefas()
    tarefa_selecionada = Tarefa.id(idTarefa)
    return render_template(
        'agenda.html',
        titulo=f'Editando a tarefa ID: {idTarefa}',
        tarefas=tarefas,
        tarefa_selecionada=tarefa_selecionada
    )

@app.route('/concluir/<int:idTarefa>')  # Concluir tarefa
def concluir(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    tarefa.concluir()
    return redirect(url_for('agenda'))

@app.route('/ola')  # Teste
def ola_mundo():
    return "Olá, Mundo!"

if __name__ == "__main__":
    app.run(debug=True)