i = 1
while i < 10:
    print(i)
    i+=1
else:
    print("This is run when the loop condition is no longer met")

# iterating an iterable such as a list
list = ["bob", "sally", "john"]
for j in list:
    print(j)

# iterating between custom range an increment
for i in range(0, 10, 2):
    print(i)

#using break and continue to control the flow of loops
while(True):
    if (i == 11):
        break
    print(i)
    i+=1
    if (i <12):
        continue
    print("This will never be printed")
