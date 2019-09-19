class Person(object):
    def __init__(self, person_name):
        self.name = person_name

    def say_hello(self):
        print( "Hi everyone my name is {}!".format(self.name))

Deer = Person("Deer Brinkley")
Deer.say_hello()
