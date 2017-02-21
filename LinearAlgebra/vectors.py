#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 16:17:01 2017

@author: fransebas
"""
import math
import matrix

class Vector():

    def __init__(self, components):

        self.components = components
        self.lenght = None

    def __len__(self):
        return None
        return len(self.components)

    def length(self):
        if self.lenght is None:
            self.lenght = math.sqrt(self*self)
        return self.lenght

    def dim(self):
        return len(self.components)

    def toMatrix(self):
        '''l = []
        for c in self.components:
            l.append([c])'''
        return matrix.Matrix([self.components])

    def __add__(self, b):
        l = []
        if b.dim() is self.dim():
            for i in range( self.dim() ):
                l.append(b.components[i] + self.components[i])

            return Vector(l)
        else:
            # sould rise exception
            print ("Vectors of diferent size")

    def __sub__(self, b):
        l = []
        if b.dim() is self.dim():
            for i in range(self.dim()):
                l.append(self.components[i] - b.components[i])

            return Vector(l)
        else:
            # sould rise exception
            print ("Vectors of diferent size")

    def __mul__(self, b):
        if type(b) is type(1) or type(b) is type(1.0):
            l = []
            for a in self.components:
                l.append( b*a )
            return Vector(l)
        else:
            r = 0
            if b.dim() is self.dim():
                for i in range( len(self.components) ):
                    r += self.components[i]*b.components[i]

                return r
            else:
                # sould rise exception
                print ("Vectors of diferent size")

    def __itruediv__(self, val):

        for k in range ( 0, self.dim() ):
            self[k] = (self[k]/val)
        return self

    def __neg__(self):
        return (-1)*self

    def __rmul__(self, b):
        return self * b

    def __str__(self):
        return str(self.components)

    def __lshift__(self, b):
        """ angle in radians """
        return math.acos((self*b)/(self.length()*b.length()))

    def __rshift__(self, b):
        """ angle in radians """
        return math.acos((self*b)/(self.length()*b.length()))

    def __getitem__(self, i):
        return self.components[i]

    def __setitem__(self, i, value):
        self.components[i] = value

    def copy(self):
        return Vector( list(self.components) )