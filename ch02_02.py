import numpy as np
'''
* XOR 게이트

x1 => NAND연산 => s1 \
                    => AND연산 => y
x2 => OR연산 => s2  /

* XOR 게이트 진리표

    x1 x2 | s1 s2 | y
    =================
    0  0  | 1  0  | 0
    1  0  | 1  1  | 1
    0  1  | 1  1  | 1
    1  1  | 0  1  | 0

NAND연산은 AND의 반대(not AND 의미)
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


def NAND(x1, x2):
    X = np.array([x1, x2])
    W = np.array([-0.5, -0.5])
    bias = 0.7 # 편향 : 한쪽으로 치우쳐 균형을 깬다는 의미
    theta = 0

    tmp = np.sum(W*X) + bias

    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def OR(x1, x2):
    X = np.array([x1, x2])
    W = np.array([0.5, 0.5])
    bias = -0.2 # 편향 : 한쪽으로 치우쳐 균형을 깬다는 의미
    theta = 0

    tmp = np.sum(W*X) + bias

    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print( XOR(0,0) )
print( XOR(0,1) )
print( XOR(1,0) )
print( XOR(1,1) )
