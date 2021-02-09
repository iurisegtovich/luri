# luri
lib_iuri (luri)

## installation:

> quick (with git):

pip install git+https://github.com/iurisegtovich/luri
#pip list
#luri                               0.0.2               
#pip uninstall luri

> quick (without git)

pip install https://github.com/iurisegtovich/luri/archive/master.zip
#pip list
#luri                               0.0.2               
#pip uninstall luri

> dev mode (git required):

git clone https://github.com/iurisegtovich/luri luri-master

pip install -e ./luri-master

#pip list
#>>> luri                               0.0.2               /home/segtovichisv/Desktop/luri-master
#pip uninstall luri

> or

pip install -e git+https://github.com/iurisegtovich/luri#egg=luri_iurisegtovich
#pip list
#luri                               0.0.2               /home/segtovichisv/Desktop/projeto_xxx/src/luri-iurisegtovich
#pip uninstall luri

> from pypi test

python -m pip install --index-url https://test.pypi.org/simple/luri-iurisegtovich

## usage

> as a standalone program
python -m luri
#this is the name of the directory neighbor to setup.py, cointaining __init__.py and __main__.py; one might call it luri_pkg even though the setup name in setup.py and showing up in pip list is plain "luri"

'''
(base) segtovichisv@luos1604:/mnt/storage/github/luri_master$ python -m luri
    __init__.py running
    it' s not very effective
    __main__.py running
    nada acontece feijoada
'''

> import package
import luri

'''
(base) segtovichisv@luos1604:/mnt/storage/github/luri_master$ python
    >>> import luri
    __init__.py running
    it' s not very effective
'''

> import modules
from luri import mod1

'''
>>> from luri import mod1
loading mod1
run "dir(mod1)" to see contents
'''

> import classes

from luri.mod1 import clas1
obj1=clas1()
'''here is your new object of the class clas1'''
obj2=clas1()
'''here is your new object of the class clas1'''
obj3=clas1()
'''here is your new object of the class clas1'''

> more tests

from luri.aux.mod2 import clas2 [ok]

python -m luri.aux [ok]

from luri import test_aux [ok]




