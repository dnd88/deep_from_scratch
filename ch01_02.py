import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,5,0.1) #0~5 까지 0.1간격으로 생성
y1 = np.sin(x)
y2 = np.cos(x)

'''
plt.plot(x, y1) # 그래프 그리기
plt.show() # 그래프 화면에 출력
'''

plt.plot(x, y1, label='sin')
plt.plot(x, y2, label='cos', linestyle='--') # 점선으로 그리기

plt.xlabel('x axis') # x축이름
plt.ylabel('y axis')

plt.title('sin & cos') # 제목
plt.legend()
plt.show()
