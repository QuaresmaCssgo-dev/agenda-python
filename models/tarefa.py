from models.database import Database
from typing import Optional
from sqlite3 import Cursor


class Tarefa:
    """
    Classe para representar uma tarefa, com métodos para salvar, obter,
    excluir, atualizar e concluir tarefas no banco de dados.
    """

    def __init__(
        self,
        titulo_tarefa: Optional[str],
        data_conclusao: Optional[str] = None,
        id_tarefa: Optional[int] = None,
        concluida: int = 0
    ) -> None:
        self.titulo_tarefa = titulo_tarefa
        self.data_conclusao = data_conclusao
        self.id_tarefa = id_tarefa
        self.concluida = concluida

    @classmethod
    def id(cls, id: int) -> "Tarefa":
        with Database() as db:
            query = '''
                SELECT titulo_tarefa, data_conclusao, concluida
                FROM tarefas
                WHERE id = ?;
            '''
            resultado = db.buscar_tudo(query, (id,))

            if not resultado:
                raise ValueError("Tarefa não encontrada.")

            titulo, data, concluida = resultado[0]

        return cls(titulo, data, id, concluida)

    def salvar_tarefa(self) -> None:
        with Database() as db:
            query = '''
                INSERT INTO tarefas (titulo_tarefa, data_conclusao, concluida)
                VALUES (?, ?, ?);
            '''
            params = (self.titulo_tarefa, self.data_conclusao, self.concluida)
            db.executar(query, params)

    @classmethod
    def obter_tarefas(cls) -> list["Tarefa"]:
        with Database() as db:
            query = '''
                SELECT titulo_tarefa, data_conclusao, id, concluida
                FROM tarefas;
            '''
            resultados = db.buscar_tudo(query)

            tarefas = [
                cls(titulo, data, id, concluida)
                for titulo, data, id, concluida in resultados
            ]

            return tarefas

    def excluir_tarefa(self) -> Cursor:
        with Database() as db:
            query = 'DELETE FROM tarefas WHERE id = ?;'
            return db.executar(query, (self.id_tarefa,))

    def atualizar_tarefa(self) -> Cursor:
        with Database() as db:
            query = '''
                UPDATE tarefas
                SET titulo_tarefa = ?, data_conclusao = ?
                WHERE id = ?;
            '''
            params = (self.titulo_tarefa, self.data_conclusao, self.id_tarefa)
            return db.executar(query, params)

    def concluir(self) -> None:
        with Database() as db:
            query = 'UPDATE tarefas SET concluida = 1 WHERE id = ?;'
            db.executar(query, (self.id_tarefa,))
            self.concluida = 1