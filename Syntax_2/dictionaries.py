mydict = {
        "name":"bob",
        "age": 34
}

print(mydict)

# assessing a key
print(mydict['age'])

# adding a new key and value
mydict['height'] = 7

# iterating keys
for key in mydict:
        print(key)

# iterating values
for key in mydict:
        print(mydict[key])

# check for a key
if 'weight' in mydict:
        print(mydict['weight'])
else:
        print('no weight property!')