
def add(num1,num2):
    return(num1+num2)
def sub(num1,num2):
    return(num1-num2)
def mul(num1,num2):
    return(num1*num2)
def calculator(num1,num2,op):
    if op== '+':
        print(add(num1,num2))
    elif op== '-':
        print(sub(num1,num2))
    elif op == '*':
        print(mul(num1,num2))
    else:
        print('Out of range!')
calculator(100,40,'+')
