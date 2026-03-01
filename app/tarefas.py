from app.banco import conectar


def adicionar_tarefa(titulo, descricao):
    if not titulo.strip():
        print("Título não pode ser vazio.\n")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO tarefas (titulo, descricao) VALUES (?, ?)",
        (titulo.strip(), descricao.strip())
    )

    conexao.commit()
    conexao.close()

    print("Tarefa adicionada com sucesso.\n")


def listar_tarefas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id, titulo, descricao, concluida FROM tarefas")
    tarefas = cursor.fetchall()

    conexao.close()

    if not tarefas:
        print("\nNenhuma tarefa cadastrada.\n")
        return

    print("\nLista de Tarefas:")
    for tarefa in tarefas:
        status = "✔" if tarefa[3] == 1 else "Pendente"
        print(f"ID: {tarefa[0]}")
        print(f"Título: {tarefa[1]}")
        print(f"Descrição: {tarefa[2]}")
        print(f"Status: {status}")
        print("-" * 30)
    print()


def concluir_tarefa(id_tarefa):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id FROM tarefas WHERE id = ?", (id_tarefa,))
    if cursor.fetchone() is None:
        print("ID não encontrado.\n")
        conexao.close()
        return

    cursor.execute(
        "UPDATE tarefas SET concluida = 1 WHERE id = ?",
        (id_tarefa,)
    )

    conexao.commit()
    conexao.close()

    print("Tarefa marcada como concluída.\n")


def remover_tarefa(id_tarefa):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id FROM tarefas WHERE id = ?", (id_tarefa,))
    if cursor.fetchone() is None:
        print("ID não encontrado.\n")
        conexao.close()
        return

    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conexao.commit()
    conexao.close()

    print("Tarefa removida com sucesso.\n")