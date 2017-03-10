class Person:
    def __init__(self, name):
        self.name = name

    def say(self, stuff):
        return self.name + ' says: ' + stuff

    def __str__(self):
        return self.name


class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)


class Professor(Lecturer):
    def say(self, stuff):
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)


class ArrogantProfessor(Professor):
    def say(self, stuff):
        return Professor.say(self, stuff)

    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)
