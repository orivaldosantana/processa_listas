import processa_notas as pn
import pandas as pd


def mostraColunas(nome_arq_notas_dados):  

    try:
        notas_dados = pd.read_csv("../dados/{}".format(nome_arq_notas_dados) )
        cont = 0
        for l in notas_dados.columns:
            print(cont,l)
            cont = cont + 1  
    except FileNotFoundError:
        msg = "O arquivo '../dados/{}' não existe.".format(nome_arq_notas_dados)
        print(msg)

    

# Unidade pode assumir valores 1, 2 e 3
def geraRelatorioUnidade(unidade,nome_arq_notas_dados,selecao,nome_arq_sigaa,nome_arq_saida):
    
    # Obtem os dados dos alunos para
    # organizar de acordo com as matrículas do SIGAA 
    try:
        turma_sigaa = pd.read_csv("../dados/{}".format(nome_arq_sigaa))
        # Mostra os dados dos primeiros estudantes da turma 
        print(turma_sigaa.head())
    except :
        msg = "O arquivo '../dados/{}' não existe.".format(nome_arq_sigaa)
        print(msg)
  

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


# Turma 02 - 2023.1 - Orivaldo 
mostraColunas("lop_turma 02-2023-07-03.csv")
#geraRelatorioUnidade(1,"lop_turma_02-2023-05-16.csv",[1,2,3,4,5,6,8],"alunos turma 02 lop 2023_1.csv","notas_uniao_u1_completo.csv")
#geraRelatorioUnidade(2,"lop_turma 02-2023-07-03.csv",[1,17,12,9,10,13,11],"alunos turma 02 lop 2023_1.csv","notas_uniao_u2_completo.csv")
geraRelatorioUnidade(3,"lop_turma 02-2023-07-03.csv",[1,14,15,16],"alunos turma 02 lop 2023_1.csv","notas_uniao_u3_completo.csv")



# Turma 02 - 2022.2 - Orivaldo 
#mostraColunas("lop_exercicios_turma02-2022-11-07.csv")
#geraRelatorioUnidade(1,"lop_exercicios_turma02-2022-11-07.csv",[1,2,3,4,5,6,7],"alunos_turma_02_2022_2.csv","notas_uniao_u1_completo.csv")


# Turma 02 - 2022.2 - Orivaldo - U2 
#mostraColunas("lop_exercicios_turma02-2022-12-13.csv")
#geraRelatorioUnidade(1,"lop_exercicios_turma02-2022-12-13.csv",[1,16,11,8,9,12,10],"alunos_turma_02_2022_2.csv","notas_uniao_u2_completo.csv")


# Turma 02 - 2022.2 - Orivaldo - U3
#geraRelatorioUnidade(3,"lop_exercicios_turma02-2022-12-13.csv",[1,13,14,15],"alunos_turma_02_2022_2.csv","notas_uniao_u3_completo.csv")



# Turma 02 - 2022.1 - Orivaldo 
#mostraColunas("lop_exercicios_t02_2022_06_09_oriva.csv")
#geraRelatorioUnidade(1,"lop_exercicios_t02_2022_06_09_oriva.csv",[1,2,3,4,5,6,7],"turma_02_2022_1_oriva.csv","notas_uniao_u1_completo.csv")
# Turma 01 - 2021.2 - Orivaldo 
#geraRelatorioUnidade(3,"lop_exercicios_2022_02_15_t01.csv",[1,2,3,4],"turma_01_2021_2.csv","notas_uniao_u3_completo_teste.csv")
# Turma 02 - 2021.2 - Rudson
#geraRelatorioUnidade(1,"lop_exercicios_01_2022_05_14_rudson.csv",[1,2,3,4,5,6,7],"turma_03_2022_1_rudson.csv","notas_uniao_u1_completo.csv")
#mostraColunas("lop_exercicios_01_2022_05_14_rudson.csv")
#geraRelatorioUnidade(3,"lop_exercicios_02_2022_02_16_rudson.csv",[1,10,14,15,16],"turma_02_2021_2_rudson.csv","notas_uniao_u3_completo_ruds.csv")

#As listas são: Repetição Contda - lista de exercicios, Vetores - Ressolvida, Vetores - Prática , Vetores - Lista de Exercícios.

