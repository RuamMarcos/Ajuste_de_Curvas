from ajuste_de_curvas import *
from tabela import gerar_tabela, salvar_imagem_tb


#Criando e recebendo os pontos
pontos = ler_pts()

#Recebendo a reta aleatória y'
y1 = ler_reta()

#Recebendo a reta aleatória y''
y2 = ler_reta()

#gerando a tabela
tabela = gerar_tabela(pontos, y1, y2)
salvar_imagem_tb(tabela)

