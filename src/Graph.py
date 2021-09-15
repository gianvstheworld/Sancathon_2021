''' Conjunto de códigos desenvolvidos para o Sancathon 2021
                                > GRABus <
* Código de controle do tráfego:
        O objetivo do desenvolvimento desse código em python é gerar grafos
    representando os pontos de ônibus e as linhas que ligam um ao outro.
    É válido lembrar que todos os códigos do projeto são versões betas que
    podem ser aperfeiçoados e mais explorados em outros escopos fora do Sancathon.
        Os grafos tem o objetivo de auxiliar na visualização da atual situação dos
    ônibus, levando em conta o fluxo de pessoas por ônibus e a cada período de tempo,
    representados pelas diferentes cores de arestas nos grafos.
'''


# Imports
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def plot_graph_with_coordinates(g, weight_name, pos=None):

    plt.figure(figsize=(20, 10))

    # Verifica se as coordenadas reais serão utilizadas

    if pos:
        plt.xlim([-0.2, 1.2])
        plt.ylim([-0.2, 1.2])
    else:
        pos = nx.spring_layout(g)

    edges = g.edges()
    d = dict(g.degree)

    options = {
        "node_color": "#A0CBE2",
        "width": 2,
        "with_labels": True,
    }

    weights = [g[u][v][weight_name] for u, v in edges]
    colors = []
    for w in weights:
        if w <= 0.3:
            colors.append("green")
        elif w > 0.3 and w <= 0.7:
            colors.append("#FFCC00")
        else:
            colors.append("red")

    # Desenha o grafo
    nx.draw(g, pos, nodelist=list(d.keys()),
            node_size=[v * 500 for v in d.values()], edge_color=colors, **options)

    plt.show()


def main():

    # Exemplo
    d_location = {'Stations': ['1','2','3','4','5','6','7'] ,
        'Latitude':[0.320687, 0.369927, 0.014087, 0.299441, 0.068567, 0.161801, 0.084923] ,
        'Longitude':[0.504865, 0.250951, 0.589596, 0.057862, 0.248278, 0.690536, 0.476913]
        }

    d_weight = {'Station_origin': ['1','2','3','4','5','6','4','2','3','7','5'] ,
        'Station_destiny':['2','3','1','1','1','3','7','5','4','5','6'] ,
        'Weight':list(np.random.random(11))
        }

    location_df = pd.DataFrame.from_dict(d_location)
    weight_df = pd.DataFrame.from_dict(d_weight)

    # Get edge_list
    #df = pd.read_csv('Stations_positions.csv')
    #df = df.replace(',','.', regex=True)

    # Converte as strings para valores numéricos
    weight_df['Weight'] = pd.to_numeric(weight_df['Weight'])
    location_df['Latitude'] = pd.to_numeric(location_df['Latitude'])
    location_df['Longitude'] = pd.to_numeric(location_df['Longitude'])

    g_df = weight_df

    pos_lat = location_df['Latitude'].to_list()
    pos_long = location_df['Longitude'].to_list()

    # Normaliza as coordenadas
    max_lat = max(pos_lat)
    min_lat = min(pos_lat)
    max_long = max(pos_long)
    min_long = min(pos_long)

    pos_lat_norm = [(x-min_lat)/(max_lat-min_lat) for x in pos_lat]
    pos_long_norm = [(x-min_long)/(max_long-min_long) for x in pos_long]

    stations = location_df['Stations']

    pos = dict(zip(stations, zip(pos_lat_norm, pos_long_norm)))

    # Cria o grafo
    g = nx.from_pandas_edgelist(g_df, 'Station_origin', 'Station_destiny', edge_attr=['Weight'], create_using=nx.DiGraph())

    plot_graph_with_coordinates(g, 'Weight', pos)


# Executa a função main
if __name__ == '__main__':
    main()