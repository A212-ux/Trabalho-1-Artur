from enum import Enum
import os

# Enumeração de tipos de ativos TI
class TipoAtivo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    SOFTWARE_LICENCIADO = 4

ARQUIVO_DADOS = "ativos_db.txt"

# Menu textual principal com tratamento de erros
def main():
    ativos = carregar_dados()
    while True:
        print("\n==============================================")
        print("   SISTEMA DE INVENTÁRIO DE CIBERSEGURANÇA    ")
        print("==============================================")
# Mostra dinamicamente quantos ativos estão cadastrados na base
        print(f" Status da Base: {len(ativos)} ativo(s) cadastrado(s)")
        print("----------------------------------------------")
        print("1. Cadastrar Ativo")
        print("2. Consultar Ativos e Vulnerabilidades")
        print("3. Atualizar Ativo")
        print("4. Remover Ativo")
        print("5. Adicionar Vulnerabilidade a um Ativo")
        print("6. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_ativo(ativos)
        elif opcao == "2":
            consultar_ativos(ativos)
        elif opcao == "3":
            atualizar_ativo(ativos)
        elif opcao == "4":
            deletar_ativo(ativos)
        elif opcao == "5":
            adicionar_vulnerabilidades(ativos)
        elif opcao == "6":
            print("Saindo do sistema!")
            break
        else:
            print("Opção inválida! Escolha um número de 1 a 6.")

if __name__ == "__main__":
    main()
