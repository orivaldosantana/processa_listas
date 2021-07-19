import processa_notas as pn
import pandas as pd

# Leitura dos dados das notas das listas do sistema LoP
#notas_dados = pd.read_csv("../dados/lop_exercicios_2021_02_27.csv")
notas_dados = pd.read_csv("../dados/lop_exercicios_2021_07_14.csv")
#notas_dados = pd.read_csv("../dados/rudson_tuma05_lop_exercicios_2021_07_19.csv")
print(notas_dados.head())


# seleciona as coluas de interesse para a unidade 1
notas_u1 = notas_dados.iloc[:,  [1, 2, 3, 4, 5, 6, 7]]
# seleciona as coluas de interesse para a unidade 2
#notas_u2 = notas_dados.iloc[:,  [1, 8, 9, 10, 11, 12, 16]]
# seleciona as coluas de interesse para a unidade 3
#notas_u3 = notas_dados.iloc[:, [1, 13, 14, 15]]

print("\nSeleção de Listas para a Unidade I")
print(notas_u1.columns)

print("\nSeleção de Listas para a Unidade II")
#print(notas_u2.columns)

print("\nSeleção de Listas para a Unidade III")
#print(notas_u3.columns)

# Calcula as médias
notas_u1 = pn.calcula_media(notas_u1)
#notas_u2 = pn.calcula_media(notas_u2)
#notas_u3 = pn.calcula_media(notas_u3)

print(notas_u1.head())

# Organiza de acordo com as matrículas do SIGAA
#turma_sigaa = pd.read_csv("../dados/turma_03_2020_2.csv")
turma_sigaa = pd.read_csv("../dados/turma_02_2021_1.csv")
#turma_sigaa = pd.read_csv("../dados/rudson_alunos_T5_2021.csv")

print(turma_sigaa.head())

padronizada_notas_u1 = pn.padroniza_sigaa(notas_u1, turma_sigaa)
#padronizada_notas_u2 = pn.padroniza_sigaa(notas_u2, turma_sigaa)
#padronizada_notas_u3 = pn.padroniza_sigaa(notas_u3, turma_sigaa)
# remove linhas duplicadas
padronizada_notas_u1 = padronizada_notas_u1.drop_duplicates()
#padronizada_notas_u2 = padronizada_notas_u2.drop_duplicates( )
#padronizada_notas_u3 = padronizada_notas_u3.drop_duplicates()

print(padronizada_notas_u1.head())

padronizada_notas_u1.to_csv(
    "../saida/notas_uniao_u1_completo.csv", index=False)
