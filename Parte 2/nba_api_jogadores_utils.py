from nba_api.stats.endpoints import commonplayerinfo, playergamelog
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




