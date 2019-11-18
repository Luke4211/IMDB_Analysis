# -*- coding: utf-8 -*-
"""
  Inf_max.py ~ Implementation of the CELF influence max
  algorithm.
  
  Specifically, open source code for these algorithms was found at
  http://ethen8181.github.io/machine-learning/networkx/max_influence/max_influence.html#Spread-Process---Independent-Cascade-(IC)
  
  Code adapted to work with networkx by Lucas Gorski
"""

import numpy as np
import networkx as nx
import time
import heapq

def celf(graph, k, prob, iters=1000):
  start_time = time.time()
  
  gains = []
  for node in range(graph.number_of_nodes()):
    spread = independent_cascade(graph, [node], prob, iters)
    heapq.heappush(gains, (-spread, node))
    
  spread, node = heapq.heappop(gains)
  solution = [node]
  spread = -spread
  spreads = [spread]
  
  lookups = [graph.number_of_nodes()]
  
  elapsed = [round(time.time() - start_time, 3)]
  
  for _ in range(k-1):
    node_lookup = 0
    match = False
    
    while not match:
      node_lookup += 1
      
      _, current_node = heapq.heappop(gains)
      spread_gain = (independent_cascade(graph, solution + [current_node], prob, iters) - spread)
      
      heapq.heappush(gains, (-spread_gain, current_node))
      match = (gains[0][1] == current_node)
      
    spread_gain, node = heapq.heappop(gains)
    spread -= spread_gain
    solution.append(node)
    spreads.append(spread)
    lookups.append(node_lookup)

    elapse = round(time.time() - start_time, 3)
    elapsed.append(elapse)

  return solution, spreads, elapsed, lookups

                                       

def independent_cascade(graph, seed, prob, iters=1000):
  total_spread = 0
  
  
  for i in range(iters):
    np.random.seed(i)
    active = seed[:]
    new_active = seed[:]
    
    while new_active:
      activated_nodes = []
      # For each node in new_active, try to influence neighbors
      for node in new_active:
        
        # Grab the node's neighbors, and randomly draw a value between
        # 0.0 and 1.0. If the value is less than prob, we have
        # influenced the node. Add influenced nodes to activated_nodes
        neighbors = list(nx.all_neighbors(graph, str(node)))
        success = (np.random.uniform(0, 1, len(neighbors)) < prob)
        activated_nodes += list(np.extract(success, neighbors))
        
      # Setminus operation ensures no duplicate nodes occur in active
      new_active = list(set(activated_nodes) - set(active))
      active += new_active
      
    total_spread += len(active)
    
  return total_spread / iters

                                  