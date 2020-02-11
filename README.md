# luri
lib_iuri (luri)

## installation:

> quick:

pip install git+https://github.com/iurisegtovich/luri

> without git

pip install https://github.com/iurisegtovich/luri/archive/master.zip

> dev mode:

git clone https://github.com/iurisegtovich/luri

pip install -e ./luri

## usage

> as a standalone program
python -m luri

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




