#basic function
def add(a, b):
    return a + b

def printPerson(name, age, height):
    print(name, age, height)

# you can specify arguments in any order if they are named
printPerson(age=12, name='bob', height=5)

#default arguments are used when they are not given in the function call
def sayHello(fname, lname='Smith'):
    print('Hello '+fname + ' ' + lname)

sayHello('John')

sayHello('Bill', 'Young')

# functions can return multiple values
def multiReturnFunc(a,b):
    return a+b, a-b, a*b, a/b

# You can assign multiple variables to the values being returned by the function
numSum, numDiff, numMult, numDiv = multiReturnFunc(10,5) 
print(numSum, numDiff, numMult, numDiv)

def cool(main_num):
    num=34
    
    def add_num():
        print(f'num is {num} and adding 2 to it gives {num+2}')
    
    def sub_num():
        nonlocal main_num
        main_num-=num
        return main_num
    
    add_num()
    return sub_num()

print(cool(10))