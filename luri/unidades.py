'''
%load_ext autoreload
%autoreload 2

from luri import unidades
from luri.unidades import dado, adimensional, unidade, calc
'''
from sympy.parsing.sympy_parser import parse_expr

class escalar(): 
    def __init__(self,x,u):
        self.x=x
        self.u=str( parse_expr(u) )
#         self.h=repr(self)

    def __neg__(self):
        #return -1*self
        other=escalar(-1*self.x,self.u)
        other.h=f'-({self.h})'
        print(f'( {repr(other)} )')
        return other
    
    def __pos__(self): #copy
        #return -1*self
        other=escalar(self.x,self.u)
        other.h=f'{self.h}'
        print(f'( {repr(other)} )')
        return other    
        
    def __repr__(self):
        if abs(self.x)<10_000 and abs(self.x)>1e-2:
            valor=f'{self.x:.3f}'.replace('.',',')
        else:
            valor=f'{self.x:.3e}'.replace('.',',').replace('e','x10^')
        unidade = str(self.u)
        if unidade =='1':
            unidade=''
        return valor+' '+unidade
    
    def __add__(self,other):
        other = self.check_unidades(other)
        
        #conferir unidade e aceitar ou rejeitar soma
        if self.u==other.u:
            ans=escalar(self.x+other.x,self.u)
        else:
            raise ValueError(f'erro de unidades, não posso somar {self.u} com {other.u}')
            
        print(f'{self} + {other} = {ans}')    
        ans.h="("+self.h+")"+" + "+"("+other.h+")"
        return ans
    
    def __sub__(self,other):
        other = self.check_unidades(other)
        
        #conferir unidade e aceitar ou rejeitar soma
        if self.u==other.u:
            ans=escalar(self.x-other.x,self.u)
        else:
            raise ValueError(f'erro de unidades, não posso somar {self.u} com {other.u}')
            
        print(f'{self} - {other} = {ans}')
        ans.h="("+self.h+")"+" - "+"("+other.h+")"
        return ans    
    
    def __mul__(self,other):
        
        other = self.check_unidades(other)

#         print(self)
#         print(other)
        #combinar unidade e tentar cortar
        from sympy.parsing.sympy_parser import parse_expr
        

        
        unidades=parse_expr(self.u+"*"+other.u).cancel()
#         print(unidades)

        s_unidades = self.cancel_unidades(unidades)

        ans = escalar(self.x*other.x, s_unidades )
        
        print(f'{self} x {other} = {ans}')
        ans.h="("+self.h+")"+" x "+"("+other.h+")"
        return ans
    
    def __rtruediv__(self,other):
        other = self.check_unidades(other)
        return(other/self)
    
    def __truediv__(self,other):
        other = self.check_unidades(other)
#         print(self)
#         print(other)
        #combinar unidade e tentar cortar
        from sympy.parsing.sympy_parser import parse_expr
        

        
        unidades=parse_expr(self.u+"/("+other.u+")").cancel()
#         print(unidades)
        s_unidades = self.cancel_unidades(unidades)

        ans = escalar(self.x/other.x, s_unidades)
        
        print(f'{self} / {other} = {ans}')
        ans.h="("+self.h+")"+" / "+"("+other.h+")"
        return ans   
    
    def check_unidades(self,other):
        if not isinstance(other,escalar):
#             print('ops')
            other=escalar(other,"1") #adimensional
            other.h=repr(other)
        return other

    def cancel_unidades(self,unidades):
        s_unidades=str(unidades.cancel())
#         if s_unidades=='1':
#             s_unidades = ''
        return s_unidades

    def __rsub__(self,other):
        other = self.check_unidades(other)
        return (other-self)
    
    def __radd__(self,other):
        other = self.check_unidades(other)
        return other+self
    def __rmul__(self,other):
        other = self.check_unidades(other)
        return other*self    
    
    def __pow__(self,other):
        #other deve ser adimensional
        #se other for inteiro -> fazer multiplicações e propagar unidades
        #se other for fload -> self deve ser admensional também
        
        other = self.check_unidades(other) # se era python, agora é "escalar / adimensional"
        if isinstance(other.x, int):
            ans = escalar(1,'1')
            ans.h=repr(ans)
            print(ans.h,'ok')
            for i in range(other.x):
                ans = ans *self
        else: #float
            if self.u != '1':
                raise ValueError(f'erro de unidades, não posso elevar {self.u} a potência {other.x}')
            else: #adimensional
                ans=escalar(self.x**other.x,'1')

        print(f'{self} ** {other} = {ans}')
        ans.h="("+self.h+")"+" ** "+"("+other.h+")"
        return ans

def check_unidades(other):
    if not isinstance(other,escalar):
#             print('ops')
        other=escalar(other,"1") #adimensional
        other.h=repr(other)
    return other        
    
    
    
def dado(x=1,u='1'):
    y=escalar(x,u)
    print(f'= {y.x} {y.u}')
    y.h=repr(y)
    return y

def unidade(u):
    ans = escalar(1.,u)
    ans.h=repr(ans)
    return ans
uni=unidade

def adimensional(x):
    ans=escalar(x,'1')
    ans.h=repr(ans)
    return ans
num=adimensional

def calc(x):
    print('#>>>')
    printable=(x.h).replace('**','^').replace('*',' ')
    print('= '+printable)
    
    printable2=(f'= {x}').replace('**','^').replace('*',' ')
    print(printable2)
    print('#<<<')
    x.h=repr(x)
    return x

