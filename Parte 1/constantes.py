from nba_api_utils import obter_time

NOME_TIME = 'Denver Nuggets'
time = obter_time(NOME_TIME)
TIME_ID = time['id']

TEMPORADA_ANTERIOR = '2023-24'
TEMPORADA_ATUAL = '2024-25'

JOGADOR_1 = 'Nikola Jokic'
JOGADOR_2 = 'Michael Porter Jr'
JOGADOR_3 = 'Jamal Murray'

RESULTADOS_PATH = '../resultados'