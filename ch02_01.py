import numpy as np

'''
퍼셉트론: 다수 신호 input > 하나의 신호 output

if(w1x1 + w2x2 > 세타(임계값)):
    y = 1
    return y
'''

'''
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = w1*x1 + w2*x2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

print(AND(1,1)) # 1
print(AND(1,0)) # 0
'''

def AND(x1, x2):
    X = np.array([x1, x2])
    W = np.array([0.5, 0.5])
    bias = -0.7 # 편향 : 한쪽으로 치우쳐 균형을 깬다는 의미  
    theta = 0

    tmp = np.sum(W*X) + bias

    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

print(AND(1,1)) # 1
print(AND(1,0)) # 0
