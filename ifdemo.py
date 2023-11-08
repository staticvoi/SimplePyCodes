# control flow
# n=12
n= input("enter number")
n=int(n)
if n%2==0:
    print("even")
else:
    print("odd")


print(4==4) #trur
print(4!=5) #true
print(4!=4) #false
print(2>1)
print(2<3)
print(2>=3)
print(2<=1)

print(3>2 and 4<1)
print(3>1 or 5>1)
print(not 4==4)


indian=['samosa','naan','butter chicken']
italian=['pasta','pizza']
mexican=['taco','rice']
dish = input("enter dish name")

if dish in indian:
    print("indian cusine")
elif dish in mexican:
    print("mexican cusine")
elif dish in italian:
    print("italian dish")
else:
    print("IDK")