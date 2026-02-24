from models.database import Database
from typing import Self


class Tarefa:
    def __init__(self: Self, titulo_tarefa: str, date_conclusao: str = None) -> None:
        self.titulo_tarefa: str = titulo_tarefa
        self.date_conclusao: str = date_conclusao

    def salvar_tarefa(self: Self) -> None:
        with Database('.data/tarefas.sqlite3') as db:
            query: str = "INSERT INTO tarefas (titulo_tarefas, data_conclusao) VALEUS (?, ?);" 
            params: tuple = (self.titulo_tarefas, self.date_conclusao)
            db.executar(query, params)
            