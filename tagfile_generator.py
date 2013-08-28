#------------
# Tag File Generator
#
# This script reads the taglist.config file to figure out which packages you 
# want to intall.  It then generates the appropriate tag files and folders for 
# a custom installation.  This is easier than manually editing every tag file.
#
# All packages in the taglist.config file will be marked as "ADD".  All other 
# packages not in this list will be marked as "SKP"
#------------

import re

# List of Package Folders
packages = {
		"a":[],
		"ap":[],
		"d":[],
		"e":[],
		"f":[],
		"k":[],
		"kde":[],
		"kdei":[],
		"l":[],
		"n":[],
		"t":[],
		"tcl":[],
		"x":[],
		"xap":[],
		"xfce":[],
		"y":[]
	}

# Read taglist.conf into memoery
taglist = []
f = open("taglist.conf","r")
for line in f:
	# Stip Comments
	l = line.split("#")[0]
	# Strips the White Space
	m = re.match("[^\s]+",l)
	# Add matches to the taglist
	if m:
		taglist.append(m.group(0))

#print taglist

f.close()

# Read all of the tag files
for category in packages:
	f = open("slackware/"+category+"/tagfile","r")
	for line in f:
		pkg_name = line.rsplit(":")[0]
		if pkg_name == "":
			continue
		if pkg_name in taglist:
			packages[category].append(pkg_name)#+":ADD")
		else:
			packages[category].append(pkg_name)#+":SKP")


	f.close()

# Create Blank Conf File
'''
f = open("taglist.conf","w")
for c in packages:
	f.write("#--------------\n")
	f.write("# "+c+"\n")
	f.write("#--------------\n")
	for p in packages[c]:
		f.write(p+"\n")
'''

# Write all of the tag files to disk
"""
for category in packages:
	f = open(category+"/tagfile","w")
	for pkg in packages[category]:
		f.write(pkg+"\n")
"""
