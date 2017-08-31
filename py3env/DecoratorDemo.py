# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 11:09:10 2017

@author: dell
"""
import itertools,functools
def connect_db():
    print('connect db')

def close_db():
    print ('close db')
    
def router(url):
    print ("asdadd%s"%url)
    def query_data(query):
        
        #装饰器：装饰一个函数，用别名来代替
        def wrapper(aa):
            connect_db()
            #
            query(aa)
        
            close_db()
        #修改装饰器名字
        wrapper.__name__=query.__name__
        return wrapper
        
    return query_data
#返回一个函数来做修改
#query_user=query_data(query_user)
#使用装饰器见上方

@router("/file")
def query_user(count):

#    connect_db()
    print ('query the user %d'%count)
#    close_db()


#query_user(3)


def testWrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print(333333333333333333)
        f = func(*args, **kw)
        for item in f:
            print(4444444444444444444)
            yield 'wrap:' + str(item)
    
    return wrapper

@testWrapper
def test():
    print(11111111111111)
    for i in range(10):
        print(2222222222222222)
        yield i
for x in test():
    print (x)