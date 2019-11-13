# -*- coding: utf-8 -*-
"""
IMDBgraph.py ~ Contains functions for parsing the
Internet Movie Database (IMDB) and 
"""

#Reads title.basics.tsv,
#stores as dict {title_id : movie_name}
#return dict
def readBasics():
  basics = open("title.basics.tsv", "r", encoding='utf-8')
  
  #Read lines of file into titles
  titles = basics.readlines()
  
  #Since first line in file is column names,
  #remove it
  del(titles[0])
  
  #Create empty dictionary to fill with values
  #Key: title_ID
  #Value: title_string
  title_map = {}
  for entry in titles:
    
    #Split string by TAB character into
    #indivudual value fields.
    values = entry.split("\t")
    
    #values[0] corresponds to title_id.
    #Since title_id starts with "tt", we
    #use the slice operator [2:] to remove
    #these characters, then append the name
    #of movie (values[2]) using title_id[2:] as 
    #key to title_map
    
    title_id = int((values[0][2:]))
    title_map[title_id] = values[2]
    
  return title_map
  

test = readBasics()

print(test[67])