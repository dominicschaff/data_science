from matplotlib import pyplot as plt

t1 = [99, 90, 85, 97, 80]
t2 = [100, 85, 60, 90, 70]

plt.scatter(t1, t2)

plt.xlabel("test 1")
plt.ylabel("test 2")

plt.title("NotComparable")
plt.savefig("scatter_comparable_not.png")

plt.axis("equal")
plt.title("Comparable")
plt.savefig("scatter_comparable_equal.png")
