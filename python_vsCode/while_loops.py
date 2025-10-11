# while loop = used to repeat a block of code as long as a condition remains a 'True'
#              we re-check the condition at the end of the loop

name = input("Enter your name: ")

while name == "":
    name = input("Enter your name: ")

age = int(input("Enter your age: "))

while age < 0:
    print("Your age cannot be less than zero")
    age = int(input("Enter your age: "))

print(f"Hello {name}!")
print(f"You are {age} years old!")