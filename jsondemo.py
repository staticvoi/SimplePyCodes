# JSON - JAVASCRIPT OBJECT NOTATION
# json is dat aexchange format similar to XML

# json light weight than xml as xml takes data as tag
# thats why json popular 
# json
# {
#     "name":"jack",
#     "age":12,
#     "phone":89729817
# }
# xml
# <name>jack</name>
# <age>12</age>
# <phone>21971</phone>

# not obj like json in python
# its just a format/concept implemented in python
# all languages support it
# generic concept

# now can read json data using any labguage that supports json like javascript,c++
# therefore called as data exchange format(code in python to javascript)
book={}
book['tom']={
    'name':'tom',
    'address':'2 Green strret NY',
    'phone':932787
}

book['bob']={
    'name':'bob',
    'address':'4 wine strret NY',
    'phone':23347
}

import json
s= json.dumps(book)
print(s)
with open(r"C:\Users\10676874\Documents\Basic Python Code of CodeBasics\jsondemo.txt","w") as f:
    f.write(s)
    print("done")
print(type(s)) #str


with open(r"C:\Users\10676874\Documents\Basic Python Code of CodeBasics\jsondemo.txt","r") as f:
    s1=f.read()
    print(s1)
    print(type(s1))
    

import json
book1=json.loads(s)
print(book1)
print(type(book1))

print(book1['bob'])

print(book1['bob']['phone'])

for person in book1:
    print(book1[person])