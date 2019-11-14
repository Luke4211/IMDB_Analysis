# -*- coding: utf-8 -*-
"""
  IMDBanalyze.py ~ Contains functions for network analysis on
  the IMDB graph. Reads IMDB graph from adjacency
  list file, and reads reference data from .csv files

  @author: Lucas Gorski
"""

import networkx as nx

G = nx.read_adjlist('luck/Adj_list.txt')

print(nx.shortest_path(G, 'nm6119929', 'nm0438471'))

