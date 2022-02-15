import processa_notas as pn
import pandas as pd

# Leitura dos dados das notas das listas do sistema LoP
#notas_dados = pd.read_csv("../dados/lop_exercicios_2021_02_27.csv")
#notas_dados = pd.read_csv("../dados/lop_exercicios_2021_07_14.csv")
#notas_dados = pd.read_csv("../dados/lop_exercicios_2021_08_23.csv")
#notas_dados = pd.read_csv("../dados/rudson_tuma05_lop_exercicios_2021_07_19.csv")
#notas_dados = pd.read_csv("../dados/rudson_tuma05_lop_exercicios_2021_08_30.csv")
#notas_dados = pd.read_csv("../dados/lop_exercicios_2021_09_18.csv")
#notas_dados = pd.read_csv("../dados/lop_exercicios_2021_11_28.csv")
#../dados/lop_exercicios_2022_02_02_t01.csv")
#notas_dados = pd.read_csv("../dados/lop_exercicios_2022_02_01_t02.csv")
notas_dados = pd.read_csv("../dados/lop_exercicios_2022_02_14_t01.csv")
#print(notas_dados.head())
#print(notas_dados.columns)
cont = 0
for l in notas_dados.columns:
    print(cont,l)
    cont = cont + 1   

# Não esquecer de selecionar a coluna Mátricula
# seleciona as colunas de interesse para a unidade 1
#notas_u1 = notas_dados.iloc[:,  [1, 2, 3, 4, 5, 6, 7]]
# seleciona as coluas de interesse para a unidade 2
#notas_u2 = notas_dados.iloc[:,  [1, 8, 9, 10, 11, 12, 16]]
notas_u2 = notas_dados.iloc[:,  [1, 17, 12, 8, 9, 13, 10, 11]]
#notas_u2 = notas_dados.iloc[:,  [1,13, 8, 5, 6, 9 , 7]]
#notas_u2 = notas_dados.iloc[:,  1:9]
# seleciona as coluas de interesse para a unidade 3
#notas_u3 = notas_dados.iloc[:, [1, 13, 14, 15]]

#print("\nSeleção de Listas para a Unidade I")
#print(notas_u1.columns)

print("\n\nSeleção de Listas para a Unidade II\n")
print(notas_u2.columns)

#print("\nSeleção de Listas para a Unidade III")
#print(notas_u3.columns)

# Calcula as médias
#notas_u1 = pn.calcula_media(notas_u1)
notas_u2 = pn.calcula_media(notas_u2)
#notas_u3 = pn.calcula_media(notas_u3)


#notas_u2.loc[:, 'Matrícula'] = notas_u2.loc[:, 'Matrícula'].astype(int)

#notas_u2['Matrícula'] = notas_u2['Matrícula'].apply( lambda coment: int(coment)  ) 
#print(notas_u2.iloc[0:10,0] )

# Organiza de acordo com as matrículas do SIGAA
#turma_sigaa = pd.read_csv("../dados/turma_03_2020_2.csv")
#turma_sigaa = pd.read_csv("../dados/turma_02_2021_1.csv")
#turma_sigaa = pd.read_csv("../dados/turma_01_2021_2.csv")
#turma_sigaa = pd.read_csv("../dados/rudson_alunos_T5_2021.csv")
turma_sigaa = pd.read_csv("../dados/turma_02_2021_2_rudson.csv")

print(turma_sigaa.head())

#padronizada_notas_u1 = pn.padroniza_sigaa(notas_u1, turma_sigaa)
padronizada_notas_u2 = pn.padroniza_sigaa(notas_u2, turma_sigaa)
#padronizada_notas_u3 = pn.padroniza_sigaa(notas_u3, turma_sigaa)
# remove linhas duplicadas
#padronizada_notas_u1 = padronizada_notas_u1.drop_duplicates()
padronizada_notas_u2 = padronizada_notas_u2.drop_duplicates( )
#padronizada_notas_u3 = padronizada_notas_u3.drop_duplicates()

#print(padronizada_notas_u1.head())

#padronizada_notas_u1.to_csv("../saida/notas_uniao_u1_completo.csv", index=False)
padronizada_notas_u2.to_csv("../saida/notas_uniao_u2_completo_ruds.csv", index=False)
