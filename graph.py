import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "SimHei"
# 画图 imgsize 代表大小 FaceColor为背景颜色
fig = plt.figure(facecolor="lightgrey")
# 划分区域
plt.subplot(2, 2, 1)
plt.title("1号")
plt.subplot(2, 2, 2)
plt.title("2号", loc="left", color="b")
plt.subplot(2, 2, 3)
MyFontDict = {"fontsize": 12, "color": "green", "rotation": 30}
plt.title("3号", fontdict=MyFontDict)
plt.subplot(2, 2, 4)
plt.title("4号", color='white', backgroundcolor="black")
plt.suptitle("MyTables", fontsize=20, color="red", backgroundcolor="yellow")
# plt.plot()
plt.tight_layout()  # 使得图表与标题不再重叠
plt.show()
