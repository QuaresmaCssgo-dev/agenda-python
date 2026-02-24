from models.database import Database
<<<<<<< HEAD
from typing import Self, Optional
=======
from typing import Self, Any, Optional
>>>>>>> origin/main
from sqlite3 import Cursor

class Tarefa:
    """
<<<<<<< HEAD
    Classe para representar uma tarefa, com métodos para salvar, obter, excluir, atualizar
    e concluir tarefas em um banco de dados usando a classe `Database`.
    """
    def __init__(self, titulo_tarefa: Optional[str], data_conclusao: Optional[str] = None,
                 id_tarefa: Optional[int] = None, concluida: int = 0) -> None:
        self.titulo_tarefa = titulo_tarefa  # título da tarefa
        self.data_conclusao = data_conclusao  # data prevista de conclusão
        self.id_tarefa = id_tarefa  # id da tarefa no banco
        self.concluida = concluida  # 0 = não concluída, 1 = concluída

    @classmethod
    def id(cls, id: int) -> Self:
        # Busca no banco uma tarefa pelo seu id e retorna objeto Tarefa
        with Database() as db:
            query = 'SELECT titulo_tarefa, data_conclusao, concluida FROM tarefas WHERE id = ?;'
            resultado = db.buscar_tudo(query, (id,))
            [[titulo, data, concluida]] = resultado
        return cls(id_tarefa=id, titulo_tarefa=titulo, data_conclusao=data, concluida=concluida)

    def salvar_tarefa(self) -> None:
        # Insere a tarefa no banco de dados
        with Database() as db:
            query = "INSERT INTO tarefas (titulo_tarefa, data_conclusao, concluida) VALUES (?, ?, ?);"
            params = (self.titulo_tarefa, self.data_conclusao, self.concluida)
=======
        Classe para representar uma tarefa, com métodos para salvar, obter, excluir e atualizar tarefas em um banco de dados usando a classe `Database`.
    """
    def __init__(self: Self, titulo_tarefa: Optional[str], data_conclusao: Optional[str] = None, id_tarefa: Optional[int] = None) -> None:
        self.titulo_tarefa: Optional[str] = titulo_tarefa
        self.data_conclusao: Optional[str] = data_conclusao
        self.id_tarefa: Optional[int] = id_tarefa
    
    # Sem o conceito de sobrecarga
    # Tarefa(titulo_tarefa="Nova tarefa")
    # Tarefa(titulo_tarefa="Outra tarefa", data_conclusao="2026-02-03")
    # Tarefa(id_tarefa=1)

    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao FROM tarefas WHERE id = ?;'
            params: tuple = (id,)
            resultado: list[Any] = db.buscar_tudo(query, params)
            # resultado = [["titulo_tarefa", "data_conclusao"]]

            # Desempacotamento de coleção
            [[titulo, data]] = resultado
            
        return cls(id_tarefa=id, titulo_tarefa=titulo, data_conclusao=data)
    
    # Simulando o conceito de sobrecarga
    # Tarefa('Título da Tarefa')
    # Tarefa('Título da Tarefa', '2026-02-03')
    # Tarefa.id(1)

    def salvar_tarefa(self: Self) -> None:
        with Database() as db:
            query: str = "INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);"
            params: tuple = (self.titulo_tarefa, self.data_conclusao)
>>>>>>> origin/main
            db.executar(query, params)

    @classmethod
    def obter_tarefas(cls) -> list[Self]:
<<<<<<< HEAD
        # Retorna uma lista de todas as tarefas que existem na tabela
        with Database() as db:
            query = 'SELECT titulo_tarefa, data_conclusao, id, concluida FROM tarefas;'
            resultados = db.buscar_tudo(query)
            tarefas = [cls(titulo, data, id, concluida) for titulo, data, id, concluida in resultados]
            return tarefas
        
    def excluir_tarefa(self) -> Cursor:
        # Exclui esta tarefa do banco pelo seu id
        with Database() as db:
            query = 'DELETE FROM tarefas WHERE id = ?;'
            resultado = db.executar(query, (self.id_tarefa,))
            return resultado

    def atualizar_tarefa(self) -> Cursor:
        # Atualiza o título e a data de conclusão no banco para o id desta tarefa
        with Database() as db:
            query = 'UPDATE tarefas SET titulo_tarefa = ?, data_conclusao = ? WHERE id = ?;'
            params = (self.titulo_tarefa, self.data_conclusao, self.id_tarefa)
            resultado = db.executar(query, params)
            return resultado

    def concluir(self) -> None:
        # Marca a tarefa como concluída no banco
        with Database() as db:
            query = 'UPDATE tarefas SET concluida = 1 WHERE id = ?;'
            db.executar(query, (self.id_tarefa,))
            self.concluida = 1
=======
        with Database() as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao, id FROM tarefas;'
            resultados: list[Any] = db.buscar_tudo(query)
            tarefas: list[Self] = [cls(titulo, data, id) for titulo, data, id in resultados]
            return tarefas
        
    def excluir_tarefa(self) -> Cursor:
        with Database() as db:
            query: str = 'DELETE FROM tarefas WHERE id = ?;'
            params: tuple = (self.id_tarefa,)
            resultado: Cursor = db.executar(query, params)
            return resultado
        
    def atualizar_tarefa(self) -> Cursor:
        with Database() as db:
            query: str = 'UPDATE tarefas SET titulo_tarefa = ?, data_conclusao = ? WHERE id = ?;'
            params: tuple = (self.titulo_tarefa, self.data_conclusao, self.id_tarefa)
            resultado: Cursor = db.executar(query, params)
            return resultado
    
>>>>>>> origin/main
