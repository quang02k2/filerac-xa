import numpy as np


def readfile(f):

    with open(f,mode='r', encoding='utf-8') as f:
        data = []
        a = f.read().split('\n')[:-1]
        for i in a:
            data.append(i.split('\t'))
    return np.array(data)


def distance(row1, row2):
    d1 = (row1-row2)**2
    d2 = sum(d1)**0.5
    return d2


def distancetoall(row,x):
    return np.array(distance(row, x[i]) for i in range(len(x)))


def division(x):
    x_train = x[:, 4:]
    lable = x[:,-1]
    try:

        x_train = np.reshape(x_train,-1)
        x_train.astype(float)
        print('ok bândsfsdfas',x_train)
    except:

        print(ValueError,'ko dk ')
    return x_train.astype, lable


def predict(lable,test):
    return lable[test.index(min(test))]




f = 'D:/kddcup.data'
data1 = readfile(f)
print(data1)
x_train, lable = division(data1)
print(x_train)
print(lable)

f = 'D:/kddcup.test'
data = readfile(f)
print(data)
x_test, x = division(data)
print(x_test)




























