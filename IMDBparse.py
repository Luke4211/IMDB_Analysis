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
  basics = open("title.basics.test.tsv", "r", encoding='utf-8')
  
  # Read lines of file into titles
  titles = basics.readlines()
  
  # Since first line in file is column names,
  # remove it
  del(titles[0])
  
  # Create empty dictionary to fill with values
  # Key: the title's unique ID.
  # Value: a list containing the name of the title
  #        and a list of actors which appear in it.
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
  name_map = read_names()
  principals = open("title.principals.test.tsv", "r", encoding='utf-8')
  
  
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
     
      # Check if person_id exists in name_map. 
      # If it does not, do nothing.
      person_id = values[2]
      if person_id in name_map:
        # Reference name_map by the person_id 
        # to retrive actor's name. 
        # Append name to actor_list in the 
        # basic_map at key title_id
        name = name_map[person_id][0]
        basic_map[title_id][1].append(name)
        
        #Append title_id to the actor's movie list
        name_map[person_id][1].append(title_id)

  return [basic_map, name_map]

def read_names():
  names = open("name.basics.test.tsv", "r", encoding='utf-8')
  
  entries = names.readlines()
  
  # Remove column names
  del(entries[0])
  
  # Initialize name_map to empty dictionary
  # Key: the person's unique ID
  # Value: list containing their name and a list
  #        containing all titles they appear in
  #        (Note: title list will be empty upon return)
  name_map = {}
  
  # Loop through entries for actors, and append
  # their name to name_map at key person_id
  for entry in entries:
    
    values = entry.split("\t")
    person_id = values[0]
    name_map[person_id] = [values[1], []]
    
  
    
  return name_map
    

basic_map, name_map = read_principals()

print(basic_map["tt0829482"])
print(name_map["nm1706767"])

