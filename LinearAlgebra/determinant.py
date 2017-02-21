#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 12:03:30 2017

@author: fransebas
"""
import math

from matrix import *

def p(b, A):
    """ get the normal vector of A to b,
    It's suppose to be working"""
    A = A.T()
    print ((A.T()*A)**-1)
    x = (( A.T()*A )**-1) * A.T() * b.toMatrix().T()
    p = Matrix.toVector((A*x).T()) # vector
#    n = b - p
    return p

def pdet(vectors):
    """ partial determinant
        pdet(x1, x2, x3... xn) = len(x1)*math.sin(angle)*pdet(x2,x3,x4...xn)
        pdet(x1, x2, x3... xn) = det(x1, x2, x3... xn) iff {x1, x2, x3... xn} are a basis
        pdet(x1) = len(x1)"""
    if len(vectors) is 1:
        return vectors[0].length()
    if len(vectors) is 2:
        return vectors[0].length()*vectors[1].length()*math.sin( vectors[0] >> vectors[1] )
    else:
        return vectors[0].length()*math.sin(( vectors[0] >> p(vectors[0], Matrix(vectors[1:])) ) )*pdet(vectors[1:])

def angle(x,y):
    pass

M = Matrix([ [8,2,12],
             [3,1,5],
             [6,8,4] ])


b = Vector([6,0,0,1])

#n = norm(b, A)

print ( pdet( [Vector( [1,1,1,1,1,1] ),
               Vector( [3,3,3,-8,3,3] ),
               Vector( [0,1,3,8,8,1] ),
               Vector( [-5,27,0,6,9,1] ),
               Vector( [-5,0,0,6,0,1] ),
               Vector( [-5,0,13,6,0,1] ),
       ]))