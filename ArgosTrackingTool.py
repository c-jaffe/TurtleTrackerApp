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

# Pull one line of data from file
lineString = "21892	29051	7/3/2003 9:23	B	0	33.887	-77.95	43.983	-128.418	2	0	-132	96	1	401 651133.1	0"

# Split string into list of items
lineData = lineString.split()

record_id = lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData[6]
obs_lon = lineData[7]

print( f" Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")
