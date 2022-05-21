class Interface:

    @staticmethod
    def list_of_insured(insured_persons):
        for person in insured_persons:
            print(person)

    @staticmethod
    def find_user(insured_persons):
        insureds_name = input("Enter the insured's name:\n")
        insureds_surname = input("Enter the insured's surname:\n")
        print()
        for person in insured_persons:
            if insureds_name in person and insureds_surname in person:
                print(person.__str__(), "\n")