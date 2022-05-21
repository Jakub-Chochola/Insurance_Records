from insured import Insured
from interface import Interface

insured_persons = []
interface = Interface()
go_on = True

while go_on:
    print("______________________________\nInsurance Records\n______________________________\n")
    options = input("Choose your action:\n"
                    "1 - Add new insured.\n"
                    "2 - Print list of all insured.\n"
                    "3 - Search for the insured.\n"
                    "4 - Quit the application.\n\n")
    print()
    if options == "1":
        name = input("Enter the insured's name:\n")
        surname = input("Enter the insured's surname:\n")
        phone_number = input("Enter the insured's phone number:\n")
        age = input("Enter the insured's age:\n")
        new_person = Insured(name, surname, phone_number, age)
        insured_persons.append(new_person.__str__())
        print()
        input("The data has been saved. Press any key to continue.\n")
    elif options == "2":
        interface.list_of_insured(insured_persons)
        print()
        input("Press any key to continue.\n")
    elif options == "3":
        interface.find_user(insured_persons)
        input("Press any key to continue.\n")
    elif options == "4":
        go_on = False
        print()
        print("Thank you for using our application. Have a nice day!\n")
    else:
        input("Invalid input. Press any key to continue.\n")
