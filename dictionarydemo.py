# dict is key value pair
# also known as maps,associate arrays,hashtables
# similar to list but access elements using key
# no order in dict as access is using keys and imp is to store values associated to keys

d={"tom":1213323,"jack":134353,"prince":3908032}
d
d["tom"]


d["sam"]=978709
d
del d["sam"]
d

for key in d:
    print("Key=",key,"Value=",d[key])

for k,v in d.items():
    print("Key=",k,"Value=",v)

print("tom" in d) #true
print("samir" in d) #false

d.clear() #gives empty dict
