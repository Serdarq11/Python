# for loop = used to iterate over a sequence (string, list, tuple, set)
#            repeat a block of code an exact amount of times

import time

for i in range(1, 11, 2):      # 1 to 10   -> 1 is inclusive, 11 is exclusive, 2 is the step
    print(i)

name = "Serdar"

for letter in name:
    print(letter, end="-")        # letters of name will be iterated one by one -> S-e-r-d-a-r-

print("")

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print("Happy new year!")

