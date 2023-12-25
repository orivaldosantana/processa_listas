import processa_notas as pn
import pandas as pd


nome_arq_sigaa = "alunos_turma_01_2023_2.csv"
nome_arq_notas_dados = "presenca.csv"

try:
   turma_sigaa = pd.read_csv("../dados/{}".format(nome_arq_sigaa))
   # Mostra os dados dos primeiros estudantes da turma 
   print(turma_sigaa.head())
except :
   msg = "O arquivo '../dados/{}' não existe.".format(nome_arq_sigaa)
   print(msg)


try:
   # Leitura dos dados das notas das listas do sistema LoP
   notas_dados = pd.read_csv("../dados/{}".format(nome_arq_notas_dados) )
except :
   msg = "O arquivo '../dados/{}' não existe.".format(nome_arq_notas_dados)
   print(msg)



# Seleciona apenas os alunos da turma do sigaa 
padronizada_notas_u = pn.padroniza_sigaa(notas_dados, turma_sigaa)

# remove linhas duplicadas
padronizada_notas_u = padronizada_notas_u.drop_duplicates()

padronizada_notas_u.to_csv("../saida/{}".format("teste.csv"), index=False)
