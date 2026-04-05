list = ['item1', 'item2', 'item3']
list2 = [12, 33, 45, 58, 23]

print(list)
# negative indexing can access elements starting from the end
print(list2[-1])

# select a subset of a list
print(list2[2:4])

# gets the length of a list
print(len(list2))

#add items to list
list.append('item4')

#remove item from list
item4 = list.pop()

#copy list
list3 = list2.copy()

# list comprehension, lets you create new lists from existing lists

num = [ 1, 2, 3, 4]
doubled = [n*2 for n in num]
print(doubled) # [ 2, 4, 6, 8]
odd = [ n for n in num if n%2 == 1]
print(odd) # [ 1, 3]

# unpacking a list, lets you create variables from items in the list
num = [ 1, 2, 3, 4]
[first, second, *rest] = num
print(first)
print(second)
print(rest)
# joining lists
num2 = [5, 6]
num3 = num + num2
print(num3) # [1, 2, 3, 4, 5, 6]

# copying lists
num4 = num2.copy()
print(num4)