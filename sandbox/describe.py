import numpy as np

def luri_describe(obj):

  print('type of your object')
  print(type(obj))
  
  print('string representation of your object')
  print('"'+str(obj)+'"') #added quotes for visual effect
  
  print('location of your object in memory map of python')
  print(id(obj))
  print(hex(id(obj)))
  
  print('byte footprint of your object -> of the descriptor (?), does not include auxiliary memory as of a numpy array; if you obj is a container or a structure, im not looking into each element or attribute')
  #i might do it with dict.items() of a  dictionary and with dir(obj) of an object recursively
  
  '''
  
In [1]: x={'a':1}                                                                                                                                                                              

In [2]: for i in x: 
   ...:     print(i) 
   ...:                                                                                                                                                                                        
a

In [3]: for i in x.items(): 
   ...:     print(i) 
   ...:                                                                                                                                                                                        
('a', 1)

In [4]: for i in x.values(): 
   ...:     print(i) 
   ...:                                                                                                                                                                                        
1

  
  '''
  
  import sys
  print(sys.getsizeof(obj))
  
  if isinstance(obj, np.ndarray ):
    print('byte footprint of your object reported by numpy')
    print(obj.nbytes)





#
luri_describe('1')



input('paused...')




luri_describe(1)
input('paused...')
luri_describe(1.)
input('paused...')
luri_describe(1+0j)
input('paused...')
luri_describe((1,))
input('paused...')
luri_describe([1])
input('paused...')
import numpy as np
luri_describe(np.array(1))
input('paused...')
luri_describe(np.array([1]))
input('paused...')
luri_describe(np.array([[1]]))
input('paused...')

luri_describe(np.random.rand(100,100) )
input('56paused...')

luri_describe(np.random.rand(100,100)[:,:] ) #view
input('59paused...')

luri_describe((np.random.rand(100,100).T).flatten()[:-1])
input('57paused...')
luri_describe( list((np.random.rand(100,100).T).flatten()[:-1]) )
input('57bpaused...')
luri_describe( [((np.random.rand(100,100).T).flatten()[:-1]) ])
input('5cbpaused...')


class luri_class():

  def __init__(self):
    return

  def __str__(self):
    '''a default behavior __str__ function'''
    print('@luri_class.__str__')
    return super().__str__()

  def __sizeof__(self):
    print( 'modafuqing huge' )
    return 100_000 #returning a fake integer here -> might confuse the garbage colelctor (?)

luri_obj = luri_class()
luri_describe(luri_obj)


#numpy array getsizeof numpy view getsizeof

#about views
x=np.array([1,2,3])
y=x[0:2] #0 and 1
y[:]=999
print(x)
print(x.base)
print(y.base)
x=y
print(x)
print(y)
print(x.base)
print(y.base)
#a view has a base
#even if there is no more name (reference) to the original object on the user side
#all created views continue as views and the base obj is not garbage collected nor its unacessed elements are cleared


'''

In [5]:                                                                                                                                                                                        

In [5]: x=np.array([1],dtype=object)                                                                                                                                                           

In [6]: import sys                                                                                                                                                                             

In [7]: sys.getsizeof                                                                                                                                                                          
Out[7]: <function sys.getsizeof>

In [8]: sys.getsizeof(x)                                                                                                                                                                       
Out[8]: 104

In [9]: x[0]='a'                                                                                                                                                                               

In [10]: sys.getsizeof(x)                                                                                                                                                                      
Out[10]: 104

In [11]: x[0]=np.zeros([100000])                                                                                                                                                               

In [12]: sys.getsizeof(x)                                                                                                                                                                      
Out[12]: 104

In [13]: x.shape                                                                                                                                                                               
Out[13]: (1,)

In [14]: x[0].shape                                                                                                                                                                            
Out[14]: (100000,)


'''
