import numpy as np

def luri_describe(obj):

  print('type of your object')
  print(type(obj))
  
  print('string representation of your object')
  print('"'+str(obj)+'"') #added quotes for visual effect
  
  print('location of your object in memory map of python')
  print(id(obj))
  print(hex(id(obj)))
  

  
  if isinstance(obj, np.ndarray ):
    print('byte footprint of your object reported by numpy')
    print(obj.nbytes)
  else
    print('byte footprint of your object -> of the descriptor (?), does not include auxiliary memory as of a numpy array')
    import sys
    print(sys.getsizeof(obj))




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

luri_describe(np.random.rand(100,100).T)
input('57paused...')

class luri_class():

  def __init__(self):
    return

  def __str__(self):
    '''a default behavior __str__ function'''
    print('@luri_class.__str__')
    return super().__str__()

  def __sizeof__(self):
    print( 'modafuqing huge' )
    return 100_000

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