import numpy as np    
def log(var):
    var = check_unidades(var) #gambiarrado
    if var.u != '1':
        raise ValueError(f'erro de unidades, não posso tirar log de {var.u}')
    else: #adimensional
        ans=np.log(var.x)
        ans=escalar(ans,'1')
        print(f'ln({var}) = {ans}')
        ans.h="ln("+var.h+")"
    return ans

def exp(var):
    var = check_unidades(var) #gambiarrado
    if var.u != '1':
        raise ValueError(f'erro de unidades, não posso tirar exp de {var.u}')
    else: #adimensional
        ans=np.exp(var.x)
        ans=escalar(ans,'1')
        print(f'exp({var}) = {ans}')
        ans.h="exp("+var.h+")"
    return ans


# x=dado(1,'cm')
# y=dado(1,'m')
# fac=dado(100,'cm/m')



# print(x) #calls 1 str or 2 repr


'''
        if isinstance(self.u,str):
            if self.u[0]=='k':
                self.x*=1000
                self.u=self.u[1:]
                self=self.__init__(self.x,self.u)
'''


"""
xxx=dado(1,'m')
xxx.h=repr(xxx)
yyy=dado(2,'m')
yyy.h=repr(yyy)
zzz=xxx+yyy+xxx+yyy

zzz.h
"""

print('unidades.py reloaded')


#OLD
# from sympy.parsing.sympy_parser import parse_expr

# class escalar():
#     def __init__(self,x,u):
#         self.x=x
#         self.u=str( parse_expr(u) )

        
#     def __repr__(self):
#         valor=str(self.x)
#         unidade = str(self.u)
#         if unidade =='1':
#             unidade=''
#         return valor+' '+unidade
    
#     def __add__(self,other):
#         other = self.check_unidades(other)
        
#         #conferir unidade e aceitar ou rejeitar soma
#         if self.u==other.u:
#             ans=escalar(self.x+other.x,self.u)
#         else:
#             raise ValueError(f'erro de unidades, não posso somar {self.u} com {other.u}')
            
#         print(f'{self} + {other} = {ans}')    
#         return ans
    
#     def __sub__(self,other):
#         other = self.check_unidades(other)
        
#         #conferir unidade e aceitar ou rejeitar soma
#         if self.u==other.u:
#             ans=escalar(self.x-other.x,self.u)
#         else:
#             raise ValueError(f'erro de unidades, não posso somar {self.u} com {other.u}')
#         return ans    
    
#     def __mul__(self,other):
        
#         other = self.check_unidades(other)

# #         print(self)
# #         print(other)
#         #combinar unidade e tentar cortar
#         from sympy.parsing.sympy_parser import parse_expr
        

        
#         unidades=parse_expr(self.u+"*"+other.u).cancel()
# #         print(unidades)

#         s_unidades = self.cancel_unidades(unidades)

#         ans = escalar(self.x*other.x, s_unidades )
        
#         print(f'{self} x {other} = {ans}')
#         return ans
    
#     def __truediv__(self,other):
#         other = self.check_unidades(other)
# #         print(self)
# #         print(other)
#         #combinar unidade e tentar cortar
#         from sympy.parsing.sympy_parser import parse_expr
        

        
#         unidades=parse_expr(self.u+"/("+other.u+")").cancel()
# #         print(unidades)
#         s_unidades = self.cancel_unidades(unidades)

#         ans = escalar(self.x/other.x, s_unidades)
        
#         print(f'{self} / {other} = {ans}')
#         return ans   
    
#     def check_unidades(self,other):
#         if not isinstance(other,escalar):
# #             print('ops')
#             other=escalar(other,"1") #adimensional
#         return other

#     def cancel_unidades(self,unidades):
#         s_unidades=str(unidades.cancel())
# #         if s_unidades=='1':
# #             s_unidades = ''
#         return s_unidades

#     def __rsub__(self,other):
#         return -1*(self-other)
#     def __radd__(self,other):
#         return self+other
#     def __rmul__(self,other):
#         return self*other    
    
#     def __pow__(self,other):
#         #other deve ser adimensional
#         #se other for inteiro -> fazer multiplicações e propagar unidades
#         #se other for fload -> self deve ser admensional também
        
#         other = self.check_unidades(other) # se era python, agora é "escalar / adimensional"
#         if isinstance(other.x, int):
#             ans = escalar(1,'1')
#             for i in range(other.x):
#                 ans = ans *self
#         else: #float
#             if self.u != '1':
#                 raise ValueError(f'erro de unidades, não posso elevar {self.u} a potência {other.x}')
#             else: #adimensional
#                 ans=escalar(self.x**other.x,'1')

#         return ans

        
    
    
    
# def dado(x=1,u='1'):
#     y=escalar(x,u)
#     print(f'<< {y.x} {y.u}')
#     return y

# def unidade(u):
#     return escalar(1.,u)
# uni=unidade

# def adimensional(x):
#     return escalar(x,'1')
# num=adimensional

# x=dado(1,'cm')
# y=dado(1,'m')
# fac=dado(100,'cm/m')

# # print(x) #calls 1 str or 2 repr


# '''
#         if isinstance(self.u,str):
#             if self.u[0]=='k':
#                 self.x*=1000
#                 self.u=self.u[1:]
#                 self=self.__init__(self.x,self.u)
# '''
