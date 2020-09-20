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

# Create variable pointing to data file.
file_name = './data/raw/sara.txt'

# create file object from file
file_object = open(file_name, 'r')

# read contents of file to list.
line_list = file_object.readlines()

# close file
file_object.close()



# Pull one line of data from file
lineString = line_list[87]

# Split string into list of items
lineData = lineString.split()

record_id = lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData[6]
obs_lon = lineData[7]

print( f" Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")

