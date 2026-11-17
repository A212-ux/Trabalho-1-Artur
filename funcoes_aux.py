# Uso de dicionário para otimizar buscas e gerenciamento em memória
def carregar_dados():
    ativos = {}
    if not os.path.exists(ARQUIVO_DADOS):
        return ativos
    
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) >= 6:
                ativo_id = int(partes[0])
                ativos[ativo_id] = {
                    "id": ativo_id,
                    "hostname": partes[1],
                    "responsavel": partes [2],
                    "setor": partes[3],
                    "tipo": partes[4],
                    "vulnerabilidades": partes[5] # Carrega a lista de vulnerabilidades
                }
    return ativos

def salvar_dados(ativos):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        for ativo in ativos.values():
            linha = f"{ativo['id']};{ativo['hostname']};{ativo['responsavel']};{ativo['setor']};{ativo['tipo']};{ativo['vulnerabilidades']}\n"
            f.write(linha)
