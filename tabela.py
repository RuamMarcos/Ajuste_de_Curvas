from ajuste_de_curvas import calcular_desvio
from ajuste_de_curvas import melhor_reta
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def tabular_reta(pts, reta, nome):
    tabela_reta = [[f"{nome} = {reta[0]}", " "]]

    tabela_reta.append([f"{nome}", "Di"])

    for i in pts:
        tabela_reta.append([f"{reta[1](i[0])}", f"{i[1] - reta[1](i[0])}"])

    tabela_reta.append([f"D = {calcular_desvio(pts, reta)}", " "])

    return tabela_reta


def tabular_pontos(pts):
    pontos = []
    n = 0
    pontos.append([" ", " ", " "])
    pontos.append(["i", "Xi", "Yi"])
    for i in pts:
        pontos.append([n, i[0], i[1]])
        n+=1
    pontos.append([" ", " ", " "])

    return pontos

#dado uma série de pontos e duas retas, essa função gera a tabela
def gerar_tabela(pts, reta1, reta2):
                 #, y1, y2, melhor_reta, desvios):
    tabela = []

    #Agregando os pontos a tabela
    tabela.append(tabular_pontos(pts))

    #Agregando a primeira reta a tebela
    tabela.append(tabular_reta(pts, reta1, "y'"))

    #Agregando a segunda reta a tebela
    tabela.append(tabular_reta(pts, reta2, "y\""))

    #Agregando a melhor reta a tebela
    tabela.append(tabular_reta(pts, melhor_reta(pts), "y"))

    return tabela

#Imprime a tabela passada como argumento
def imprimir_tabela(tabela):
    for j in range(0, len(tabela[0])):  
           print(f"| {tabela[0][j]} | {tabela[1][j]} | {tabela[2][j]} | {tabela[3][j]} | ")

def salvar_imagem_tb(tb):
    for i in tb:
        df = pd.DataFrame(i)

        fig, ax = plt.subplots()
        ax.axis('off')

        tabela = ax.table(cellText=df.values, colLabels=df.columns, cellLoc="center", loc="center")

        tabela.auto_set_font_size(False)
        tabela.set_fontsize(12)
        tabela.scale(1.2, 1.2)

        plt.savefig(f"{tb.index(i)}.png", bbox_inches='tight', pad_inches=0.1)
        plt.show()


    # Carregar as imagens das tabelas
    imagem_tabela_2x4 = Image.open("0.png")
    imagem_tabela_2x6 = Image.open("1.png")

    # Definir a largura e altura para a nova imagem combinada
    nova_largura = imagem_tabela_2x4.width + imagem_tabela_2x6.width
    nova_altura = max(imagem_tabela_2x4.height, imagem_tabela_2x6.height)

    # Criar uma nova imagem em branco com o tamanho definido
    imagem_combinada = Image.new("RGB", (nova_largura, nova_altura), (255, 255, 255))

    # Colar as tabelas na imagem combinada
    imagem_combinada.paste(imagem_tabela_2x4, (0, 0))
    imagem_combinada.paste(imagem_tabela_2x6, (imagem_tabela_2x4.width, 0))

    # Salvar ou exibir a imagem combinada
    imagem_combinada.save("tabela_combinada.png")
    imagem_combinada.show()

