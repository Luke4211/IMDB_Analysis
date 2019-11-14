# -*- coding: utf-8 -*-
"""
IMDBparse.py ~ Contains functions for parsing the
Internet Movie Database (IMDB)

@author Lucas Gorski
"""

# Reads title.basics.tsv,
# stores as dict {title_id :[movie_name, actor_list]}
# (note actor_list will be empty upon return)
# return dict
def read_basics():
  basics = open("title.basics.tsv", "r", encoding='utf-8')
  
  # Read lines of file into titles
  titles = basics.readlines()
  
  # Since first line in file is column names,
  # remove it
  del(titles[0])
  
  # Create empty dictionary to fill with values
  # Key: the title's unique ID.
  # Value: the name of the title.
  title_map = {}
  
  # Loop through lines, and add key,value
  # pairs to title_map
  for entry in titles:
    
    # Split string by TAB character into
    # indivudual value fields.
    values = entry.split("\t")
    
    #values[0] corresponds to title_id.
    # Append the name of movie 
    #(values[2]) using title_id as 
    # key to title_map
    
    title_id = values[0]
    title_map[title_id] = [values[2], [] ]
    
  return title_map
  

def read_principals():
  basic_map = read_basics()
  principals = open("title.principals.tsv", "r", encoding='utf-8')
  name_map = read_names()
  
  # Read lines of file into entries
  entries = principals.readlines()
  
  # Remove column names
  del(entries[0])
  
  for entry in entries:
    
    # See readBasics() for explanation
    values = entry.split("\t")
    title_id = values[0]
    
    
    # Check if title_id exists in basic map.
    # If it exists, update record. Otherwise do nothing.
    # (Intuitively you would assume it does,
    # but as of 11/13/2019 there are 164 title_id's
    # present in title.principals.tsv that are not
    # present in title.basics.tsv)
    if title_id in basic_map:
      # Reference name_map by the person_id 
      # to retrive actor's name. Check
      # if person_id exists in name_map, and if so
      # append to actor_list in the basic_map at key title_id
      person_id = values[2]
      if person_id in name_map:
        name = name_map[person_id]
        basic_map[title_id][1].append(name)
    return basic_map

def read_names():
  names = open("name.basics.tsv", "r", encoding='utf-8')
  
  entries = names.readlines()
  
  # Remove column names
  del(entries[0])
  
  # Initialize name_map to empty dictionary
  # Key: the person's unique ID
  # Value: the person's name
  name_map = {}
  
  for entry in entries:
    
    values = entry.split("\t")
    person_id = values[0]
    name_map[person_id] = values[1]
    
  return name_map
    
"""
test = read_principals()

print(test["tt0000001"])
"""
