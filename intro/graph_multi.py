from matplotlib import pyplot as plt

line1 = [x**2 for x in range(13)]
line2 = [x**3 for x in range(13)]
line3 = [y - x for x, y in zip(line1, line2)]

xs = [i for i in range(len(line1))]

plt.plot(xs, line1, 'g-', label='line1')
plt.plot(xs, line2, 'r-.', label='line2')
plt.plot(xs, line3, 'b:', label='line3')

plt.legend(loc=9) # top middle
plt.xlabel("Number")
plt.xticks([]) # remove the ticks
plt.title("Lines and diff")

plt.savefig("multi-line.png")
