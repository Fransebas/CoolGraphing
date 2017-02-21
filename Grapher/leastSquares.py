#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 20:56:50 2017

@author: fransebas
"""
import math
import sys
import inspect as inspect
from grapher import *
sys.path.append('/Users/again/Python/LinearAlgebra')
from matrix import *

class LeastSquare:
    def __init__(self, points, fs = "def f(x): return %x*$0$% + %$1$%", n = None):
        """ fs is the function string """
        self.fs = fs

        """ Count the number of constants if is not provided
        which shold match the number of separate functions in f(x) i.e. x, x**2, x**3 ..."""
        if n is None:
            self.n = 0
            self.countVars()
        else:
            self.n = n


        self.functions = [None for i in range(self.n)] #  make the n spae
        self.getFunctions()

        self.cartesian = Plane((450,450))
        self.points = points
        self.cartesian.drawPoints(points, 3)

    def getNextC(self,i, c, s = None):
        if s is None:
            s = self.fs

        for j in range(i+1, len(s) ):
            if s[j] is c:
                return j

    def clean(self, s):
        """ clean all the $ """
        for i in range( len(s) ):
            if s[i] is '$':
                j = self.getNextC(i,'$', s)
                return s[:i] + "1" + s[j+1:]




    def getFunctions(self):
        e = i = j = 0
        l = len(self.fs)
        '''while i < l:
            if self.fs[i] is '%':
                j = self.getNextC(i,'%')
                s = self.clean(self.fs[i+1:j])

                s = "lambda x: " + s
                self.functions[]( eval( s ) )

                i = j
                count += 1
            i += 1'''


        while i < l:
            if self.fs[i] is '%': # or any other special character
                j = self.getNextC(i,'%')
                e = i
            elif self.fs[i] is '$':
                k = self.getNextC(i, '$')

                indx = int( self.fs[i+1:k] )

                s = self.clean(self.fs[e+1:j])
                s = "lambda x: " + s
                print (s)

                self.functions[indx] = ( eval( s ) )

                i = j
            i += 1

    def wait(self):
        self.cartesian.win.getMouse()
        self.cartesian.win.close()

    def solve(self):
        self.A = self.getMatrixFromPoints(self.points)
        print (self.A)
        self.B = self.getB(self.points)
        self.P = self.getBestSol(self.A, self.B)
        self.Eq = self.getEquation(self.A)
        self.vals = self.Eq.solve(self.P)

        print (self.vals)

        self.createFunction()

    def graph(self):
        print (self.f)
        self.cartesian.graph(self.f)

    def createFunction(self):
        i = 0
        self.fs2 = ''
        l = len(self.fs)
        while i < l:
            if self.fs[i] is '%': # or any other special character
                i += 1
                continue
            if self.fs[i] is '$':
                j = self.getNextC(i, '$')
                indx = int( self.fs[i+1:j] ) # don't know if the right is inclusive or not
                i = j
                self.fs2 += str(self.vals[indx][0])
            else:
                self.fs2 += self.fs[i]
            i += 1



        exec ( self.fs2 , globals())
        self.f = f

        print ("the function is ")
        print (self.fs2)
        print (self.f)
        print (self.f(1))

        return self.f

    def countVars(self):
        self.n = 0
        for c in self.fs:
            if c is "$":
                self.n += 1
        self.n //= 2

    def getMatrixFromPoints(self, points):
        A = []
        for p in points:
            row = []

            print (self.n)

            for i in range(self.n):
                row.append( self.functions[i]( p[0] ) )

            A.append(row)
        return Matrix(A)

    def getB(self, points):
        b = []
        for p in points:
            b.append([p[1]])
        return Matrix(b)

    def getBestSol(self, A, B):
        return A.T()*B

    def getEquation(self, A):
        return A.T()*A

    #def determinationCoef(self):

if __name__ == "__main__":


    points = [(1,0),(10,50),(40,50),(200,50),(2,2),(400,400),(-120,-56)]
    #points = [(-1,5),(1,13),(2,17)]
    print ( points )

    ls = LeastSquare(points, fs =
                     """def f(x): return %$6$*x**6% + %$5$*x**5% + %$4$*x**4% + %$3$*x**3% + %$2$*x**2% + %$1$*x% + %$0$%
    """)

    """
    Polinoms:
        "def f(x): return %$4$*x**4% + %$3$*x**3% + %$2$*x**2% + %$1$*x% + %$0$%"

    Exponentials
        def f(x):
            return %$0$*math.exp(x/100)% + %$1$% ## check for the x/100

    Logarithms:
        def f(x):
            if x > 0:
                return %$0$*math.log(x)% + %$1$%
            return 0

            roots:
            sqaure Root
            def f(x):
                if x >= 0:
                    return %$0$*x**(1/2)% + %$1$%
                return 0
    """
    ls.solve()
    ls.graph()
    ls.wait()

