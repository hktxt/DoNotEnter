from numpy import *
import operator

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]  #读取矩阵的长度，shape[0]就是读取矩阵第一维度的长度。dataSetSize = 4
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet #输入[0， 0]与其的差
    sqDiffMat = diffMat ** 2 #差值的各元素平方
    #print sqDiffMat
    sqDistances = sqDiffMat.sum(axis = 1) #平方和. 按行相加，这里sqDistances = [ 2.21  2.    0.    0.01]
    distances = sqDistances ** 0.5 #开方就是距离，欧式距离 [ 1.48660687  1.41421356  0.          0.1       ]
    sortedDistIndicies = distances.argsort() #argsort函数返回的是数组值从小到大的索引值[2 3 1 0],http://blog.csdn.net/maoersong/article/details/21875705
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1 #字典操作classCount = {'A': 1, 'B': 2}
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True) #排序 反序
    #sortedClassCount = [('B', 2), ('A', 1)]
    return sortedClassCount[0][0]

group, labels = createDataSet()
print classify0([0, 0], group, labels, 3)

"""
1. shape函数是numpy.core.fromnumeric中的函数，它的功能是读取矩阵的长度，比如shape[0]就是读取矩阵第一维度的长度。http://jingyan.baidu.com/article/a24b33cd5c90b319fe002b9e.html
2. tile函数位于python模块 numpy.lib.shape_base中，他的功能是重复某个数组。比如tile(A,n)，功能是将数组A重复n次，构成一个新的数组.http://jingyan.baidu.com/article/219f4bf7da4d8dde442d389e.html
3. .sum()函数是模块numpy的一个函数：默认axis为None，表示将所有元素的值相加,对于二维数组,axis=1表示按行相加 , axis=0表示按列相加
4.
sorted()函数：
a = {'A': 1, 'B': 2, 'C': 0}
print sorted(a.iteritems(), key = operator.itemgetter(0), reverse = True)
>>>[('C', 0), ('B', 2), ('A', 1)]

a = {'A': 1, 'B': 2, 'C': 0}
print sorted(a.iteritems(), key = operator.itemgetter(1), reverse = True)
>>>[('B', 2), ('A', 1), ('C', 0)]

"""