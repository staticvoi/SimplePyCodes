# function eg is a dishwasher
# input is dirty dishes
# function body has 3 steps - add water+soap,clean them,dry them
# output is clean dishes

def total_expense(exp): # function argument
    """
    DOCUMENTATION STRINGS- Define something about the function like what it does,what are args etc
    """
    total=0
    for i in exp:       # line 2 to 4 is function body
        total = total+i
    return total # return value

tom_exp=[12,56,32,768,87]

print("total expense = ",total_expense(tom_exp))



def sum(a,b):
    print("a=",a)
    print("b=",b)
    sum=a+b
    print("total isnide function=",sum)
    return sum

# 2 types of arguments - positional and named arguments
# sum1=sum(5,6) #positional arguements - 5 is considered to be a acc to poistion
sum1=sum(b=5,a=6) #named arguments- providing descp which arguement is wha
print("total outside function=",sum1)


def sum(a,b=0): #default agruemnt - if user doesnt pass a value take 0 as default value
    print("a=",a)
    print("b=",b)
    sum=a+b
    print("total isnide function=",sum)
    return sum
sum1=sum(5,6) #here 6 is passed so will take 6 as argument and not 0
