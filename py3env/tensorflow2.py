# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:59:42 2017

@author: dell
"""
#####sesonr
import tensorflow as tf

matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],[2]])


product = tf.matmul(matrix2,matrix1)


##method 1
#sess = tf.Session()
#result = sess.run(product)
#
#print(result)
#sess.close()

##method 2 自动关上sess
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)



state= tf.Variable(0,name='counter')


#print(state.name)
one = tf.constant(1)

print(one)

new_value=tf.add(state,one)


update = tf.assign(state,new_value)
init = tf.initialize_all_variables()


#这里才是真正的程序运行，其他的只是加载类
with tf.Session() as sess:
    with tf.device("/gpu:1"):
#        sess.run(init)
        for _ in range(3):
            sess.run(update)
            print(sess.run(state))
        
        
#        