#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 20:56:50 2017

@author: fransebas
"""
import sys
from grapher import *
sys.path.append('/Users/again/Python/LinearAlgebra')
from matrix import *

class LeastSquare():
    def __init__(self, points, fs = "def f(x): return x*$0 + $1", n = None):
        if n is None:
            self.n = 0
            self.countVars()
        else:
            self.n = n

        self.cartesian = Plane((450,450))
        self.points = points
        self.cartesian.drawPoints(points, 3)

        self.A = self.getMatrixFromPoints(self.points)
        self.B = self.getB(points)
        self.P = self.getBestSol(A, B)
        self.Eq = self.getEquation(A)
        self.val = Eq.solve(P)
        self.fs = fs

        self.createFunction()

        self.cartesian.graph(self.f)

    def createFunction():
        fs2 = ''
        for i in range(self.fs):
           if self.fs[i] is '$':
               indx = int( self.fs[i+1] )
               i += 1
               self.fs2 += str(self.vals[0][indx])
           else:
               self.fs2 += self.fs[i]

        self.f = exec ( fs2 )
        return self.f

    def countVars():
        self.n = 0
        for c in range:
            if c is "$":
                self.n += 1

    def getMatrixFromPoints(points):
        A = []
        for p in points:
            A.append([1,p[0]])
        return Matrix(A)

    def getB(points):
        b = []
        for p in points:
            b.append([p[1]])
        return Matrix(b)

    def getBestSol(A, B):
        return A.T()*B

    def getEquation(A):
        return A.T()*A


def getMatrixFromPoints(points):
    A = []
    for p in points:
        A.append([1,p[0]])
    return Matrix(A)

def getBestSol(A, B):
    return A.T()*B

def getEquation(A):
    return A.T()*A

def getB(points):
    b = []
    for p in points:
        b.append([p[1]])
    return Matrix(b)

def f(x,c,d):
    return c + d*x

points = [(90,20),(10,50),(40,50),(200,50),(1,1),(400,400)]

A = getMatrixFromPoints(points)
print (A)
B = getB(points)
print (B)
P = getBestSol(A, B)
print (P)
Eq = getEquation(A)
print (Eq)
print (P.m)
sol = Eq.solve(P)

print (sol)

cartesian = Plane((450,450))

cartesian.drawPoints(points, 3)
cartesian.graph(lambda x: sol[0][0] + sol[1][0]*x)

cartesian.win.getMouse()
cartesian.win.close()