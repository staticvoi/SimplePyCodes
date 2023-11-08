class Person:
    def __init__(self,name) -> None:
        self.name=name
    def talk(self):
        print(f"name is {self.name}")

john = Person("jane")
john.talk