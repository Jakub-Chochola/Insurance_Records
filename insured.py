class Insured:

    def __init__(self, first_name, last_name, phone_number, age):
        """
        Creates new insured person, based on the inputed first name, last name, phone number and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.age = age

    def __str__(self):
        """
        Returns first name, last name, phone number and age of the insured person.
        """
        return "{0} {1} {2} {3}".format(self.first_name, self.last_name, self.phone_number, self.age)


