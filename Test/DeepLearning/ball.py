import tensorflow as tf
sess = tf.Session()
a = tf.constant(10)
b = tf.constant(22)
print(sess.run(a + b)) #32
import keras