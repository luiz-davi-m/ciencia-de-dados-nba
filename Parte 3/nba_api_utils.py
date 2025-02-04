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

