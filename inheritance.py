class mammal:
    def walk(self):
        print("walk")

class dog(mammal):
    pass

class cat(mammal):
    def meow(self):
        print("meow")

dog1=dog()
dog.walk

cat1=cat()
cat.walk
cat.meow