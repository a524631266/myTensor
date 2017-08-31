# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 10:07:34 2017

@author: dell
"""

import tensorflow as tf

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1,input2)

with tf.Session() as sess:
     print (sess.run(output,feed_dict={input1:[8.0],input2:[9.0]}))
#     output)
