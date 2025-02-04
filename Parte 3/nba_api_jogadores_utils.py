from scipy.stats import gumbel_r, gumbel_l
from nba_api.stats.static import players
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os


def buscar_id_jogador(nome_jogador):
    jogadores = players.get_players()
    dicionario_jogadores = next((jogador for jogador in jogadores if jogador['full_name'] == nome_jogador), None)
    if dicionario_jogadores:
        return dicionario_jogadores['id']
    return None


def get_player_data(csv_path):
    df = pd.read_csv(csv_path)

    required_columns = ['PTS', 'REB', 'AST']
    if not all(column in df.columns for column in required_columns):
        raise ValueError(f"O arquivo CSV deve conter as colunas: {required_columns}")

    return df[required_columns]


def fit_gumbel(data, extreme_type='max'):
    if extreme_type == 'max':
        loc, scale = gumbel_r.fit(data)
    elif extreme_type == 'min':
        loc, scale = gumbel_l.fit(data)
    else:
        raise ValueError("extreme_type deve ser 'max' ou 'min'")
    
    return loc, scale


def calculate_probabilities(loc, scale, x):
    prob_above_x = 1 - gumbel_r.cdf(x, loc=loc, scale=scale)  # P(Y > x)
    prob_exceed_or_equal_x = 1 - gumbel_r.cdf(x - 1, loc=loc, scale=scale)  # P(Y >= x)
    prob_below_or_equal_x = gumbel_r.cdf(x, loc=loc, scale=scale)  # P(Y <= x)
    prob_below_x = gumbel_r.cdf(x - 1, loc=loc, scale=scale)  # P(Y < x)

    return {
        'Probabilidade de marcar acima de X': prob_above_x,
        'Probabilidade de atingir ou exceder X': prob_exceed_or_equal_x,
        'Probabilidade de atingir ou ficar abaixo de X': prob_below_or_equal_x,
        'Proporção de valores menores ou iguais a X': prob_below_or_equal_x,
        'Proporção de valores menores que X': prob_below_x
    }


def plot_results(data, loc, scale, x, stat_name, jogador):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(f'Análise de Extremos para {stat_name} - {jogador}', fontsize=16)

    sns.histplot(data, kde=False, stat='density', ax=axes[0, 0], color='blue', label='Dados')
    x_values = np.linspace(min(data), max(data), 1000)
    pdf_values = gumbel_r.pdf(x_values, loc=loc, scale=scale)
    axes[0, 0].plot(x_values, pdf_values, 'r-', label='Gumbel Ajustada')
    axes[0, 0].set_title('Histograma com Distribuição de Gumbel')
    axes[0, 0].legend()

    sns.kdeplot(data, ax=axes[0, 1], color='blue', label='Dados')
    axes[0, 1].plot(x_values, pdf_values, 'r-', label='Gumbel Ajustada')
    axes[0, 1].set_title('Densidade de Probabilidade')
    axes[0, 1].legend()

    cdf_values = gumbel_r.cdf(x_values, loc=loc, scale=scale)
    axes[1, 0].plot(x_values, cdf_values, 'g-', label='CDF de Gumbel')
    axes[1, 0].axvline(x=x, color='black', linestyle='--', label=f'X = {x}')
    axes[1, 0].set_title('Probabilidade Acumulada (CDF)')
    axes[1, 0].legend()

    probs = calculate_probabilities(loc, scale, x)
    labels = list(probs.keys())
    values = list(probs.values())
    axes[1, 1].bar(labels, values, color='orange')
    axes[1, 1].set_title('Probabilidades Calculadas')
    axes[1, 1].tick_params(axis='x', rotation=45)

    plt.tight_layout()

    output_path = f"../resultados/parte_3/graficos/ocorrencia_{stat_name}_{jogador}.png"
    plt.savefig(output_path)
    plt.tight_layout()
    plt.show()
    plt.close(fig)

def analyze_player(csv_path, x_pts, x_reb, x_ast, jogador):
    data = get_player_data(csv_path)

    loc_pts, scale_pts = fit_gumbel(data['PTS'], extreme_type='max')
    loc_reb, scale_reb = fit_gumbel(data['REB'], extreme_type='max')
    loc_ast, scale_ast = fit_gumbel(data['AST'], extreme_type='max')

    results_pts = calculate_probabilities(loc_pts, scale_pts, x_pts)
    results_reb = calculate_probabilities(loc_reb, scale_reb, x_reb)
    results_ast = calculate_probabilities(loc_ast, scale_ast, x_ast)

    results = {
        'Pontos': results_pts,
        'Rebotes': results_reb,
        'Assistências': results_ast
    }

    for stat, values in results.items():
        print(f"\n{stat}:")
        for question, answer in values.items():
            print(f"{question}: {answer:.4f}")


    plot_results(data['PTS'], loc_pts, scale_pts, x_pts, 'Pontos', jogador)
    plot_results(data['REB'], loc_reb, scale_reb, x_reb, 'Rebotes', jogador)
    plot_results(data['AST'], loc_ast, scale_ast, x_ast, 'Assistências', jogador)
