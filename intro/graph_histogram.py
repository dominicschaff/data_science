from matplotlib import pyplot as plt
from collections import Counter
from random import randint

grades = [randint(0, 101) for _ in range(100)]

histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()], histogram.values(), 10, edgecolor=(0, 0, 0))

plt.axis([-5, 105, 0, max(histogram.values()) + 2 ])

plt.xticks([10 * i for i in range(11)])

plt.xlabel("Bucket")
plt.ylabel("# of Students")
plt.title("Distribution of Marks")
plt.savefig("histogram.png")
