# -*- coding: utf-8 -*-
import csv
import os
"""
  IMDBparse.py ~ Contains functions for parsing the
  Internet Movie Database (IMDB), encoding it into
  a graph format, and writing the results to files.

  @author Lucas Gorski
"""

# This is the primary function of this file.
# Calling it parses all of the IMDB files, processes them into
# an adjacency matrix and two reference maps, and then writes them
# to files in the directory specified by directory_name.
# 
def generate_adj_list(directory_name):
  os.mkdir(directory_name)
  
  # Call read_principals to parse IMDB data to
  # generate the title and name maps
  title_map, name_map = read_principals()
  
  # Open target files for writing
  adj_list_file = open(directory_name + "/Adj_list.txt", "w", encoding='utf-8')
  title_map_file = open(directory_name + "/Title_map.csv", "w", encoding='utf-8')
  name_map_file = open(directory_name + "/Name_map.csv", "w", encoding='utf-8')
  
  # Pass map files to a csv writer, as we will
  # store these as .csv files.
  title_writer = csv.writer(title_map_file, delimiter=',', lineterminator='\n')
  name_writer = csv.writer(name_map_file, delimiter=',', lineterminator='\n')
  
  # Write the contents of title_map and name_map to .csv files
  # because we will be modifying their contents later
  # in this function.
  for key, value in title_map.items():
    title_writer.writerow([key, value])
  title_map_file.close()
  
  for key, value in name_map.items():
    name_writer.writerow([key, value])
  name_map_file.close()
  
  # Write entries from title_map to adjacency list file.
  for key, value in title_map.items():
    line = key + " "
    for actor in value[1]:
      line += actor + " "     
      
      # Remove edge from name_map to prevent
      # duplicate edges from being recorded
      name_map[actor][1].remove(key)
    line += '\n'
    adj_list_file.write(line)
    
  # Write entries from name_map to adjacency list file.
  for key, value in name_map.items():
    
    if len(value[1]) > 0:
      line = key + " "
      
      for movie in value[1]:
        line += movie + " "    
        
      line += '\n'
      adj_list_file.write(line)
    else:
      line = key + '\n'
      adj_list_file.write(line)
    
  adj_list_file.close()


'''
  The functions below are helper functions for generate_adj_list
'''


# Returns a list containing two dictionaries:
# The first dictionary maps movie ID's to their name, 
# a list of actors/directors/writers who appear, the rating
# of the movie, and the number of votes the rating is based off.
#
# The second dictionary maps people's ID's to their name and
# a list of movies they appear in.
def read_principals():
  
  basic_map = read_basics()
  name_map = read_names()
  principals = open("title.principals.tsv", "r", encoding='utf-8')
  
  
  # Read lines of file into entries
  entries = principals.readlines()
  
  principals.close()
  
  # Remove column names
  del(entries[0])
  
  for entry in entries:
    
    # See readBasics() for explanation
    values = entry.split("\t")
    title_id = values[0]
    
    
    # Check if title_id exists in basic map.
    # If it exists, update record. Otherwise do nothing.
    # (Intuitively you would assume it always does,
    # but as of 11/13/2019 there are 164 title_id's
    # present in title.principals.tsv that are not
    # present in title.basics.tsv)
    if title_id in basic_map:
     
      # Check if person_id exists in name_map. 
      # If it does not, do nothing.
      person_id = values[2]
      if person_id in name_map:
        # Append person_id to actor_list in the 
        # basic_map at key title_i
        basic_map[title_id][1].append(person_id)
        
        #Append title_id to the actor's movie list
        name_map[person_id][1].append(title_id)
  
  return [basic_map, name_map]


# Returns a dictionary in the following format:  
# Key: the title's unique ID.
# Value: a list containing: the name of the title,
#        a list of actors which appear in it, 
#        it's rating out of 10 and how many votes
#        the rating is based off.
# (note: the actor_list will be empty upon return)
def read_basics():
  
  ratings_map = read_ratings()
  
  basics = open("title.basics.tsv", "r", encoding='utf-8')
  
  # Read lines of file into titles
  titles = basics.readlines()
  
  basics.close()
  
  # Since first line in file is column names,
  # remove it
  del(titles[0])
  
  # Create empty dictionary to fill with values
  title_map = {}
  
  # Loop through lines, and add key,value
  # pairs to title_map
  for entry in titles:
    
    # Split string by TAB character into
    # indivudual value fields.
    values = entry.split("\t")
    
    # Retrieve title_id from the first index in values
    # Append to title_map at key title_id a list containing 
    # the name of movie and empty 
    # list used to later store actor's names.
    # Add two -1 values, which will be used to store
    # rating and number of votes. The -1 value ensures
    # all entries have the same number of index's because
    # we cannot assume all movies have an entry in ratings_map
    
    title_id = values[0]
    title_map[title_id] = [values[2], [], -1, -1 ]
    
    # If the movie has an entry in the ratings map,
    # replace the -1 values with the rating and number
    # of votes
    if title_id in ratings_map:
      rating, votes = ratings_map[title_id]
      title_map[title_id][2], title_map[title_id][3] = rating, votes
  
  return title_map

# Returns a dictionary in the following format:
# Key: the title's unique ID.
# Value: A list containing a double representing 
#        the movie's rating out of 10, and an integer
#        representing the number of votes  
def read_ratings():
  title_ratings = open("title.ratings.tsv", "r", encoding='utf-8')
  
  # Read lines of title_ratings into ratings
  ratings = title_ratings.readlines()
  
  title_ratings.close()
  
  # Remove column names
  del(ratings[0])
  
  # Create empty dictionary to fill with values
  ratings_map = {}
  
  # Loop through each entry in ratings, and append
  # the rating and number of votes to ratings_map
  for entry in ratings:
    
    values = entry.split("\t")
    
    title_id = values[0]
    ratings_map[title_id] = [values[1], values[2].rstrip()]
  return ratings_map

# Returns a dictionary in the following format:
# Key: the person's unique ID
# Value: list containing their name and a list
#        containing all titles they appear in
#        (Note: title list will be empty upon return)
def read_names():
  names = open("name.basics.tsv", "r", encoding='utf-8')
  
  entries = names.readlines()
  
  names.close()
  
  # Remove column names
  del(entries[0])
  
  # Initialize name_map to empty dictionary
  name_map = {}
  
  # Loop through entries for actors, and append
  # their name to name_map at key person_id
  for entry in entries:
    
    values = entry.split("\t")
    person_id = values[0]
    name_map[person_id] = [values[1], []]
    
  
  
  return name_map



generate_adj_list("luck")

