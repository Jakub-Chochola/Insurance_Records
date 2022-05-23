class Interface:

    @staticmethod
    def list_of_insured(insured_persons):
        for person in insured_persons:
            print(person)

    @staticmethod
    def find_user(insured_persons):
        insureds_first_name = input("Enter the insured's first name:\n")
        insureds_last_name = input("Enter the insured's last name:\n")
        print()
        for person in insured_persons:
            if insureds_first_name in person and insureds_last_name in person:
                print(person.__str__(), "\n")