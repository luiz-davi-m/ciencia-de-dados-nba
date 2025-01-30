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