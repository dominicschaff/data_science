from matplotlib import pyplot as plt

things = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
counts = [5, 3, 7, 1, 3]

plt.bar(range(len(things)), counts)

plt.title("Counts of things")
plt.ylabel("# of Things")

plt.xticks(range(len(things)), things)

plt.savefig("bar.png")

