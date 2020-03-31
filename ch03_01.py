import numpy as np
import matplotlib.pyplot as plt
'''
다중퍼셉트론으로 복잡한 처리 가능
but 가중치 설정은 인간이 수동으로 해야함
=> 신경망 학습을 통해 자동으로 가중치 설정 가능


* active function 활성함수 예
    - step function 계단함수
    - sigmoid function

'''

def step_function(x):
    y = x > 0
    return y.astype(np.bool) # np 배열의 자료형을 bool타입으로 변환 , np.int로 가능

x = np.array([-1.0, 1.0, 2.0])

print(step_function(x))
# [False  True  True]

def step_function2(x):
    return np.array( x > 0, dtype = np.int )

x = np.arange(-5.0, 5.0, 0.1)
y = step_function2(x)

plt.plot(x, y)
plt.xlim(-5, 5)
plt.ylim(-0.1, 1.1) # y축 범위 지정
plt.show()


'''
* 기계학습문제는 2개로 나뉨
    -분류 : 데이터가 어느 class에 속하느냐
    -회귀 : input데이터의 (연속적인)수치 예측

* 회귀 : 19세기 영국 우생학자 프랜시스 골턴,
    완두콩 키 실험
    키가 큰 부모의 자식은 부모보다 작고, 작은 부모의 자식은 부모보다 큰, 즉 평균으로 회귀(regression)하는 경향이 있음 발견
    선형관계가 있어 예측 가능
'''

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def ReLU(x):
    return np.maximum(0, x)

y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y축 범위 지정
plt.show()

y = ReLU(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y축 범위 지정
plt.show()

# exp(x): 지수함수 exponential function (e는 자연상수)

'''
103p

* 배치처리 batch : (ex)이미지 데이터를 지폐처럼 여러 다발로 묶는것(묶음) 이를통해 이미지 1장당 처리시간 대폭 줄임
    - 배치처리를 수행함으로써 큰 배열로 이루어진 계산을 하게되는데
    컴퓨터에서는 큰배열을 한꺼번에 계산하는것이
    분할된 작은 배열들을 여러번 계산하는 것보다 빠름

    1. 수치 계산 라이브러리가 큰 배열을 효율적으로 처리하도록 최적화되어있기 때문
    2. 신경망에서 데이터 전송이 병목으로 작용함
    배치처리를 해서 버스에 주는 부하를 줄인다는 것
    (느린 I/O를 통해 데이터 읽는 횟수가 줄어, 빠른 GPU로 순수 계산을 수행하는 비율이 높아짐)

'''
