from nba_api_time_utils import obter_time

NOME_TIME = 'Denver Nuggets'
time = obter_time(NOME_TIME)
TIME_ID = time['id']

TEMPORADA_ANTERIOR = '2023-24'
TEMPORADA_ATUAL = '2024-25'

RESULTADOS_PATH = '../resultados/parte_1'