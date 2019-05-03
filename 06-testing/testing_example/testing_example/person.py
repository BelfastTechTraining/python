class  PersonException(Exception):
    def __init__(self, person, msg):
        self.person = person
        self.msg = msg
    def __repr__(self):
        return f"PersonException<person={self.person}, msg={self.msg}>"
    def __str__(self):
        return f"PersonException: {self.msg}"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.living = True
    def throw_exception(self):
        raise PersonException(self, "manually throwing exception!")
    def can_vote(self):
        if self.age >= 18:
            return True
        return False
    def die(self):
        self.living = False
        print(f"{self.name} died at the ripe old age of {self.age}")