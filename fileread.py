# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:16:23 2016

@author: AKononov
"""

import sys

# first argument is init file
# second argument is output file

print(sys.argv)

# control variables
controls = []
params = {'GENS' : 0, 'POPN' : 0, 'PARENTS' : 0, 'MRATE' : 0 }

# initialize algorthm
with open(sys.argv[1], "r") as f:
	searchlines = f.readlines()
	f.close()
for i, line in enumerate(searchlines):
	print(line)
	if "CTRLS" in line: 
		for l in searchlines[i+1:]:
			l = l.strip()
			if bool(l):
				if l[-1:] is "/":
					controls.append([float(x) for x in l[:-1].split()])
					break
				controls.append([float(x) for x in l.split()])
	elif "GENS" in line:
		for l in searchlines[i+1:]:
			l = l.strip()
			if bool(l):
				if l[-1:] is "/":
					params['GENS'] = int(l[:-1].strip())
					break
	elif "POPN" in line:
		for l in searchlines[i+1:]:
			l = l.strip()
			if bool(l):
				if l[-1:] is "/":
					params['POPN'] = int(l[:-1].strip())
					break
	elif "MRATE" in line:
		for l in searchlines[i+1:]:
			l = l.strip()
			if bool(l):
				if l[-1:] is "/":
					params['MRATE'] = float(l[:-1].strip())
					break
	elif "PARENTS" in line:
		for l in searchlines[i+1:]:
			l = l.strip()
			if bool(l):
				if l[-1:] is "/":
					params['PARENTS'] = int(l[:-1].strip())
					break
				
print(controls)
print(params)