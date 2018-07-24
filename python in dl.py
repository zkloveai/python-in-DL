import numpy as np

1.shape，它的功能是查看矩阵或者数组的维数。
x = np.array([[1,2,5],[2,3,5],[3,4,5],[2,3,6]])
# 输出数组的行和列数
print x.shape  # (4, 3)
# 只输出行数
print x.shape[0] # 4
# 只输出列数
print x.shape[1] # 3

2.reshape,主要作用将数组进行变形
X_flatten1 = X.reshape(X.shape[0],-1).T  #X_flatten为列向量，将X所有的元素排成一列，-1的意思是适应行数
X_flatten2 = X.reshape(3,-1).T           #X_flatten为列向量，将X所有的元素排成三列，-1的意思是适应行数

3.
np.dot(A, B)： 对于秩为1的数组，执行对应位置相乘，然后再相加；对于秩不为1的二维数组，执行矩阵乘法运算；超过二维的可以参考numpy库介绍

4.
np.multiply(A,B)  数组和矩阵对应位置相乘，输出与相乘数组/矩阵的大小一致

5. 
np.zeros((A, B)) A*B的矩阵/数组 双括号！！

6.
for i in range(1,L)    循环从1到L-1

7.
list.append(obj)  用于在列表末尾添加新的对象。