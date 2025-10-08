# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = 'Serdar Kaya'
age = 22
gpa = 3.36
is_student = True

# print(type(name))   # <class 'str'>
# print(type(age))    # <class 'int'>
# print(type(gpa))    # <class 'float'>
# print(type(is_student)) # <class 'bool'>

gpa = int(gpa)  # 3 now
print(gpa)

age = float(age)    # 22.0 now
print(age)

age = str(age)  # 22.0, however it is a string not a float
print(age)

name = bool(name)   # True, because it is not an empty string
print(name)
