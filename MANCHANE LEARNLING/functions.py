import numpy as np




def predict(X,Thenta):
    return X@ Thenta

def computeCost(x,y,Thenta):
    predicted = predict(x,Thenta)
    sqr_error = (predicted-y)**2

    sum_error = np.sum(sqr_error)

    m = np.size(y)
    j = (1/(2*m))* sum_error
    return j

def computerCOST_VEC(x,y,Thenta):
    error = predict(x,Thenta)
    m = np.size(y)
    j = (1/(2*m))*np.transpose(error)@error
    return j


# alpha la gai tri mac dinh = 0,02
# inter la vong lap la 5000 lan
def GradientDescent(x,y,alpha=0.02,inter= 5000):
    # giá trị ban đầu của Thenta  = 0
    # số lượng Thenta bằng số cột x
    Thenta = np.zeros(np.size(x,1))

    # array lưu lại các giá trị của j trong quá trình lặp
    j_hist = np.zeros((inter,2))
    # kích thước là inter*2, cột đầu chỉ là các số từ 1 đến inter đê tiện cho việc plot.
    # kích thước được truyền vào qua một tupplr
    m = np.size(y)
    # ma trận ngược đảo( hàng cà cột) của x
    X_T = np.transpose(x)

    # biến tmaj thời để kiêm tra tiến độ Gradient Descent
    pre_cost = computeCost(x,y,Thenta)


    for i in range(0,inter):

        error = predict(x,Thenta) - y
        Thenta = Thenta - (alpha/m)*(X_T@ error)

        cost = computeCost(x,y,Thenta)
        if np.round(cost,15) == np.round(pre_cost):
            print('reach optima at I = %d ; j = %.6f'%(i,cost))
            j_hist[i:,0] = range(i,inter)
            j_hist[i:,1] = cost
            break
        pre_cost = cost
        j_hist[i,0] = i
        j_hist[i,1] = cost
    yield Thenta
    yield j_hist












