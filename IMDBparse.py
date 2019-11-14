# -*- coding: utf-8 -*-
"""
IMDBparse.py ~ Contains functions for parsing the
Internet Movie Database (IMDB)

@author Lucas Gorski
"""
"""
TODO: Since adj matrix must be square, we should undo the int typecast
and omit removing leading characters and 0's, since we need to 
differentiate between movie nodes and actor nodes

"""


#Reads title.basics.tsv,
#stores as dict {title_id :[movie_name, actor_list]}
# (note actor_list will be empty upon return)
#return dict
def read_basics():
  basics = open("title.basics.tsv", "r", encoding='utf-8')
  
  #Read lines of file into titles
  titles = basics.readlines()
  
  #Since first line in file is column names,
  #remove it
  del(titles[0])
  
  #Create empty dictionary to fill with values
  #Key: the title's unique ID
  #Value: a string containing the name of the title.
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
    #these characters and cast it to an integer
    #to remove leading zeroes, then append the name
    #of movie (values[2]) using title_id as 
    #key to title_map
    
    title_id = int(values[0][2:])
    title_map[title_id] = [values[2], [] ]
    
  return title_map
  

def read_principals(basic_map):
  principals = open("title.principals.tsv", "r", encoding='utf-8')
  name_map = read_names()
  #Read lines of file into entries
  entries = principals.readlines()
  
  #Remove column names
  del(entries[0])
  
  for entry in entries:
    
    #See readBasics() for explanation
    values = entry.split("\t")
    title_id = int((values[0][2:]))
    
    
    #Check if title_id exists in basic map.
    #If it exists, update record. Otherwise do nothing.
    #(Intuitively you would assume it does,
    #but as of 11/13/2019 there are 164 title_id's
    #present in title.principals.tsv that are not
    #present in title.basics.tsv)
    if title_id in basic_map:
      #Reference name_map by the person_id 
      #to retrive actor's name. Check
      #if person_id exists in name_map, and if so
      #append to actor_list in the basic_map at key title_id
      person_id = int(values[2][2:])
      if person_id in name_map:
        name = name_map[person_id]
        basic_map[title_id][1].append(name)


def read_names():
  names = open("name.basics.tsv", "r", encoding='utf-8')
  
  entries = names.readlines()
  
  #Remove column names
  del(entries[0])
  
  #Initialize name_map to empty dictionary
  #Key: the person's unique ID
  #Value: a string containing the person's name
  name_map = {}
  
  for entry in entries:
    
    values = entry.split("\t")
    
    person_id = int(values[0][2:])
    name_map[person_id] = values[1]
    
  return name_map
    
    
test = read_basics()
read_principals(test)

print(test[1504832])
    
    
    
    
    
    
    
    
  