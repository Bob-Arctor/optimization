# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 11:12:44 2016

@author: AKononov
"""

import numpy as np
import math

X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1]]) #training data X
y = np.array([[0,0,1,1]]).T #training data Y

# np.random.seed(1)

def weights(dim=3):
	return 2*np.random.random((dim,1)) - 1 #randomize intial weights (Theta)

def runForward(X, theta): #this runs our net and returns the output
	return sigmoid(np.dot(X, theta))
def costFunction(X, y, theta): #our cost function, simply determines the arithmetic difference between the expected y and our actual y
	m = float(len(X))
	hThetaX = np.array(runForward(X, theta))
	return np.sum(np.abs(y - hThetaX))
def sigmoid(x): return 1 / (1 + np.exp(- x)) #Just our run-of-the-mill sigmoid function