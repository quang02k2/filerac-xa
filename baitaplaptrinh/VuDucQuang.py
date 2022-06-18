
import numpy as np
def readfile(namefile):
    try:
        with open(namefile, mode='r') as f:
            x = []
            while True:
                line = f.readline()
                if not line: break
                x.append(line.split())
            return np.array(x)
    except:
        print('File khon ton tai')
        return


def distance(x1, x2):
    k = 0.0
    if len(x1) == len(x2):
        for i in range(len(x1)):
            k += (x1[i] - x2[i]) ** 2
        return k
    else:
        print('Tính khoảng cách Euclidean lỗi')


def distancetoall(x_train, test):
    dis = np.zeros(len(x_train))
    for i in range(len(x_train)):
        dis[i] = distance(x_train[i], test)
    return dis


def predict(dis, lable):
    m = min(dis[np.where(dis > 0)])
    minpos = np.where(dis == m)[0][0]
    return lable[minpos]


def train_test(file):
    x_train = readfile(file)
    lable = x_train[:, len(x_train[0]) - 1]
    x_train = x_train[:, 4:len(x_train[0]) - 1]
    x_train = x_train.astype(float)
    return x_train, lable

def main():
    filename1 = 'D:/kddcup.data'
    filename2 = 'D:/kddcup.test'
    print('Đang đọc tệp', filename1, end='')
    x_train,lable = train_test(filename1)
    print("Done")
    print('\t', filename1, x_train.shape)
    print('Đang đọc tệp', filename2, end='')
    x_test, lable_test = train_test(filename2)
    print('Done')
    print('\t', filename2, x_test.shape)
    pos = int(input('Nhập bản ghi muốn dự báo lớp: '))
    if pos < 0 or pos >= len(x_test):
        print('\tVị trí của bản ghi không hợp lệ!')
    else:
        print('\tVị trí của bản ghi hợp lệ!')
        print('Đang tính khoảng cách.................', end='')
        test = x_test[pos]
        dis = distancetoall(x_train, test)
        print('Done')
        print('Lớp của dữ liệu: ', predict(dis, lable))

main()




































































