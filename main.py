from app.interface import menu
from app.banco import criar_tabela


def main():
    criar_tabela()
    menu()


if __name__ == "__main__":
    main()