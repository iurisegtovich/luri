'''
empty module1
'''

print('loading mod1')
print('run "dir(mod1)" to see contents')

class a:
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

    def __call__(self,arg):
        import numpy as np
        #print('obj(): called')
        #print(self.prop)
        #print(args)
        if isinstance(arg,str):
            return self._array(arg)
        return

    def __getitem__(self,key): #key or slice (?)
        import numpy as np
        #print('obj(): getitem')
        #print(self.prop)
        #print(key)
        #if key string call array
        #if key slice call range
        if isinstance(key,slice):
            return self._range(key)
        else:
            #print(type(key))
            if np.isscalar(key):
                return (key,)
            else:
                return tuple(key)


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
    
    def _range(self,_slice):
        #print(_slice)
        start = _slice.start if _slice.start is not None else 0
        stop = _slice.stop if _slice.stop is not None else 1
        step = _slice.step if _slice.step is not None else 1
        #print(start,stop,step)
        return range(start,stop,step)


#%%singleton_ing
a=a()
#%%testing
def testcall():
  a()
  a(None)
  a(1)
  #a(:) #SyntaxError: invalid syntax
#%%
def testgetitem():
  #a[] #SyntaxError: invalid syntax
  a[None]
  a[1]
  a[:]
  
#%%tests1
M=a._array("""
        
0.342717E-02  ,,,,,, 0.647191E-01
;;;;			\r\n\r\n
;	;; ; ; ;\n\n\n 
     ,		,,,
0.647191E-01 0.201713E+01
""") #string notation, can be copy/pasted from other sources, can use flexible separators

print(M)

M=a("""
        
0.342717E-02  ,,,,,, 0.647191E-01
;;;;			\r\n\r\n
;	;; ; ; ;\n\n\n 
     ,		,,,
0.647191E-01 0.201713E+01
""")

print(M)


M=a._array("1,2,3\n4 5 6")
M=a._array("1,2,3\r\n4 5 6")
M=a._array("1	2\t3,4 5;6 7 8 9 10")

print(M)

v=a._array('1 2 3')
print(v)
v=a._array('1;2;3')
print(v)
v=a._array('1 2 3')[0]
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

#%%tests2
r=a[1:20:3] #slice notation, can use variables, ...

print(type(r))
print(r)

for ri in r:
    print (ri)
    
#%%tests3

a[0:8]
#Out[245]: range(0, 8)
#
a[:8]
#Out[246]: range(0, 8)
#
a[8,]
#Out[247]: [8]

a[8]
