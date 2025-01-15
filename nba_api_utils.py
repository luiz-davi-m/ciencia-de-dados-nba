from nba_api.stats.static import teams
import pandas as pd

def resgatar_times():
    times = teams.get_teams()
    return pd.DataFrame(times)

def obter_time(nome):
    times = resgatar_times()
    return times[times['full_name'] == nome].iloc[0]

times = resgatar_times()
nome_do_time = "Denver Nuggets"
time = obter_time(nome_do_time)
print(time)