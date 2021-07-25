from pywebio.input import *
from pywebio.output import *
def mathamatical_operation():
    a = input("Enter the first value", type = FLOAT)
    b = input("Enter the second value", type = FLOAT)
    c = 0
    operation = radio("Choose one of the operation", options=['+','-','*','/','%'])
    operation_name=""

    if operation=="+":
        operation_name="addition"
        c=a+b
    elif operation=='-':
        operation_name="subtraction"
        c=a-b
    elif operation=='*':
        operation_name=="Multiplication"
        c=a*b
    elif operation=="%":
        operation_name="Modulo"
        c=a%b
    else:
        operation_name="division"
        c=a/b
    put_text('The operation selected is %s and the output is: %2f'%(operation_name,c))

if __name__ == '__main__':
    mathamatical_operation()