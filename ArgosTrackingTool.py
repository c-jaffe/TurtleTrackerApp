#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Cate Jaffe (cmj64@duke.edu)
# Date:   September 20 2020
#-------------------------------------------------------------

# Ask user to search for date:
user_date = input("Specify a date to find Sara: ")

# Create variable pointing to data file.
file_name = './data/raw/sara.txt'

# create file object from file
file_object = open(file_name, 'r')

# read contents of file to list.
line_list = file_object.readlines()

# close file
file_object.close()

# Create 2 empty dictionary objects
date_dict = {}
coord_dict = {}

### Loop!
# iterate thru all lines in list
for lineString in line_list:
    
    # skip over lines if first character is # or u (ie, first 17 lines)
    if lineString[0] in ('#','u'): continue
        
    # Split string into list of items
    lineData = lineString.split()
    
    # extract items in list to variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4] 
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    
    # assign values to dictionary, only if LC = 1,2, or 3
    if obs_lc in ('1', '2', '3'):
        #print( f" Record {record_id} indicates Sara was seen at lat: {obs_lat} and lon: {obs_lon} on {obs_date}")
        date_dict[record_id] = obs_date
        coord_dict[record_id] = ( obs_lat, obs_lon )
        
# Create empty list to hold matching keys
matching_keys = []
        
# After above filtering, loop through items in dictionary and collect keys for mathcing dates
for date_item in date_dict.items():
    the_key, the_date = date_item    
    
    # Does date match user date? If so, add keys to list
    if the_date == user_date:
        matching_keys.append(the_key)
        
# Reveal locations for each key in matching_keys list
for matching_key in matching_keys:
    the_lat, the_lon = coord_dict[matching_key]
    # print(the_lat, the_lon)
    print( f" Record {matching_key} indicates Sara was seen at lat: {the_lat} and lon: {the_lon} on {user_date}")
        
        
    
