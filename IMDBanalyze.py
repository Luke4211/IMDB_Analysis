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
import Inf_max as im
from networkx.algorithms.smallworld import sigma

def analyze_graph(directory_name):
  graph_pkg = package_graph(directory_name)
  graph = graph_pkg[0]
  title_map = graph_pkg[1]
  name_map = graph_pkg[2]
  
  #print("Closeness: " + nx.closeness_centrality(graph))
  print("Average Clustering Coefficient: " + str(nx.average_clustering(graph)))
  print("Density: " + str(nx.density(graph)))
  
  influence_max(graph, 5, title_map, name_map)
  
  
# Prints out maximally influential actors/movies.
def influence_max(graph, num_select, title_map, name_map, prob=.1):
  sol, spread, elapsed, lookup = im.celf(graph, num_select, prob)
  
  for node in sol:
    if node in name_map:
      print("One of the maximally influential actors: " + str(name_map[node]))
    else:
      print("One of the maximally influential movies: " + str(title_map[node]))
      
  print("Time elapsed since inf_max calculation began: " + str(elapsed))
  
  
# Calculates small world sigma value for each of the
# graph's subcomponents. 
# NOTE: Due to the size of the network, it is unlikely
# this function will complete as it is very computationally
# expensive. Try to cull graph to ratings over 200,000 if you
# attempt to use this method
def small_world(graph, title_map, name_map):
  # Split graph into it's disconnected components
  components = nx.connected_component_subgraphs(graph)
  
  # Calculate small world sigma value for each component
  for subgraph in components:
    node = list(subgraph.nodes)[0]
    if node in title_map:
      title = title_map[node][0]
      print("A movie contained in component: " + title)
      print("Small Word (sigma) for " + title + " : " + str(sigma(subgraph)))
      
    else:
      name = name_map[node]
      print("An actor contained in component: " + name)
      print("Small Word (sigma) for " + name + " : " + str(sigma(subgraph)))
  
# Read graph from file, and return a list containing
# the graph and the reference maps returned by read_maps
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
  title_map = {val[0]:[val[1], val[2], val[3]] for val in title_reader}
  name_map = {val[0]:val[1] for val in name_reader}
  
  title_map_file.close()
  name_map_file.close()
  
  return [title_map, name_map]

#analyze_graph("test")

