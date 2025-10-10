# list [] = mutable, most flexible
# tuple () = immutable, faster
# set {} = mutable (add/remove), unordered, NO duplicates, best for membership testing

fruits = ["apple", "orange", "banana", "coconut"]

# fruits[0] = "pineapple"    -> changing first index value  -> A tuple does not support it and gives an error
# fruits.append("mango")     -> mango added as last element -> again a tuple does not support it
# fruits.remove("banana")    -> banana will be removed      -> again a tuple does not support it
# fruits.pop(0)              -> remove apple                -> again a tuple does not support it
# fruits.clear()             -> remove all the elements     -> again a tuple does not support it

for fruit in fruits:
    print(fruit, end=" ")   # apple orange banana coconut 

# in sets, since it is unordered, we cannot assign an index for specific fruit e.g, fruits[0] = pineapple
# since it is unordered, every time we iterate the loop, we get different order of fruits
# we cannot use append but we can use add method. Same for for remove, but we cannot use pop
# basically we can't play with indices
# we cannot add more than one element, I mean we can but it does not effect to the list and takes just one

print() # skip the default line as we use end="" above

fruit = input("Enter a fruit to search for: ")

if fruit in fruits:                 # used for membership testing to search an element in the set
    print(f"{fruit} was found")
else:
    print(f"{fruit} was not found")
