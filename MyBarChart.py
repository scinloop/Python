# 柱状图
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
# 设置中文字体
plt.rcParams['axes.unicode_minus'] = False
# 设置负号显示

y1 = [32, 25, 16, 30, 45, 37]
y2 = [-32, -25, -16, -30, -45, -37]

plt.bar(range(len(y1)), y1, width=1, facecolor='green', edgecolor='white', label='统计1')
plt.bar(range(len(y2)), y2, width=1, facecolor='blue', edgecolor='white', label='统计2')

plt.suptitle("柱状图", fontsize=20)

plt.legend()
plt.show()
