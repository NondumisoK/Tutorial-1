import numpy
# For any given array X
m=input("Please input array number:")
X=numpy.arange(m)
X_even=X[2:-1:2] #Take all even points 
X_Odd=X[1:-1:2] #Take all odd points in array
X_even_skip=[2::2] # Taking all even points yet skipping first and last points
