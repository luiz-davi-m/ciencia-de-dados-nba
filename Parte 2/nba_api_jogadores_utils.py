from nba_api.stats.endpoints import commonplayerinfo, playergamelog, playercareerstats
from nba_api.stats.static import players
import pandas as pd


def buscar_id_jogador(nome_jogador):
    jogadores = players.get_players()
    dicionario_jogadores = next((jogador for jogador in jogadores if jogador['full_name'] == nome_jogador), None)
    if dicionario_jogadores:
        return dicionario_jogadores['id']
    return None


def obter_info_basica_jogador(id_jogador):
    info_jogador = commonplayerinfo.CommonPlayerInfo(player_id=id_jogador)
    return info_jogador.get_data_frames()[0]


def obter_logs_dos_jogos_por_jogador(id_jogador, temporada):
    logs = playergamelog.PlayerGameLog(player_id=id_jogador, season=temporada)
    return logs.get_data_frames()[0]


def calcular_medias_jogador(nome_jogador, arquivo_csv):
    df = pd.read_csv(arquivo_csv)

    df_jogador = df[df["Jogador"] == nome_jogador].copy()


    if df_jogador.empty:
        print(f"Jogador {nome_jogador} não encontrado no arquivo CSV!")
        return

    df_jogador[['Pontos', 'Rebotes', 'Assistências']] = df_jogador[['Pontos', 'Rebotes', 'Assistências']].apply(pd.to_numeric)

    media_pontos = df_jogador['Pontos'].mean()
    media_rebotes = df_jogador['Rebotes'].mean()
    media_assistencias = df_jogador['Assistências'].mean()

    print(f"📊 Estatísticas de {nome_jogador}:")
    print(f"   🏀 Média de pontos por jogo: {media_pontos:.2f}")
    print(f"   🔄 Média de rebotes por jogo: {media_rebotes:.2f}")
    print(f"   🎯 Média de assistências por jogo: {media_assistencias:.2f}")
    print("-" * 40)

    return media_pontos, media_rebotes, media_assistencias


def calcular_porcentagem_abaixo_media(nome_jogador, media_pontos, media_rebotes, media_assistencias, arquivo_csv):
    df = pd.read_csv(arquivo_csv)

    df_jogador = df[df["Jogador"] == nome_jogador].copy()

    if df_jogador.empty:
        print(f"Jogador {nome_jogador} não encontrado no arquivo CSV!")
        return None, None, None

    df_jogador.loc[:, ['Pontos', 'Rebotes', 'Assistências']] = df_jogador[['Pontos', 'Rebotes', 'Assistências']].apply(pd.to_numeric)

    total_jogos = len(df_jogador)

    pontos_abaixo = (df_jogador['Pontos'] < media_pontos).sum() / total_jogos * 100
    rebotes_abaixo = (df_jogador['Rebotes'] < media_rebotes).sum() / total_jogos * 100
    assistencias_abaixo = (df_jogador['Assistências'] < media_assistencias).sum() / total_jogos * 100

    print(f"📉 Estatísticas de {nome_jogador} abaixo da média:")
    print(f"   ❌ {pontos_abaixo:.2f}% dos jogos com pontos abaixo da média ({media_pontos:.2f})")
    print(f"   ❌ {rebotes_abaixo:.2f}% dos jogos com rebotes abaixo da média ({media_rebotes:.2f})")
    print(f"   ❌ {assistencias_abaixo:.2f}% dos jogos com assistências abaixo da média ({media_assistencias:.2f})")
    print("-" * 40)


def calcular_medianas_jogador(nome_jogador, arquivo_csv):
    df = pd.read_csv(arquivo_csv)

    df_jogador = df[df["Jogador"] == nome_jogador].copy()

    if df_jogador.empty:
        print(f"Jogador {nome_jogador} não encontrado no arquivo CSV!")
        return None, None, None

    df_jogador[['Pontos', 'Rebotes', 'Assistências']] = df_jogador[['Pontos', 'Rebotes', 'Assistências']].apply(pd.to_numeric)

    mediana_pontos = df_jogador['Pontos'].median()
    mediana_rebotes = df_jogador['Rebotes'].median()
    mediana_assistencias = df_jogador['Assistências'].median()

    print(f"📊 Medianas de {nome_jogador}:")
    print(f"   🔸 Mediana de pontos: {mediana_pontos:.2f}")
    print(f"   🔸 Mediana de rebotes: {mediana_rebotes:.2f}")
    print(f"   🔸 Mediana de assistências: {mediana_assistencias:.2f}")
    print("-" * 40)

    return mediana_pontos, mediana_rebotes, mediana_assistencias


def calcular_porcentagem_abaixo_mediana(nome_jogador, mediana_pontos, mediana_rebotes, mediana_assistencias, arquivo_csv):
    df = pd.read_csv(arquivo_csv)

    df_jogador = df[df["Jogador"] == nome_jogador].copy()

    if df_jogador.empty:
        print(f"Jogador {nome_jogador} não encontrado no arquivo CSV!")
        return None, None, None

    df_jogador[['Pontos', 'Rebotes', 'Assistências']] = df_jogador[['Pontos', 'Rebotes', 'Assistências']].apply(pd.to_numeric)

    total_jogos = len(df_jogador)

    pontos_abaixo = (df_jogador['Pontos'] < mediana_pontos).sum() / total_jogos * 100
    rebotes_abaixo = (df_jogador['Rebotes'] < mediana_rebotes).sum() / total_jogos * 100
    assistencias_abaixo = (df_jogador['Assistências'] < mediana_assistencias).sum() / total_jogos * 100

    print(f"📉 Estatísticas de {nome_jogador} abaixo da mediana:")
    print(f"   ❌ {pontos_abaixo:.2f}% dos jogos com pontos abaixo da mediana ({mediana_pontos:.2f})")
    print(f"   ❌ {rebotes_abaixo:.2f}% dos jogos com rebotes abaixo da mediana ({mediana_rebotes:.2f})")
    print(f"   ❌ {assistencias_abaixo:.2f}% dos jogos com assistências abaixo da mediana ({mediana_assistencias:.2f})")
    print("-" * 40)


