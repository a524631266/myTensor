# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:31:44 2017

@author: dell
"""

from functools import reduce
from operator import mul
aa=map(lambda x: x**2,[1,2,3,4,5])
even=filter(lambda x: x & 1 == 0,[1,2,3,4,5])
pro=reduce(lambda x,y: x*y,[1,2,3,4],[1,10])
