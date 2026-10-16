from enum import Enum
import os

# Enumeração de tipos de ativos TI
class TipoAtivo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    SOFTWARE_LICENCIADO = 4

ARQUIVO_DADOS = "ativos_db.txt"

# Uso de dicionário para otimizar buscas e gerenciamento em memória
def carregar_dados():
    ativos = {}
    if not os.path.exists(ARQUIVO_DADOS):
        return ativos
    
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) >= 6:
                ativos_id = int(partes[0])
                ativos[ativo_id] = {
                    "id": ativo_id,
                    "hostname": partes[1],
                    "responsavel": partes [2],
                    "setor": partes[3],
                    "tipo": partes[4],
                    "vulnerabilidades": eval(partes[5]) # Carrega alista de vulnerabilidades
                }
    return ativos

def salvar_dados(ativos):
    with open(ARQUIVO_DADOS, "w", encoding="uft-8") as f:
        for ativo in ativos.values():
            linha = f"{ativo['id']};{ativo['hostname']};{ativo['responsavel']};{ativo['setor']};{ativo['tipo']};{ativo['vulnerabilidades']}\n"
            f.write(linha)

# Cadastrar ativo
def cadastrar_ativo(ativos):
    print("\n---Cadastrar Novo Ativo ---")
    while True:
        try:
            ativo_id = int(input("ID único(número inteiro): "))
            if ativo_id in ativos:
                print("Erro: Já existe um ativo com esse ID.")
                continue
            break
        except ValueError:
            print("Digite um número inteiro válido.")

    hostname = input("Hostname / Nome do ativo: ").strip()
    responsavel = input("Responsável: ").strip()
    setor = input("Setor / localização: ").strip()

    print("\nTipos de Ativos:")
    for tipo in TipoAtivo:
        print(f"[{tipo.value}] {tipo.name.replace('_',' ')}")

    while True:
        try:
            tipo_escolhido = int(input("Escolha o número do tipo de ativo (1 a 4): "))
            tipo_obj = TipoAtivo(tipo_escolhido)
            break
        except ValueError:
            print("Escolha um número válido entre 1 e 4.")

    ativos[ativo_id] = {
        "id": ativo_id,
        "hostname": hostname,
        "responsavel": responsavel,
        "setor": setor,
        "tipo": tipo_obj.name,
        "vulnerabilidades": []
    }
    salvar_dados(ativos)
    print("Ativo cadastrado com sucesso!")

# Buscar e visualisar ativos e vulnerabilidades
def consultar_ativos(ativos):
    print("\n--- Consultar Ativos ---")
    if not ativos:
        print("Nenhum ativo cadastrado na base.")
        return
    
    busca = input("Digite o ID ou o Hostname do ativo (ou deixe em branco para ver todos): ").strip()

    encontrados = []
    for ativo in ativos.values():
        if not busca or str(ativo["id"]) == busca or busca.lower() in ativo["hostname"].lower():
            encontrads.append(ativo)

    if not encontrados:
        print("Nenhum ativo encontrado.")
        return

    for a in encontrados:
        print(f"\nID: {a['id']} | Hostname: {a['hostname']} | Responsável: {a['responsavel']} | Setor: {a['setor']} | Tipo: {a['tipo']}")
        print("Vulnerabilidades associadas:")
        if not a["vulnerabilidades"]:
            print("  -> O ativo está sem vulnerabilidades registradas.")
        else:
            for v in a["vulnerabilidades"]:
                print(f"  - Descrição: {v['descricao']} | Severidade: {v['severidade']} | Status: {v['status']}")

# Atualizar dados de um ativo     
def atualizar_ativo(ativos):
    print("\n--- Atualizar Ativo ---")
    try:
        ativo_id = int(input("Digite o ID do ativo que desja atualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    if ativo_id not in ativos:
        print("Ativo não encontrado.")
        return

    ativo = ativos[ativo_id]
    print(f"Atualizando ativo: {ativo['hostname']} (Deixe em branco para manter o valor atual)")

    novo_resp = input(f"Novo responsável [{ativo['responsavel']}]: ").strip()
    if novo_resp: ativo['responsavel'] = novo_resp

    novo_setor = input(f"Novo setor [{ativo['setor']}]: ").strip()
    if novo_setor: ativo['setor'] = novo_setor

    salvar_dados(ativos)
    print("Ativo atualizado com sucesso!")

# Deletar ativo
def deletar_ativo(ativos):
    print("\n--- Remover Ativo ---")
    try:
        ativo_id = int(input("Digitr o ID do ativo que desja remover: "))
    except ValueError:
        print("ID inválido.")
        return
    
    if ativo_id in ativos:
        del ativos[ativo_id]
        salvar_dados(ativos)
        print("Ativo e suas vulnerabilidades removidos com sucesso!")
    else:
        print("Ativo não encontrado.")

# Cadastrar vulnerabilidades em um ativo
def adicionar_vulnerabilidades(ativos):
    print("\n--- Cadastrar Vulnerabilidade ---")
    try:
        ativo_id = int(input("Digite o Id do ativo para associar a vulnerabilidade; "))
    except ValueError:
        print("ID inváçido.")
        return
    
    if ativo_id not in ativos:
        print("Ativo não encontrado.")
        return

    descricao = input("Descrição da vulnerabilidade: ").strip()
    
    print("Severidades: [1] Baixa  [2] Média  [3] Alta  [4] Crítica")
    sev_op = input("Escolha a severidade (Baixa/Média/Alta/Crítica): ").strip().capitalize()
    if sev_op not in ["Baixa", "Média", "Alta", "Crítica"]:
        sev_op = "Média"

    print("Status: [1] Aberta  [2] Em tratamento  [3] Corrigida  [4] Risco aceito")
    status_op = input("Digite o status: ").strip()
    
    nova_vuln = {
        "descricao": descricao,
        "severidade": sev_op,
        "status": status_op if status_op else "Aberta"
    }

    ativos[ativo_id]["vulnerabilidades"].append(nova_vuln)
    salvar_dados(ativos)
    print("Vulnerabilidade associada com sucesso!")

# Menu textual principal com tratamneto de erros
def main():
    ativos = carregar_dados()
    while True:
        print("\n==============================================")
        print("   SISTEMA DE INVENTÁRIO DE CIBERSEGURANÇA    ")
        print("==============================================")
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
            adicionar_vulnerabilidade(ativos)
        elif opcao == "6":
            print("Saindo do sistema. Bom trabalho na apresentação!")
            break
        else:
            print("Opção inválida! Escolha um número de 1 a 6.")

if __name__ == "__main__":
    main()
