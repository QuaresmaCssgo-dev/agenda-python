from sqlite3 import Connection, connect, Cursor
from types import TracebackType
from typing import Any, Self, Optional, Type
<<<<<<< HEAD

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
=======
from dotenv import load_dotenv
import traceback
import os

load_dotenv() # Procura um arquivo .env com variáveis
DB_PATH = os.getenv('DATABASE', './data/tarefas.sqlite3')

def init_db(db_name: str = DB_PATH) -> None:
    with connect(db_name) as conn:
>>>>>>> origin/main
        conn.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo_tarefa TEXT NOT NULL,
<<<<<<< HEAD
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
=======
            data_conclusao TEXT  
        );
        """)

class Database:
    """
        Classe que gerencia conexões e operações com um banco de dados SQLite. Utiliza o protocolo de gerenciamento de contexto para garantir que a conexão seja encerrada corretamente.
    """
    def __init__(self, db_name: str = DB_PATH) -> None:
        self.connection: Connection = connect(db_name)
        self.cursor: Cursor = self.connection.cursor()

    def executar(self, query: str, params: tuple = ()) -> Cursor:
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor
    
    def buscar_tudo(self, query: str, params: tuple = ()) -> list[Any]:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def close(self) -> None:
        self.connection.close()

    # Métodos para o gerenciamento de contexto
    # Método de entrada no contexto
    def __enter__(self) -> Self:
        return self
    
    # Método de saída do contexto
    def __exit__(
            self, 
            exc_type: Optional[Type[BaseException]], 
            exc_value: Optional[BaseException], 
            tb: Optional[TracebackType]) -> None:
        
        if exc_type is not None:
>>>>>>> origin/main
            print('Exceção capturada no contexto:')
            print(f'Tipo: {exc_type.__name__}')
            print(f'Mensagem: {exc_value}')
            print('Traceback completo:')
            traceback.print_tb(tb)

<<<<<<< HEAD
        # Fecha a conexão ao sair do bloco 'with'
=======
>>>>>>> origin/main
        self.close()