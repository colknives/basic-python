''' Sample list manipulation '''
x = [1,2,3,4,5,6,7,8]

''' append value in list '''
x.append(2)
print(x)

''' insert value in list '''
x.insert(2,99)
print(x)

''' remove value in list '''
x.remove(3)
print(x)

x.remove(x[2])
print(x)

''' show list from index 3 to 4 '''
print(x[3:5])

''' show last digit in list '''
print(x[-1])

''' show index of a value in list '''
print(x.index(7))

''' count all specific value in list '''
print(x.count(8))

''' sort list '''
x.sort()
print(x)
