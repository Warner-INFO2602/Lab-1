name = "bobby"
nameType = type(name) 
print(nameType) # This should indicate that the variable is a string (<class 'str'>)


age = 12
ageType = type(age)
print(ageType) # This should indicate that the variable is an integer (<class 'int'>)


height = 6.5
heightType = type(height)
print(heightType) #<class 'float'>

hasDate = False
hasDateType = type(hasDate)
print(hasDateType) #<class 'bool'>

comp = 7j 
compType = type(comp)
print(compType) # <class 'complex'>

# using fstrings for interpolation
message = f'Hi my name is {name} I am {age} years old'
print(message) # ‘Hi my name is bobby I am 12 years old'

# type casting to convert types
intHeight = int(height) # 6
strHeight = str(height) # '6'
floatHeight = float(intHeight) # 6.0 