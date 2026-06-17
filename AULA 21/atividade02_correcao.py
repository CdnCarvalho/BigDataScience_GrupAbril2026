import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # Delimitando somente as variáveis necessárias
    df_estelionato = df_ocorrencias[['mes_ano', 'estelionato']]

    # Totalizar estelionato por mês/ano
    df_estelionato = df_estelionato.groupby('mes_ano', as_index=False)['estelionato'].sum()

    print(df_estelionato.head())

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()



# obter informações sobre padrão de estelionato
try:
    print('Obtendo informações sobre padrão de estelionato...')

    # Converter para array numpy
    array_estelionato = np.array(df_estelionato['estelionato'])

    # Média e mediana
    media = np.mean(array_estelionato)
    mediana = np.median(array_estelionato)

    # Distância relativa entre média e mediana
    distancia = abs((media - mediana) / mediana)

    print('\nMedidas de tendência central: ')
    print(30*'-')
    print(f'Média de estelionatos: {media}')
    print(f'Mediana de estelionatos: {mediana}')
    print(f'Distância entre média e mediana: {distancia}')


    # Quartis (Weibull)
    q1 = np.quantile(array_estelionato, 0.25)
    q2 = np.quantile(array_estelionato, 0.50)
    q3 = np.quantile(array_estelionato, 0.75)

   
    # Mairores e menores estelionatos
    print('\nMeses/Ano com menores quantidades de estelionato:')
    print(30*'-')
    df_estelionato_menores = df_estelionato[df_estelionato['estelionato'] < q1]
    print(df_estelionato_menores.sort_values(by='estelionato'))

    print('\nMeses/Ano com maiores quantidades de estelionato:')
    print(30*'-')
    df_estelionato_maiores = df_estelionato[df_estelionato['estelionato'] > q3]
    print(df_estelionato_maiores.sort_values(by='estelionato', ascending=False))



    # Medidas de dispersão
    maximo = np.max(array_estelionato)
    minimo = np.min(array_estelionato)
    amplitude = maximo - minimo

    print('\nMedidas de dispersão: ')
    print(30*'-')
    print('Máximo: ', maximo)
    print('Mínimo: ', minimo)
    print('Amplitude total: ', amplitude)


    # IQR
    iqr = q3 - q1


    # Cálculo dos limites para outliers
    limite_superior = q3 + (1.5 * iqr)
    limite_inferior = q1 - (1.5 * iqr)

    print('\nMedidas de posição: ')
    print(30*'-')
    print('Mínimo: ', minimo)
    print(f'Limite inferior: {limite_inferior}')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')
    print(f'IQR: {iqr}')
    print(f'Limite superior: {limite_superior}')
    print('Máximo: ', maximo)


    # ---------------------------- ACHANDO OS OUTLIERS -------------------------
    df_outliers_inferiores = df_estelionato[df_estelionato['estelionato'] < limite_inferior]
    df_outliers_superiores = df_estelionato[df_estelionato['estelionato'] > limite_superior]

    print('\nMeses/Ano com outliers inferiores: ')
    print(30*'-')
    if len(df_outliers_inferiores) == 0:
        print('Não existem outliers inferiores!')
    else:
        print(df_outliers_inferiores.sort_values(by='estelionato'))

    print('\nMeses/Ano com outliers superiores: ')
    print(30*'-')
    if len(df_outliers_superiores) == 0:
        print('Não existem outliers superiores!')
    else:
        print(df_outliers_superiores.sort_values(by='estelionato', ascending=False))

except Exception as e:
    print(f'Erro ao obter informações sobre padrão de estelionato: {e}')
    exit()


# VISUALIZAÇÃO
try:
    # pip install matplotlib
    # plt.figure(figsize=(18, 10))
    plt.subplots(2, 2, figsize=(18, 10))

    # POSIÇÃO 01 - BOXPLOT DA DISTRIBUIÇÃO
    plt.subplot(2, 2, 1)
    plt.boxplot(array_estelionato, vert=False, showmeans=True)


    # POSIÇÃO 02 - MEDIDAS ESTATÍSTICAS
    plt.subplot(2, 2, 2)
    plt.text(0.1, 0.9, f'Média: {media}')
    plt.text(0.1, 0.8, f'Mediana: {mediana}')
    plt.text(0.1, 0.7, f'Distância: {distancia}')
    plt.text(0.1, 0.6, f'Mínimo: {minimo}')

    plt.text(0.1, 0.5, f'Limite inferior: {limite_inferior}', fontsize=10)
    plt.text(0.1, 0.4, f'Q1: {q1}', fontsize=10)
    plt.text(0.1, 0.3, f'Q3: {q3}', fontsize=10)
    plt.text(0.1, 0.2, f'Limite superior: {limite_superior}', fontsize=10)
    plt.text(0.1, 0.1, f'Maior valor: {maximo}', fontsize=10)
    plt.text(0.1, 0.0, f'Amplitude Total: {amplitude}', fontsize=10)

    plt.axis('off')
    plt.title('Resumo Estatístico')


    # POSIÇÃO 03 - Outlieres Superiores
    plt.subplot(2, 2, 3)
    df_outliers_superiores = (
    df_outliers_superiores
    # .sort_values(by='estelionato', ascending=False)
    .head(10)
    .sort_values(by='estelionato', ascending=True)
)

    plt.barh(df_outliers_superiores['mes_ano'], df_outliers_superiores['estelionato'])

    plt.title('Outliers superiores - quantidades de estelionato')


    # POSIÇÃO 04 - Outlieres Inferiores ou Menores Estelionatos
    plt.subplot(2, 2, 4)
    if len(df_outliers_inferiores) > 0:
        df_outliers_inferiores = (
            df_outliers_inferiores
            .sort_values(by='estelionato', ascending=True)
        )

        plt.barh(
            df_outliers_inferiores['mes_ano'], 
            df_outliers_inferiores['estelionato']
        )
        plt.title('Meses e anos com Outliers Inferiores')


    # Caso não existam, exibe os 10 menores valores
    else:
        df_estelionato_menores = (
            df_estelionato_menores
            .sort_values(by='estelionato', ascending=True)
            .head(10)
            .sort_values(by='estelionato', ascending=False)
        )

        plt.barh(
            df_estelionato_menores['mes_ano'], 
            df_estelionato_menores['estelionato']
        )
        plt.title('Bottom 10 - Municípios com menores roubos')

    plt.tight_layout()
    plt.show()


except Exception as e:
    print(f'Erro ao visualizar os dados: {e}')
    exit()