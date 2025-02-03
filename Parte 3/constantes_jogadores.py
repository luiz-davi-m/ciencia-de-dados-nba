from nba_api_utils import obter_time

NOME_TIME = 'Denver Nuggets'
time = obter_time(NOME_TIME)
TIME_ID = time['id']

JOGADOR_1 = 'Nikola Jokić'
JOGADOR_2 = 'Michael Porter Jr.'
JOGADOR_3 = 'Jamal Murray'

JOGADORES = [JOGADOR_1, JOGADOR_2, JOGADOR_3]

TEMPORADA_ATUAL = '2024-25'

RESULTADOS_PATH = '../resultados/parte_3'