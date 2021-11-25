'''
# x1=np.random.random([2,2])
# x2=np.random.random([2,2])
# x3=np.random.random(2)

# print('x1=',x1)
# print('x2=',x2)
# # x>>loader('name.txt')

# [x1] >> loader('name.txt')
# #if x is 2d, save m = x = args[0]
# #if x is one or more 1d, save m = np.vstack(args).T

# y1 = loader('name.txt').M
# [y1] = loader('name.txt').M,
# print('y1=',y1)

#note q se salvar c m c, vai ter q ler com m ou como c c c c

#a alternativa seria o loader salvar o txt com metadados no cabeçalho (qual ou quais colunas são cada c ou m) e receber como argumento o dict locals() e o string dos nomes de var para ele fazer o desempacoamento complexo

#example
[P,DP,ThetaS,ThetaL,DV,DVEL,DH,DH2,DH3] >> loader('sim_xe_stuff/stuff_xe.txt')
[P,DP,ThetaS,ThetaL,DV,DVEL,DH,DH2,DH3] = loader('sim_c1_stuff/stuff_c1.txt').T
'''

import numpy as np
class loader():
  def __init__(self,fname):
    self.fname=fname
  # __ilshift__ <<=
  # __irshift__ >>=
  # __lshift__ __rlshift__<<
  # __rshift__   __rrshift__>>

  def __rrshift__(self,list1):
    # print('__rrshift__')
    # print(self.fname)
    # print(args)
    
    if (len(list1) == 1) and (np.asarray(list1[0]).ndim == 2):
        mat=list1[0]
        np.savetxt(self.fname,mat)
    elif ( len(list1)>=1 ) and (np.all([np.asarray(list1[j]).ndim == 1 for j in range(len(list1))])):
      mat=np.vstack(list1).T
      np.savetxt(self.fname,mat)
    #else #some are 2d and some are 1d
    #for each, if 1d reshape to 2d as col
    #then hstack all
    #then save
    elif ( len(list1)>=1 ) and not (np.all([np.asarray(list1[j]).ndim == 1 for j in range(len(list1))])):
      items=[]
      for item in list1:
        if item.ndim==1:
          items+=[item.reshape([len(item),1])]
        elif item.ndim==2:
          items+=[item]
      mat=np.hstack(items)
      # print(mat)
      np.savetxt(self.fname,mat)
    
    return 

#   def __pos__(self):
#     return np.loadtxt(self.fname,ndmin=2)
  
  @property
  def T(self):
    '''loads and returns transposed for unpacking'''
    return np.loadtxt(self.fname,ndmin=2).T

  @property
  def M(self):
    '''loads and returns as 2d'''
    return np.loadtxt(self.fname,ndmin=2)


