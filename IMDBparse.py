# -*- coding: utf-8 -*-
"""
IMDBparse.py ~ Contains functions for parsing the
Internet Movie Database (IMDB)
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
    #these characters and cast it to an integer
    #to remove leading zeroes, then append the name
    #of movie (values[2]) using title_id as 
    #key to title_map
    
    title_id = int((values[0][2:]))
    title_map[title_id] = [values[2], [] ]
    
  return title_map
  

def read_principals(basic_map):
  principals = open("title.principalstsv", "r", encoding='utf-8')
  
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
      #Add the person's unique identifier to the 
      #second index of the value in basic_map at the
      #key of the movie identifier
      basic_map[title_id][1].append(values[2])


    
    
    
    
    
    
    
    
    
    
    
  