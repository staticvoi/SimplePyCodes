tot = 0 #global var accessed anywhere in code
def sum(a,b):
    print("a=",a)
    print("b=",b)
    tot=a+b #local var within block right now function
    print("total isnide function=",tot)
    return tot


sum1=sum(b=5,a=6) 
print("total outside function=",sum1)
print("total = ",tot)