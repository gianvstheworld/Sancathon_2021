# Imports
import pandas as pd
import numpy as np
import networkx as nx

# Test function

def plot_graph(G, weight_name=None):
    '''
    G: a networkx G
    weight_name: name of the attribute for plotting edge weights (if G is weighted)
    '''

    import matplotlib.pyplot as plt

    plt.figure()
    pos = nx.spring_layout(G)
    edges = G.edges()
    weights = None

    if weight_name:
        weights = [int(G[u][v][weight_name]) for u, v in edges]
        labels = nx.get_edge_attributes(G, weight_name)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.drawing.nx_pylab.draw_networkx(G, pos, edgelist=edges)
    else:
        nx.draw_networkx(G, pos, edgelist=edges)
# Test

# Get edge_list
G_df = pd.read_csv('Stations_data.csv')

G = nx.from_pandas_edgelist(G_df, 'Station_origin', 'Station_destiny', edge_attr=['Weight'], create_using=nx.DiGraph())

plot_graph(G, 'Weight')

# Real function
def plot_graph_with_coordinates(G, pos, weight_name=None):
    '''
    G: a networkx G
    weight_name: name of the attribute for plotting edge weights (if G is weighted)
    '''
    import matplotlib.pyplot as plt

    plt.figure(figsize=(20, 10))
    plt.xlim([-0.2, 1.2])
    plt.ylim([-0.2, 1.2])
    edges = G.edges()
    weights = None

    if weight_name:
        weights = [int(G[u][v][weight_name]) for u, v in edges]
        labels = nx.get_edge_attributes(G, weight_name)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.drawing.nx_pylab.draw_networkx(G, pos, edgelist=edges)
    else:
        nx.draw_networkx(G, pos, edgelist=edges)

# Get edge_list
df = pd.read_csv('Stations_positions.csv')
df = df.replace(',','.', regex=True)
df['Weight'] = pd.to_numeric(df['Weight'])
df['Latitude'] = pd.to_numeric(df['Latitude'])
df['Longitude'] = pd.to_numeric(df['Longitude'])

G_df = df.drop(['Latitude', 'Longitude'], axis=1)

pos_lat = df['Latitude'].to_list()
pos_long = df['Longitude'].to_list()

# Normalizing the coordinates
max_lat = max(pos_lat)
min_lat = min(pos_lat)
max_long = max(pos_long)
min_long = min(pos_long)

pos_lat_norm = [(x - min_lat)/(max_lat - min_lat) for x in pos_lat]
pos_long_norm = [(x - min_long)/(max_long - min_long) for x in pos_long]

stations = df['Station_origin']

pos = dict(zip(stations, zip(pos_lat_norm, pos_long_norm)))

G = nx.from_pandas_edgelist(G_df, 'Station_origin', 'Station_destiny', edge_attr=['Weight'], create_using=nx.DiGraph())

plot_graph_with_coordinates(G, pos, 'Weight')