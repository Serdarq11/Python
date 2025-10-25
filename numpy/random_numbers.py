import numpy as np

rng = np.random.default_rng(seed=1)     # if we type seed=1, it will always give me the same array

print(rng.integers(low=1, high=101, size=3))    # [48 52 76]
print(rng.integers(low=1, high=101, size=(3, 2)))
# [[96  4]
#  [15 83]
#  [95 25]]

np.random.seed(seed=1)

print(np.random.uniform())  # it will give me random float number between 0 and 1
print(np.random.uniform(low=-1, high=1))
print(np.random.uniform(low=-1, high=1, size=3))    # [-0.49595868 -0.7143175   0.54138483]

print(np.random.uniform(low=-1, high=1, size=(3, 2)))
# [[ 0.9320919  -0.31466577]
#  [-0.82528992  0.76873026]
#  [-0.17395118  0.67458301]]

# shuffle an array
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)    # [3 4 2 5 1]

fruits = np.array(["🍎", "🍊", "🍌", "🥥", "🍍"])
fruits = rng.choice(fruits, size=3)
print(fruits)   # ['🍍' '🍊' '🍌'] -> choose randomly

fruits = rng.choice(fruits, size=(3, 3))
print(fruits)
# [['🍊' '🍊' '🍍']
#  ['🍍' '🍌' '🍌']
#  ['🍌' '🍊' '🍌']]


