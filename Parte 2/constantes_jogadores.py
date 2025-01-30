from nba_api_jogadores_utils import buscar_id_jogador
from nba_api_utils import obter_time

NOME_TIME = 'Denver Nuggets'
time = obter_time(NOME_TIME)
TIME_ID = time['id']

JOGADOR_1 = 'Nikola Jokić'
JOGADOR_2 = 'Michael Porter Jr.'
JOGADOR_3 = 'Jamal Murray'

JOGADOR_1_ID = buscar_id_jogador(JOGADOR_1)
JOGADOR_2_ID = buscar_id_jogador(JOGADOR_2)
JOGADOR_3_ID = buscar_id_jogador(JOGADOR_3)

JOGADORES = [JOGADOR_1, JOGADOR_2, JOGADOR_3]

TEMPORADA_ATUAL = '2024-25'

RESULTADOS_PATH = '../resultados/parte_2'