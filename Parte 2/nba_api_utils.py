from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamgamelog
import pandas as pd

def resgatar_times():
    times = teams.get_teams()
    return pd.DataFrame(times)

def obter_time(nome):
    times = resgatar_times()
    return times[times['full_name'] == nome].iloc[0]

def salvar_dataset_csv(data_set, path):
    data_set.to_csv(path, index=False)

def obter_informacoes_do_time(team_name):
    all_teams = teams.get_teams()
    for team in all_teams:
        if team_name.lower() in team['full_name'].lower():
            return {'id': team['id'], 'nome': team['full_name'], 'sigla': team['abbreviation']}
    return None

def calcular_jogos_casa_fora(nome_time_analisado, oponente, temporada):
    time_analisado = obter_informacoes_do_time(nome_time_analisado)
    oponente_info = obter_informacoes_do_time(oponente['nome'])

    if not time_analisado or not oponente_info:
        print("Erro ao obter informações dos times.")
        return

    game_log = teamgamelog.TeamGameLog(team_id=time_analisado['id'], season=temporada).get_data_frames()[0]

    sigla_time_analisado = time_analisado['sigla']
    sigla_oponente = oponente_info['sigla']
    jogos_vs_oponente = game_log[game_log["MATCHUP"].str.contains(f"{sigla_time_analisado} vs. {sigla_oponente}|{sigla_time_analisado} @ {sigla_oponente}")]

    jogos_casa = jogos_vs_oponente[jogos_vs_oponente["MATCHUP"].str.startswith(f"{sigla_time_analisado} vs.")].shape[0]
    jogos_fora = jogos_vs_oponente[jogos_vs_oponente["MATCHUP"].str.startswith(f"{sigla_time_analisado} @")].shape[0]

    # Exibir os resultados
    print(f"\n🆚 Contra {oponente_info['nome']} ({sigla_oponente}):")
    print(f"🏠 Jogos em casa: {jogos_casa}")
    print(f"🛫 Jogos fora de casa: {jogos_fora}")