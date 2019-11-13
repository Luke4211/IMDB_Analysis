# -*- coding: utf-8 -*-
"""
IMDBparse.py ~ Contains functions for parsing the
Internet Movie Database (IMDB)
"""

#Reads title.basics.tsv,
#stores as dict {title_id :[movie_name, actor_list]}
# (note actor_list will be empty upon return)
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
  
  #Loop through lines, and add key,value
  #pairs to title_map
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
    title_map[title_id] = [values[2], [] ]
    
  return title_map
  

def readPrincipals(basic_map):
  principals = open("title.principals.tsv", "r", encoding='utf-8')
  
  #Read lines of file into entries
  entries = principals.readlines()
  
  #Remove column names
  del(entries[0])
  
  i = 0
  for entry in entries:
    
    #See readBasics() for explanation
    values = entry.split("\t")
    title_id = int((values[0][2:]))
    
    #Add the person's unique identifier to the 
    #second index of the value in basic_map at the
    #key of the movie identifier
    
    
    if title_id in basic_map:
      basic_map[title_id][1].append(values[2])
    else:
      i+=1
  print(i)
test = readBasics()

readPrincipals(test)

print(test[67][1])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  