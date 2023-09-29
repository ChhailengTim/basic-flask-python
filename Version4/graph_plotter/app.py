import matplotlib.pyplot as plt

left = [2, 4, 5, 6]
height = [2, 3, 6, 6]

# Adjust tick_label to have the same number of elements as left and height
tick_label = ['one', 'two', 'three', 'four']

plt.bar(left, height, tick_label=tick_label, width=0.8, color=['blue', 'orange'])

plt.ylim(1, 8)
plt.xlim(1, 8)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Demo Graph - Bar Chart')

plt.show()
