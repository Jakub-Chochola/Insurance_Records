class Insured:

    def __init__(self, name, surname, phone_number, age):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.age = age

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.name, self.surname, self.phone_number, self.age)


