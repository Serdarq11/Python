import numpy as np

# Filtering = Refers to the process of selecting elements from an array that match a given condition

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

print(teenagers)    # [17 16 15]
print(adults)    # [21 19 20 30 18 39 22 18 19 20 21]
print(seniors)  # [65 99]
print(evens)    # [20 16 30 18 22 18 20]
print(odds)     # [21 17 19 65 39 15 99 19 21]

# where
adults2 = np.where(ages >= 18, ages, 0)
print(adults2)
#[[21  0 19 20  0 30 18 65]
# [39 22  0 99 18 19 20 21]]
