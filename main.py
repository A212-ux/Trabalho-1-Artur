from enum import Enum
import os

# Enumeração de tipos de ativos TI
class TipoAtivo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    ESTACAO_TRABALHO = 4

ARQUIVO_DADOS = "ativos_db.txt"

# Uso de dicionário para otimizar buscas e gerenciamento em memória
def carregar_dados():
    ativos = {}
    if not os.path.exists(ARQUIVO_DADOS):
        return ativos
    
    with open(ARQUIVO_DADOS)

