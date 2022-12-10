import matplotlib.pyplot as plt

x1 = [2, 4, 5, 6]
y1 = [2, 3, 6, 7]
plt.plot(x1, y1, label = 'line1')

x2 = [1, 2, 4, 5]
y2 = [1, 4, 6, 7]
plt.plot(x2, y2, label = 'line2')

plt.xlabel('X Axis')
plt.xlabel("Y Axis")
plt.title('Demo Graph')
plt.legend()

plt.show()