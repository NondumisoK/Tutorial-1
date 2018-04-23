import numpy
def vector_cr(n):
  x=numpy.arange(n)
  x=0.5*x*numpy.pi/(n-1)  # to keep array within [0,pi/2]
  return x
  
def integrate_simple(n):
  dx=numpy.pi/2/2
  x=vector_cr(n)
  y=numpy.cos(x)
  sum_y=numpy.sum(y)
  return dx*sum_y
  
L=[10,30,100,300,1000]  
for i in L:
  m=integrate_simple(i)
  soln_for_i=[]+m
 
 
Actual=1 # Actual cos integral between 0 and pi/2
Error1=soln_for_i[0]-1
Error2=soln_for_i[1]-1
Error3=soln_for_i[2]-1
Error4=soln_for_i[3]-1
Error5=soln_for_i[4]-1

  
  

  
  
