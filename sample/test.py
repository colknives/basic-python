''' Sample print function '''
print('This is an example of a print function')


''' Sample variable '''
testVar = "Sample text"
print(testVar)


''' Sample packing '''
x,y = (3,5)
print(x)
print(y)


''' Sample while condition '''
condition = 1

while condition < 10:
    print(condition)
    condition += 1


''' Sample for loop '''
exampleList = [1,2,3,4,5,6,7,8,9]

for x in exampleList:
    print(x)

for y in range(1,11):
    print(y)


''' Sample if condition '''
x = 1
y = 8
z = 5
a = 5

if x < y:
    print('x is less than y')

if x < y > z:
    print('x is less than to y and y is greater than z ')

if a == z:
    print('a is equal to z')


''' Sample if else condition '''
x = 5
y = 8

if x > y:
    print('x is greater than y')
else:
    print('y is greater than x')


''' Sample if elif else condition '''
x = 5
y = 10
z = 22

if x > y:
    print('x is grater than y')
elif x < z:
    print('x is less than z')
else:
    print('none')


''' Sample function '''
def sample():
    print('sample function')

sample()



''' Sample function w/ parameters '''
def addition(num1,num2 = 5):
    answer = num1 + num2
    return answer

print(addition(1,3))

def window(width, height, font = 'TNR', bgc='w'):
    print(width, height, font, bgc)

window(500, 200, 'Calibri')
window(200, 700, bgc='r')



''' Sample local and global variables '''
x = 6

def example():
    globx = x
    globx += 5
    return globx

print(example())



''' Sample write to file '''
text = 'Sample Text to Save \nnew line!'

saveFile = open('exampleFile.txt','w')
saveFile.write(text)
saveFile.close()



''' Sample append to file '''
appendMe = '\nNew information'

appendFile = open('exampleFile.txt','a')
appendFile.write('\n')
appendFile.write(appendMe)
appendFile.close()




''' Sample read to file '''
readMe = open('exampleFile.txt','r').read()
print(readMe)



''' Sample convert each line on file into a list '''
readList = open('exampleFile.txt','r').readlines()
print(readList)



''' Sample class '''
class calculator:
    def addition(num1, num2):
        added = num1 + num2
        return added

    def subtraction(num1, num2):
        subtract = num1 - num2
        return subtract

    def multiplication(num1, num2):
        multiply = num1 * num2
        return multiply

    def division(num1, num2):
        divide = num1 / num2
        return divide

print(calculator.division(15,3))



''' Sample custom modules / importing modules '''
import calculator2 as calc

print(calc.addition(15,3))

from calculator2 import *

print(subtraction(12,4))



''' Sample get user input '''
x = input('What\'s your name: ')
print('Hello ',x)

        
