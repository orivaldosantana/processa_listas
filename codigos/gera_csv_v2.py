import processa_notas as pn
import pandas as pd


def mostraColunas(nome_arq_notas_dados):
    notas_dados = pd.read_csv("../dados/{}".format(nome_arq_notas_dados) )
    cont = 0
    for l in notas_dados.columns:
        print(cont,l)
        cont = cont + 1  

# Unidade pode assumir valores 1, 2 e 3
def geraRelatorioUnidade(unidade,nome_arq_notas_dados,selecao,nome_arq_sigaa,nome_arq_saida):
    
    # Obtem os dados dos alunos para
    # organizar de acordo com as matrículas do SIGAA 
    turma_sigaa = pd.read_csv("../dados/{}".format(nome_arq_sigaa))

    # Mostra os dados dos primeiros estudantes da turma 
    print(turma_sigaa.head())

    # Leitura dos dados das notas das listas do sistema LoP
    notas_dados = pd.read_csv("../dados/{}".format(nome_arq_notas_dados) )

    # Não esquecer de selecionar a coluna Mátricula
    # seleciona as colunas de interesse para a unidade 
    notas_u = notas_dados.iloc[:, selecao]
    print("\n\nSeleção de Listas para a Unidade {}\n".format(unidade))
    print(notas_u.columns)

    # Calcula as médias
    notas_u = pn.calcula_media(notas_u)

    # Seleciona apenas os alunos da turma do sigaa 
    padronizada_notas_u = pn.padroniza_sigaa(notas_u, turma_sigaa)

    # remove linhas duplicadas
    padronizada_notas_u = padronizada_notas_u.drop_duplicates()

    
    padronizada_notas_u.to_csv("../saida/{}".format(nome_arq_saida), index=False)


#notas_u2.loc[:, 'Matrícula'] = notas_u2.loc[:, 'Matrícula'].astype(int)

#notas_u2['Matrícula'] = notas_u2['Matrícula'].apply( lambda coment: int(coment)  ) 
#print(notas_u2.iloc[0:10,0] )





mostraColunas("lop_exercicios_02_2022_02_16_rudson.csv")
# Turma 01 - 2021.2 - Orivaldo 
#geraRelatorioUnidade(3,"lop_exercicios_2022_02_15_t01.csv",[1,2,3,4],"turma_01_2021_2.csv","notas_uniao_u3_completo_teste.csv")
# Turma 02 - 2021.2 - Rudson
geraRelatorioUnidade(3,"lop_exercicios_02_2022_02_16_rudson.csv",[1,10,14,15,16],"turma_02_2021_2_rudson.csv","notas_uniao_u3_completo_ruds.csv")

#As listas são: Repetição Contda - lista de exercicios, Vetores - Ressolvida, Vetores - Prática , Vetores - Lista de Exercícios.

