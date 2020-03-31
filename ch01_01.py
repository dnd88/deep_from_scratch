import numpy as np


'''
[1,2,3] : 원소 3개짜리 1차원 배열,
원소별 : element-wise,
원소별 곱셈 : element-wise product

'''
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])

# element-wise product
z = x * y
print(z)
# 출력 [ 2.  8. 18.]

'''
np.array는 N차원 배열 작성 가능
1차원 : vector
2차원 : matrix
라고 부름, 벡터와 행렬을 일반화한 것을 텐서라 함 tensor
'''

# 브로드캐스트 : (스칼라값(수치하나)과 배열의 산술연산)
A = np.array([[1,2], [3,4]])
B = np.array([10])

print(A * B)
print(A * 10)
'''
결과값
[[10 20]
 [30 40]]
'''
# 형상
print(A.shape)
# 원소 데이터타입
print(A.dtype)

X = np.array([[1,1],[2,2],[3,3]])
print(X.shape)
# 3X2행렬 (3,2)

# 원소접근 행먼저, 열다음
print(X[2][1])
