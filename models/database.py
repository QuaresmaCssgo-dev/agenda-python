from sqlite3 import Connection, connect, Cursor
from types import TracebackType
from typing import Any, Self, Optional, Type

from dotenv import load_dotenv  # Importa a função para ler o .env
import os
import traceback

# Carrega o arquivo .env (se existir) e adiciona ao ambiente do sistema
load_dotenv()

# Pega a variável DATABASE definida no .env ou usa o caminho padrão
DB_PATH = os.getenv("DATABASE", "./data/tarefas.sqlite3")

def init_db(db_name: str = DB_PATH) -> None:
    # Inicializa o banco criando a tabela caso ela ainda não exista
    with connect(db_name) as conn:
        # Cria tabela principal
        conn.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo_tarefa TEXT NOT NULL,
            data_conclusao TEXT
        );
        """)
        # Adiciona coluna concluida se ainda não existir
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(tarefas);")  # pega colunas da tabela
        colunas = [col[1] for col in cursor.fetchall()]
        if "concluida" not in colunas:
            cursor.execute("ALTER TABLE tarefas ADD COLUMN concluida INTEGER DEFAULT 0;")
            conn.commit()

class Database:
    """
    Gerencia conexões e operações SQLite.
    Essa classe permite usar a sintaxe 'with Database() as db:' para abrir,
    usar e fechar automaticamente a conexão sem precisar chamar close() manualmente.
    """

    def __init__(self, db_name: str = DB_PATH) -> None:
        # Abre a conexão com o banco de dados usando o caminho definido em DB_PATH
        self.connection: Connection = connect(db_name)
        # Cria um cursor para executar comandos SQL
        self.cursor: Cursor = self.connection.cursor()

    def executar(self, query: str, params: tuple = ()) -> Cursor:
        # Executa uma query SQL (INSERT, UPDATE, DELETE) e aplica a mudança no banco
        self.cursor.execute(query, params)
        self.connection.commit()  # Salva as mudanças permanentemente no arquivo .sqlite3
        return self.cursor  # Retorna o cursor para quem chamou

    def buscar_tudo(self, query: str, params: tuple = ()) -> list[Any]:
        # Executa uma query SQL (normalmente SELECT) e retorna todos os resultados
        self.cursor.execute(query, params)
        return self.cursor.fetchall()  # Retorna uma lista com todas as linhas encontradas
    
    def close(self) -> None:
        # Fecha a conexão com o banco de dados
        self.connection.close()

    def __enter__(self) -> Self:
        # Esse método é chamado quando começa o bloco 'with'
        return self
    
    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            tb: Optional[TracebackType]) -> None:

        # Se durante o bloco 'with' ocorrer um erro, este bloco captura e mostra
        if exc_type:
            print('Exceção capturada no contexto:')
            print(f'Tipo: {exc_type.__name__}')
            print(f'Mensagem: {exc_value}')
            print('Traceback completo:')
            traceback.print_tb(tb)

        # Fecha a conexão ao sair do bloco 'with'
        self.close()