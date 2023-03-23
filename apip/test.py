import random

lst = []

while len(lst) != 8:
    st = random.choice(("H", "T")) + random.choice(("H", "T")) + random.choice(("H", "T"))
    if not st in lst:
        lst.append(st)

print(lst)