import pandas as pd
import matplotlib.pyplot as plt

# Dados para a tabela
dados = {
    "i": ["1", "2", "...", "n"],
    "x_i": ["x_1", "x_2", "...", "x_n"],
    "y_i": ["y_1", "y_2", "...", "y_n"],
    "ŷ = a + bx_i": ["ŷ_1", "ŷ_2", "...", "ŷ_n"],
    "d_i (1)": ["d_1", "d_2", "...", "d_n"],
    "ŷ = c + dx_i": ["ŷ_1", "ŷ_2", "...", "ŷ_n"],
    "d_i (2)": ["d_1", "d_2", "...", "d_n"],
    "y_i = m + nx_i": ["y_1", "y_2", "...", "y_n"],
    "d_i (3)": ["d_1", "d_2", "...", "d_n"]
}

# Criação do DataFrame
df = pd.DataFrame(dados)

# Criação da figura e do eixo
fig, ax = plt.subplots(figsize=(10, 2))  # Ajuste o tamanho conforme necessário
ax.axis('off')  # Esconde o eixo

# Adiciona a tabela ao eixo
tabela = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# Ajusta a fonte e escala da tabela
tabela.auto_set_font_size(False)
tabela.set_fontsize(10)
tabela.scale(1.5, 1.5)

# Exibe a tabela
plt.show()
