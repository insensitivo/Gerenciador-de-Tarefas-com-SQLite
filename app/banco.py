import sqlite3

BANCO = "tarefas.db"


def conectar():
    return sqlite3.connect(BANCO)


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            concluida INTEGER DEFAULT 0
        )
    """)

    conexao.commit()
    conexao.close()