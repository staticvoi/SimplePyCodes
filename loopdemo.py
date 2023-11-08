exp = [12908,120,3249,9483,873,94]
# total = exp[0]+exp[1]+exp[2]+...
total=0
for i in exp:
    total = total+i
print("total="+total)


total=0
for i in range(len(exp)):
    total = total+exp[i]
    print('month=',(i+1),'expense=',exp[i])
print("total="+total)

for j in range(1,11):
    # print(j)
    print(j*j)



key_loc ='chair'
locations=['car','garage','comp','room','chair']

for i in locations:
    if i==key_loc:
        print("found key in ",i)
        break #break when the goal is found
    else:
        print("key not found in ",i)


for i in range(1,6):
    if i%2==0:
        continue
    print(i*i)


i = 1
while i<=5:
    print(i)
    i=i+1