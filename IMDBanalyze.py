# -*- coding: utf-8 -*-
"""
  IMDBanalyze.py ~ Contains functions for network analysis on
  the IMDB graph. Reads IMDB graph from adjacency
  list file, and reads reference data from .csv files
  
  (work in progress)
  @author: Lucas Gorski
"""

import csv
import networkx as nx
from networkx.algorithms.smallworld import sigma

def analyze_graph(directory_name):
  graph_pkg = package_graph(directory_name)
  graph = graph_pkg[0]
  title_map = graph_pkg[1]
  name_map = graph_pkg[2]
  
  #print("Closeness: " + nx.closeness_centrality(graph))
  print("Clustering Coefficient: " + str(nx.average_clustering(graph)))
  print("Density: " + str(nx.density(graph)))
  print("Small Word (sigma): " + str(sigma(graph)))
  
def package_graph(directory_name):
  graph = nx.read_adjlist(directory_name + "/Adj_list.txt")
  title_map, name_map = read_maps(directory_name)
  
  return [graph, title_map, name_map]

# Reads in title and name maps from specified directory,
# returns a list containing each map
def read_maps(directory_name):
  title_map_file = open(directory_name + "/Title_map.csv", "r", encoding='utf-8')
  name_map_file = open(directory_name + "/Name_map.csv", "r", encoding='utf-8')
  
  # Pass map files to csv readers
  title_reader = csv.reader(title_map_file)
  name_reader = csv.reader(name_map_file)
  
  # Construct dictionaries from the csv readers
  title_map = {val[0]:val[1] for val in title_reader}
  name_map = {val[0]:val[1] for val in name_reader}
  
  title_map_file.close()
  name_map_file.close()
  
  return [title_map, name_map]

analyze_graph("test2")

