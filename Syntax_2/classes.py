#Parent class
class Person:

  def __init__(self, name, height, weight):
    self.name = name;
    self.height = height;
    self.weight = weight;

  def sayHello(self):
    print("Hello! I'm a person, my name is", self.name)

# Child class inherits from Person
class Student(Person):

        # super is the reference to the parent class Person so 
        # we call Person's constructor here to set the Person
        # properties of the student instance
        def __init__(self, stid, name, height, weight):
                super().__init__(name, height, weight)
                self.stid = stid
        
        # override method of parent
        def sayHello(self):
                print("Hello! I'm a student, my name is", self.name)


bob = Person('bob', 12, 34)
sally = Student(123, 'sally', 7, 34)

bob.sayHello();
sally.sayHello();

print(bob.name);