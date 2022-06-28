class Human:
    def log(self):
        print("Mother fucker")

class Person(Human):
    def __init__(this, name, age):
        this.name = name
        this.age = age

    @staticmethod
    def read_person():
        print("Mother fucker ")

    def __str__(self):
        return self.name + " " + str(self.age)

    def display_all(group):
        for person in group:
            print(person)

    def updateName(self, newName):
        self.name = newName

    @property  ## getter but cannot invoke
    def name(self):
        # print("getting the name")
        return self._name
    @name.setter#set the name
    def name(self,name):
        # print("setting the name")
        self._name = name

# c = Person("Nhan Vu", 21)
person = [Person("Nhan Vu", 21),
          Person("Linh Bui", 20)]
print(person[0])
person[0].log()
# Person.display_all()

# update attribute
# c.updateName("Minh")
# c.name = "Minh"
# c.age = '100'

# Person.read_person()
