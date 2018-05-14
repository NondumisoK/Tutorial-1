import numpy
import vector_cr
def integrate_simpson(n):
  dx=numpy.pi/2/(n-1)*2
  y=numpy.cos(vector_cr(n))
  x_even=y[2:-1:2]
  x_odd=y[1:-1:2]
  sum=numpy.sum(x_even)/3+numpy.sum(x_odd)*2/3+y[0]/6+y[-1]/6
  return sum*dx
