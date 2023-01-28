num1 = input("Please enter first number ")
if num1.isnumeric():
    num1 = int(num1)
else:
    print("Invalid number")
    quit()
num2 = input("Please enter second number ")
if num2.isnumeric():
    num2 = int(num2)
else:
    print("Invalid number")
    quit()

sign = input("Please enter a sign(+, -, *, /)")
result = 0
isResultValid = True  

if sign == '+':
    result = num1 + num2
elif sign == '-':
    result = num1 - num2
elif sign == '*':
    result = num1 * num2
elif sign == '/':
    if (num2 == 0) :
        print("0 can not be a divisor!")
        isResultValid = False
    else :
        result = num1 / num2
else :
    print("Invalid sign!")
    isResultValid = False

if isResultValid == True :
    print(num1, sign, num2, '=', result)
