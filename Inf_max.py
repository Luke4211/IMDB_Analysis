# -*- coding: utf-8 -*-
"""
  Inf_max.py ~ Implementation of the Cost Effective Lazy Forwarding
  (CELF) influence maximization algorithm.
  
  Specifically, open source code for these algorithms was found at
  http://ethen8181.github.io/machine-learning/networkx/max_influence/max_influence.html
  
  Further reading on CEFL algorithm: 
  https://www.openu.ac.il/personal_sites/moran-feldman/publications/Handbook2018.pdf
  
  Algorithm adapted to work with networkx by Lucas Gorski
"""

import numpy as np
import networkx as nx
import time
import heapq

# Cost Effective Lazy Forwarding algorithm to approximate
# maximal influencers.
def celf(graph, k, prob, iters=1000):
  start_time = time.time()
  
  # Use greedy algorithm to compute first maximally influential node
  gains = []
  for node in nx.nodes(graph):
    spread = independent_cascade(graph, [node], prob, iters)
    # (spread is negated because heapq is a minheap)
    heapq.heappush(gains, (-spread, node))
    
  spread, node = heapq.heappop(gains)
  solution = [node]
  spread = -spread
  spreads = [spread]
  
  lookups = [graph.number_of_nodes()]
  
  elapsed = [round(time.time() - start_time, 3)]
  
  # Since we already calculated the most influential node above
  # using the greedy algorithm, calculate the rest of the k-1
  # maximally influential nodes.
  for _ in range(k-1):
    node_lookup = 0
    match = False
    
    while not match:
      node_lookup += 1
      
      # grab the next lowest (highest) spread node from minheap
      # compute it's gain and subtract the current highest spread from it
      _, current_node = heapq.heappop(gains)
      spread_gain = (independent_cascade(graph, solution + [current_node], prob, iters) - spread)
      
      # If the previous top node remains on top, set match to
      # true to break out of while loop
      heapq.heappush(gains, (-spread_gain, current_node))
      match = (gains[0][1] == current_node)
    
    # Append previous top node and it's respective
    # information to return lists.
    spread_gain, node = heapq.heappop(gains)
    spread -= spread_gain
    solution.append(node)
    spreads.append(spread)
    lookups.append(node_lookup)
    
    elapse = round(time.time() - start_time, 3)
    elapsed.append(elapse)

  return solution, spreads, elapsed, lookups

                                       
# Compute the average "spread" for a set of nodes "seed"
def independent_cascade(graph, seed, prob, iters=1000):
  total_spread = 0
  
  # Compute spread iters many times
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
      
    # Add to total_spread the number of nodes influenced
    total_spread += len(active)
    
  # Calculate average nodes influenced over all iterations
  return total_spread / iters

                                  
