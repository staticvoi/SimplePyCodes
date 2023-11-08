# exception are errors that occur within program
# exception unexpected to happen
# error program terminates abruptly and crash stop execuution
# handle exception

# 1/0 - ZeroDivisionError
# 'abc'+2 - TypeError

x=int(input("num 1= "))
y=int(input("num 2= "))
try:
    z=x/y
except Exception as e: #generic way of handling exception
    print('Exception is ',e)
    z=None
print('Division is ',z)


x=int(input("num 1= "))
y=int(input("num 2= "))
try:
    z=x/y
except ZeroDivisionError: #speecific way of handling exception
    print('division by 0 not possible')
    z=None
print('Division is ',z)

# type python builtin exceptions in google

x=int(input("num 1= "))
y=input("num 2= ")
try:
    z=x/y
except ZeroDivisionError:
    print('division by 0 not possible')
    z=None
except Exception as e:
    print('exception is: ',type(e).__name__) #gives name of exception that has occurred
    z = None
print('Division is ',z)
