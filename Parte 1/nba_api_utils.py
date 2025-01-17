from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguestandings
import pandas as pd


CONFERENCIAS = {
    "east": [
        "Massachusetts", "New York", "Pennsylvania", "Maryland", "Georgia",
        "Florida", "Indiana", "Michigan", "Illinois", "Ohio", "Wisconsin",
        "Ontario", "District of Columbia", "North Carolina"
    ],
    "west": [
        "California", "Oregon", "Washington", "Arizona", "Colorado", "Utah",
        "Texas", "Oklahoma", "Minnesota", "Louisiana", "Tennessee"
    ]
}

def resgatar_times():
    times = teams.get_teams()
    return pd.DataFrame(times)

def resgatar_times_por_temporada(temporada):
    times = leaguestandings.LeagueStandings(season=temporada).get_data_frames()[0]
    return pd.DataFrame(times)

def dividir_por_conferencia(data_set):
    leste = data_set[data_set['Conference'] == "East"]['TeamName'].tolist()
    oeste = data_set[data_set['Conference'] == "West"]['TeamName'].tolist()

    max_length = max(len(leste), len(oeste))
    tabela_conferencias = pd.DataFrame({
        "Conferência Leste": leste + [None] * (max_length - len(leste)),
        "Conferência Oeste": oeste + [None] * (max_length - len(oeste))
    })

    return tabela_conferencias

def resgatar_times_dividos_por_conferencia():
    data_set = resgatar_times_por_temporada("2024-25")
    return dividir_por_conferencia(data_set)

def obter_time(nome):
    times = resgatar_times()
    return times[times['full_name'] == nome].iloc[0]

def salvar_dataset_csv(data_set, path):
    data_set.to_csv(path, index=False)

def classificar_por_vitorias(data_set):
    data_set_ordenado = data_set.sort_values(by="WINS", ascending=False)

    leste = data_set_ordenado[data_set_ordenado['Conference'] == "East"]
    oeste = data_set_ordenado[data_set_ordenado['Conference'] == "West"]

    max_length = max(len(leste), len(oeste))

    leste = leste[['TeamName', 'WINS']].reset_index(drop=True)
    oeste = oeste[['TeamName', 'WINS']].reset_index(drop=True)

    leste = leste.reindex(range(max_length), fill_value={'TeamName': '', 'WINS': 0})
    oeste = oeste.reindex(range(max_length), fill_value={'TeamName': '', 'WINS': 0})

    tabela_conferencias = pd.concat([leste, oeste], axis=1)
    tabela_conferencias.columns = pd.MultiIndex.from_tuples([
        ("Conferência Leste", "TeamName"),
        ("Conferência Leste", "WINS"),
        ("Conferência Oeste", "TeamName"),
        ("Conferência Oeste", "WINS"),
    ])

    return tabela_conferencias

def resgatar_clissificao_atual():
    times = resgatar_times_por_temporada("2024-25")
    return classificar_por_vitorias(times)