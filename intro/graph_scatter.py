from matplotlib import pyplot as plt

data = {
  'a': {
    'friends': 70,
    'minutes': 175
  },
  'b': {
    'friends': 65,
    'minutes': 170
  },
  'c': {
    'friends': 72,
    'minutes': 205
  },
  'd': {
    'friends': 63,
    'minutes': 120
  },
  'e': {
    'friends': 71,
    'minutes': 220
  }
}

fr = [f['friends'] for k, f in data.items()]
mi = [f['minutes'] for k, f in data.items()]
plt.scatter(fr, mi)

for name, person in data.items():
  plt.annotate(
      name,
      xy=(person['friends'], person['minutes']),
      xytext=(5, -5),
      textcoords='offset points'
    )

plt.title("Minutes vs Friends")
plt.xlabel("Friends")
plt.ylabel("Minutes")
plt.savefig("scatter.png")

