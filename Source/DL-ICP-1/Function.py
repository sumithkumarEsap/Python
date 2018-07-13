import tensorflow as tf
#creaated a matrix to store values of a
a=tf.constant([[3,6],[1,2]])

#creaated a matrix to store values of b
b=tf.constant([[2,2],[2,2]])

#creaated a matrix to store values of c
c=tf.constant([[4,5],[3,2]])
#multiplying matrix a,a
x=tf.matmul(a,a)

#adding the result x to b
y=tf.add(x,b)
#multiplying the result y to c
z=tf.matmul(y,c)
#running a session on z
with tf.Session() as sess:
   # print(sess.run(x))
    z=sess.run(z)
    print(z)