from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamgamelog
import pandas as pd

def salvar_dataset_csv(data_set, path):
    data_set.to_csv(path, index=False)


def get_team_info(team_name):
    all_teams = teams.get_teams()
    for team in all_teams:
        if team_name.lower() in team['full_name'].lower():
            return {'id': team['id'], 'nome': team['full_name'], 'sigla': team['abbreviation']}
    return None

def calcular_jogos_casa_fora(oponente, temporada):
    denver_nuggets = get_team_info("Denver Nuggets")
    oponente_info = get_team_info(oponente['nome'])

    if not denver_nuggets or not oponente_info:
        print("Erro ao obter informações dos times.")
        return

    game_log = teamgamelog.TeamGameLog(team_id=denver_nuggets['id'], season=temporada).get_data_frames()[0]

    sigla_oponente = oponente_info['sigla']
    jogos_vs_oponente = game_log[game_log["MATCHUP"].str.contains(f"DEN vs. {sigla_oponente}|DEN @ {sigla_oponente}")]

    jogos_casa = jogos_vs_oponente[jogos_vs_oponente["MATCHUP"].str.startswith(f"DEN vs.")].shape[0]
    jogos_fora = jogos_vs_oponente[jogos_vs_oponente["MATCHUP"].str.startswith(f"DEN @")].shape[0]

    # Exibir os resultados
    print(f"\n🆚 Contra {oponente_info['nome']} ({sigla_oponente}):")
    print(f"🏠 Jogos em casa: {jogos_casa}")
    print(f"🛫 Jogos fora de casa: {jogos_fora}")
