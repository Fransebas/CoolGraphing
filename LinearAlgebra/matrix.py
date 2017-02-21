#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 13:44:09 2017

@author: fransebas
"""
from vectors import *

class Matrix():

    @staticmethod
    def I(n):
        return Matrix([ [1 if i is j else 0 for j in range(n) ] for i in range(n) ])

    @staticmethod
    def toVector(M):
        if M.m is 1:
            return M[0]
        else:
            """ Should rise an exception """
            print ("The matrix is not a vector")

    def __init__(self, vectors):
        if type(vectors[0]) is type(Vector([0])):
            self.vectors = vectors
            self.n = vectors[0].dim() # columns
            self.m = len(vectors) # rows
        else:
            self.vectors = [ Vector(v) for v in (vectors) ]
            self.n = len(vectors[0]) # columns
            self.m = len(vectors) # rows

    def copy(self):
        l = []
        for v in self.vectors:
            l.append( list(v.components) )
        return Matrix( l )




    '''@staticmethod
    def T(A):
        B = A.copy()
        # Debuggin ****************
        print (B)
        return B.T()'''

    def T(self):
        """ transpose of a matrix """

        vectors = [ [ 0 for i in range(self.m) ] for j in range(self.n) ]

        for i in range( len( self.vectors ) ): #rows
            for j in range( self.vectors[0].dim() ): #colums
                vectors[j][i] = self.vectors[i][j]

        return Matrix(vectors)

    def __mul__(self, B):
        """ Multiply matrix A*B """
        C = B.T()
        vectors = []
        i = 0
        if self.n is B.m:
            for r in self.vectors:
                vectors.append([])
                for c in C.vectors:
                    vectors[i].append(r*c)

                i += 1

            return Matrix(vectors)
        else:
            """should rise exception """
            print ("error no posible mutiplication")

    def __str__(self):
        s = ""
        for v in self.vectors:
            s += str(v) + '\n'
        return s

    def p(self, r1, r2):
        vAux = self[r2].copy()
        self[r2] = self[r1]
        self[r1] = vAux

    def r(self, r1, r2, c):
        """ sum row 2 by a multiple c of row 1  """
        self[r2] = self[r2] + ( c*self[r1] )


    def __getitem__(self, i):
        return self.vectors[i]

    def __setitem__(self, i, value):
        self.vectors[i] = value

    def solve(self,B):
        """ Solve a square matrix given a set of solutions B,
        B should be nx1 (most cases B.T())"""
        return (self**-1)*B

    def GaussJordan(self,Aug):
        print("this is the sol")
        print (Aug)
        print (self**-1)
        return (self**-1)*Aug
        """if self.n is self.m:
            A = self.copy()

            for i in range ( len( A.vectors ) ):
                 #select the pivot
                j = A.findNonZero(i)

                if j is None:
                    print ("Non invertible matrix")
                    return

                if j is not i:
                    A.p  (i, j)
                    Aug.p(i, j)

                #1 divide row to get 1

                (Aug[i]) /= A[i][i]
                A[i] /= A[i][i]

                for k in range(0, len( A.vectors )):
                    if k is i:
                        continue
                        #eros below and over the diagonal

                        c = -A.vectors[k][i]

                        A.r  (i, k, c)
                        Aug.r(i, k, c)

                return (A,Aug)

        else:
            print ("No square matrix")"""

    def findNonZero(self, i):
        for j in range( i, self.n ):
            if self[j][i] is not 0:
                return j
        return None

    def simplify(self, precision=16):
        for i in range ( len ( self.vectors ) ):
            for j in range ( self.vectors[i].dim() ):
                ( m,e ) = math.frexp( self[i][j] )

                if e <= -15:
                    self[i][j] = 0
                    continue

                """ It's not the best, I should check for all Natruals and not
                only 1"""
                if self[i][j] > 0.9999999 and self[i][j] < 1:
                    self[i][j] = 1
                    continue




    def __pow__(self, e):


        if self.n is self.m:
            if e is -1:
                # self.GaussJordan(Inv = Matrix.I(self.n))
                A = self.copy()
                Inv = Matrix.I(self.n)

                for i in range ( len( A.vectors ) ):
                    """ select the pivot """
                    j = A.findNonZero(i)

                    if j is None:
                        print ("Non invertible matrix")
                        return

                    if j is not i:
                        A.p  (i, j)
                        Inv.p(i, j)

                    """ 1 divide row to get 1 """


                    (Inv[i]) /= A[i][i]
                    A[i] /= A[i][i]

                    for k in range(0, len( A.vectors )):
                        if k is i:
                            continue
                        """ zeros below and over the diagonal """

                        c = -A.vectors[k][i]

                        A.r  (i, k, c)
                        Inv.r(i, k, c)


                return Inv

        else:
            print ("No square matrix")