def calcular_moda_jogador(nome_jogador, arquivo_csv):
    df = pd.read_csv(arquivo_csv)

    df_jogador = df[df["Jogador"] == nome_jogador].copy()

    if df_jogador.empty:
        print(f"Jogador {nome_jogador} não encontrado no arquivo CSV!")
        return None, None, None

    df_jogador[['Pontos', 'Rebotes', 'Assistências']] = df_jogador[['Pontos', 'Rebotes', 'Assistências']].apply(pd.to_numeric)

    moda_pontos = df_jogador['Pontos'].mode()[0]
    moda_rebotes = df_jogador['Rebotes'].mode()[0]
    moda_assistencias = df_jogador['Assistências'].mode()[0]

    print(f"📊 Moda de {nome_jogador}:")
    print(f"   🔸 Moda de pontos: {moda_pontos}")
    print(f"   🔸 Moda de rebotes: {moda_rebotes}")
    print(f"   🔸 Moda de assistências: {moda_assistencias}")
    print("-" * 40)

    return moda_pontos, moda_rebotes, moda_assistencias


def calcular_frequencia_moda(nome_jogador, moda_pontos, moda_rebotes, moda_assistencias, arquivo_csv):
    df = pd.read_csv(arquivo_csv)

    df_jogador = df[df["Jogador"] == nome_jogador].copy()

    if df_jogador.empty:
        print(f"Jogador {nome_jogador} não encontrado no arquivo CSV!")
        return None, None, None

    df_jogador[['Pontos', 'Rebotes', 'Assistências']] = df_jogador[['Pontos', 'Rebotes', 'Assistências']].apply(pd.to_numeric)

    freq_pontos = (df_jogador['Pontos'] == moda_pontos).sum()
    freq_rebotes = (df_jogador['Rebotes'] == moda_rebotes).sum()
    freq_assistencias = (df_jogador['Assistências'] == moda_assistencias).sum()

    print(f"📊 Frequência da Moda de {nome_jogador}:")
    print(f"   🔹 A moda de pontos ({moda_pontos}) aparece {freq_pontos} vezes")
    print(f"   🔹 A moda de rebotes ({moda_rebotes}) aparece {freq_rebotes} vezes")
    print(f"   🔹 A moda de assistências ({moda_assistencias}) aparece {freq_assistencias} vezes")
    print("-" * 40)


def calcular_percentual_abaixo_da_moda(nome_jogador, moda_pontos, moda_rebotes, moda_assistencias, arquivo_csv):
    df = pd.read_csv(arquivo_csv)

    df_jogador = df[df["Jogador"] == nome_jogador].copy()

    if df_jogador.empty:
        print(f"Jogador {nome_jogador} não encontrado no arquivo CSV!")
        return None, None, None

    df_jogador[['Pontos', 'Rebotes', 'Assistências']] = df_jogador[['Pontos', 'Rebotes', 'Assistências']].apply(pd.to_numeric)

    perc_pontos = (df_jogador['Pontos'] < moda_pontos).mean() * 100
    perc_rebotes = (df_jogador['Rebotes'] < moda_rebotes).mean() * 100
    perc_assistencias = (df_jogador['Assistências'] < moda_assistencias).mean() * 100

    print(f"📊 Percentual de Jogos Abaixo da Moda - {nome_jogador}:")
    print(f"   🔹 Pontos: {perc_pontos:.2f}% dos jogos")
    print(f"   🔹 Rebotes: {perc_rebotes:.2f}% dos jogos")
    print(f"   🔹 Assistências: {perc_assistencias:.2f}% dos jogos")
    print("-" * 40)


def calcular_desvio_padrao_jogador(nome_jogador, arquivo_csv):
    df = pd.read_csv(arquivo_csv)

    df_jogador = df[df["Jogador"] == nome_jogador].copy()

    if df_jogador.empty:
        print(f"Jogador {nome_jogador} não encontrado no arquivo CSV!")
        return None, None, None

    df_jogador[['Pontos', 'Rebotes', 'Assistências']] = df_jogador[['Pontos', 'Rebotes', 'Assistências']].apply(pd.to_numeric)

    desvio_pontos = df_jogador['Pontos'].std()
    desvio_rebotes = df_jogador['Rebotes'].std()
    desvio_assistencias = df_jogador['Assistências'].std()

    print(f"📊 Desvio Padrão - {nome_jogador}:")
    print(f"   🔹 Pontos: {desvio_pontos:.2f}")
    print(f"   🔹 Rebotes: {desvio_rebotes:.2f}")
    print(f"   🔹 Assistências: {desvio_assistencias:.2f}")
    print("-" * 40)


def obter_estatisticas_de_toda_a_carreira(id_jogador):
    dados_da_carreira = playercareerstats.PlayerCareerStats(player_id=id_jogador)
    return dados_da_carreira.get_data_frames()[0]
