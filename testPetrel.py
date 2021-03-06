# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:24:17 2016

@author: AKononov
"""

import numpy as np, sys, os

def getScriptPath():
    return os.path.dirname(os.path.realpath(sys.argv[0]))
				
dumpFile = getScriptPath() + '\\' + sys.argv[1]
outFile = getScriptPath() + '\\' + sys.argv[2]

curPop = np.loadtxt(dumpFile)
#dummy with extra column
output = np.zeros((curPop.shape[0], curPop.shape[1]+1))
#dummy function
def myfunc(x):
	return 23+2*x[1]*x[0] - 5*x[0] - x[1]*x[1] + 8.3 * x[1] +1.3*x[0]*x[0]
	
res = np.apply_along_axis( myfunc, axis=1, arr=curPop )
res = res[None].T
output[:,:-1] = curPop
output[:,-1:] = res

np.savetxt(outFile, output, fmt='%10.5f', newline="\n")
#print(output)