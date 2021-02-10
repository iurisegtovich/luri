#maybe call "a" "mat" and "r" "seq"
#more typing but a and r are doomed to be used as vars soon enough in any script
#and its better than diffing only by op like luri("1,2;3,4") and luri[1:30:2]

class mat:
    import numpy as np
    
#    def __init__(self,*args):
#        print('obj=a(): init')
#        self.prop=args
#        return
#
#    def __new__(cls,*args):
#        print('obj=a(): new')
#        self=super().__new__(cls)
#        return self

    def __mod__(self,arg):
        import numpy as np
        #print('obj(): called')
        #print(self.prop)
        #print(args)
        if isinstance(arg,str):
            return self._array(arg)
        return


    #TOC
    #> array 1d/2d from:
    #> string with:
    #> columns by space, comma, tab
    #> lines by ctrlR ctrlN semicolon;
    def _array(self,string):
        string=string.replace(';','\n')
        string=string.replace('\r\n','\n')
        
        string=string.replace(',',' ')
        string=string.replace('\t',' ')
        
        import numpy as np
        import io
        array = np.loadtxt(io.StringIO(string),ndmin=2)
        return array
    
#in order to use variables in the convenience i would have to split each field and use  ast.literal_eval() with the caller namespace before sending into loadtxt
#in order to compose like (see below) i would have check, after the eval, if the obj is a 1d or 2darray and split into elements for reparsing
#like M = [line; line; 1, 2, 3]
#or #like M = [line; line; [ 1, 2, 3 ] ]
#or like M = [col, col, [1;2;3] ] 
# or longline = [line, line, 1, 2, 3 ]
#etc...
#currently this is a convenience for quick number matrix e.g. copy from excel
#maybe extend to use ast and to compose, or maybe create a advanced class emat()


#%%singleton_ing
mat=mat()
#%%testing
def testcall():
  mat%()
  mat%(None)
  mat%(1)
  #a(:) #SyntaxError: invalid syntax
#%%

#%%tests1
M=mat._array("""
        
0.342717E-02  ,,,,,, 0.647191E-01
;;;;			\r\n\r\n
;	;; ; ; ;\n\n\n 
     ,		,,,
0.647191E-01 0.201713E+01
""") #string notation, can be copy/pasted from other sources, can use flexible separators

print(M)

M=mat%"""
        
0.342717E-02  ,,,,,, 0.647191E-01
;;;;			\r\n\r\n
;	;; ; ; ;\n\n\n 
     ,		,,,
0.647191E-01 0.201713E+01
"""

print(M)


M=mat._array("1,2,3\n4 5 6")
M=mat._array("1,2,3\r\n4 5 6")
M=mat._array("1	2\t3,4 5;6 7 8 9 10")

print(M)

v=mat._array('1 2 3')
print(v)
v=mat._array('1;2;3')
print(v)
v=mat._array('1 2 3')[0]
print(v)

x="1\t2"
y="1	2"
print(x==y)

x="1\n2"
y="1\r2"

'''y
Out[149]: '1\r2'

print(y)
2'''

z="""1
2"""

w="1\r\n2"
print(x==y)
print(x==z)
print(x==w)



#---


class seq:
    import numpy as np
    
#    def __init__(self,*args):
#        print('obj=a(): init')
#        self.prop=args
#        return
#
#    def __new__(cls,*args):
#        print('obj=a(): new')
#        self=super().__new__(cls)
#        return self



    def __getitem__(self,key): #key or slice (?)
        import numpy as np
        #print('obj(): getitem')
        #print(self.prop)
        #print(key)
        #if key string call array
        #if key slice call range
        if isinstance(key,slice):
            print('slice -> range')
            return self._range(key)
        else:
            #print(type(key))
            if np.isscalar(key):
                print('scalar -> tuple of one item')
                return (key,)
            else:
                print('iterable -> tuple')
                return tuple(key)



    
    def _range(self,_slice):
        #print(_slice)
        start = _slice.start if _slice.start is not None else 0
        stop = _slice.stop if _slice.stop is not None else 100
        step = _slice.step if _slice.step is not None else 1
        #print(start,stop,step)
        return range(start,stop,step)


#%%singleton_ing
seq=seq()
#%%testing

#%%
def testgetitem():
  #a[] #SyntaxError: invalid syntax
  seq[None]
  seq[1]
  seq[:]
  

#%%tests2
r1=seq[1:20:3] #slice notation, can use variables, ...

print(type(r1))
print(r1)

for ri in r1:
    print (ri)
    
#%%tests3

seq[0:8]
#Out[245]: range(0, 8)
#
seq[:8]
#Out[246]: range(0, 8)
#
seq[8,]
#Out[247]: [8]

seq[8]
