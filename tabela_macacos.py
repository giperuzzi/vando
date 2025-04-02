import pandas as pd
import numpy as np

# Definição das colunas (variáveis)
colunas = ["Especie", "Tamanho", "Peso", "Expectativa_Vida", "Populacao", "Regiao"]

# Dados das espécies de macacos
especies = ["Bugio", "Macaco-Prego", "Mico-Leao-Dourado", "Mandril", "Babuíno", "Gorila", "Orangotango", "Gibão", "Sagui", "Colobus"]

# Geração dos dados aleatórios
np.random.seed(42)  # Para reprodutibilidade dos resultados
dados = {
    "Especie": especies,
    "Tamanho": np.round(np.random.uniform(30, 200, 10), 2),  # cm
    "Peso": np.round(np.random.uniform(1, 200, 10), 1),  # kg
    "Expectativa_Vida": np.random.randint(10, 50, 10),  # anos
    "Populacao": np.random.randint(1000, 1000000, 10),  # indivíduos
    "Regiao": ["América do Sul", "América do Sul", "Brasil", "África", "África", "África", "Ásia", "Ásia", "América do Sul", "África"]
}

# Criando a tabela (DataFrame)
tabela = pd.DataFrame(dados)

# Exibir a tabela
print("Tabela de Dados de Macacos:")
print(tabela)

# Exibir a contagem de linhas e colunas
linhas, colunas = tabela.shape
print(f"\Número de linhas: {linhas}")
print(f"Número de colunas: {colunas}")
