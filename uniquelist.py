num = [2,2,4,1,5,6,6,1]
unique=[]

for n in num:
    if n not in unique:
        unique.append(n)
print(unique)