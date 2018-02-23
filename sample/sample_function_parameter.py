''' Sample function w/ parameters '''
def addition(num1,num2 = 5):
    answer = num1 + num2
    return answer

print(addition(1,3))

def window(width, height, font = 'TNR', bgc='w'):
    print(width, height, font, bgc)

window(500, 200, 'Calibri')
window(200, 700, bgc='r')
