from typing import Dict, Iterable, Tuple, List


def t1(inp: int, var2: str) -> bool:
  return len(var2) > inp

assert t1(1, "hello") == True, "This statement should be true"
assert t1(10, "hi") == False, "This should also be true"


from collections import defaultdict, Counter

a = defaultdict(int)

assert a['none'] == 0

a['two'] += 1

assert a['two'] == 1

a = Counter([1, 2, 3, 4,1 , 2, 3,1,2, 3,1 ,1])

print(a)

a = ((z, z*z) for z in range(1000))
print(a)

for i in a:
  print(i)

