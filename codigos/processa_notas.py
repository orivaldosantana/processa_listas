import pandas as pd


def padroniza_sigaa(notas_u, turma_sig):
    # converte o campo matrícula para inteiro
    #notas_u.loc[:, 'Matrícula'] = notas_u.loc[:, 'Matrícula'].astype(int)
    notas_u['Matrícula'] = notas_u['Matrícula'].apply( lambda m: int(m)  ) 
    # junta dois data-frames pela matrícula
    notas_uniao_u = pd.merge(turma_sig, notas_u, how='left', on='Matrícula')
    return notas_uniao_u


def calcula_media(notas_u):
    # divite as notas por 10
    notas_u_listas = notas_u
    notas_u_listas.iloc[:, 1:] = notas_u.iloc[:, 1:].div(10)
    # Calcula a média de cada aluno
    notas_u_listas.loc[:, 'Média'] = notas_u_listas.iloc[:, 1:].mean(axis=1)
    return notas_u_listas
