# CoolGraphing
Is a set of python program to graph curves and make lineal algebra

I made this programs just for fun, If they are usefull to you, use them freely. I know I lack a lot of documentation and comments but if people really use my program I'll add them.

# The Programs Icluded are 

- Zelle's graphing library (This is not mine nor to powerfull but really simple)
	- Grapher/graphics.py
- Vector and Matrix Classes for operations (This are mine but feel free to change the interface to use numpy or something you like)
	- LinearAlgebra/matrix.py and LinearAlgebra/vectors.py
- Grapher Class wich is a cartesian plane for graphing 
	- Grapher/grapher.py
- Least Square program where you can graph any function that passes near a cetain set of points
	- Grapher/leastSquares.py

# How to use them

- To use learn how to use Zelle's graphing library go to http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/graphics.html

- I made a mess making matrices that are made of vectors, anyway the interface is simple
	- To make a matrix: Matrix([ [a],[b], [c] ]) # matrix are made up from a list of list, and each small list is a row
	- to make a vector: Vector([a, b ,c]) # is a list of the individual values

- To make a catesian plane use the Class:
	- Plane((450,450)) # the parameter is a Touple pointing the center.
	- There are a lot of options to make a Plane that I do not explain here but If you need to know please email me ffransebas@gmail.com. 

- To make use of Least Squares
	- LeastSquare(setOfPoints, functions)
		- The setOfPoints is a list of touples ex: points = [(1,0),(10,50),(40,50),(200,50),(2,2),(400,400),(-120,-56)]
		- The function are pass as a string in python format ex:
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