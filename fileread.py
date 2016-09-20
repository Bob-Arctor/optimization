# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:16:23 2016

@author: AKononov
"""

import sys, numpy as np, os

# first argument is init file
# second argument is intermidiate file - must be empty or absent in the begining
# third argument is output file - will be overwritten

print(sys.argv)

# control variables
controls = []
params = {'POPN' : 0, 'PARENTS' : 0, 'MRATE' : 0 }

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

print(params)

# now read second param which is a intermidiate file
# if file is not there or empty -> first iteration
if not os.path.isfile(sys.argv[2]) :#or os.stat("file").st_size == 0:
	# generate POPN - population
	# random values in every column based on given ranges
	
	nextPop = np.random.choice(np.arange(controls[0][0],controls[0][1],step=0.01),size=(params['POPN'],len(controls)),replace=False)
	for col in range(1,nextPop.shape[1]):
		nextPop[:,col] = np.random.choice(np.arange(controls[col][0],controls[col][1],step=0.01),size=(params['POPN']),replace=False)
	
# write new population to a file
	print(nextPop)

np.savetxt(sys.argv[2], nextPop, fmt='%10.5f', newline="\n")
