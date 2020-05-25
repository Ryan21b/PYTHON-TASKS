import car_functions
from car_data import cars


def main():
    welcome_message = '\n' + "Welcome to our Cars Database!" + '\n'
    welcome_message += "You need choose one of the three options:" + '\n'
    welcome_message += "Option 1: Select a car based on their ID" + '\n'
    welcome_message += "Option 2: Display all of the cars in the database" + '\n'
    welcome_message += "Option 3: Exit the programme" + '\n'
    print(welcome_message)
    running = True
    while running:  # This is our main loop, and we rerun all of the main CLI option everytime
        try:
            user_choice = int(input("Choose option (1,2,3): "))
            output_message = ""
        except ValueError as e:
            output_message = "ERROR: That was not a valid choice! Choose between the follow: 1,2,3"
            user_choice = 0

        # Which action to take based on user decision
        if user_choice == 1:  # View car based on ID
            try:
                user_car_id = int(input("Input the ID of the car you want to see: "))
                user_car = car_functions.get_car_based_on_id(cars, user_car_id)
                if user_car is None:
                    print("This ID didn't match any of the cars in the Database! :(")
            except ValueError as e:
                print("That is not a valid number, car id's are always whole numbers.")
                user_car = None

            if user_car is not None:
                user_car_running = True
                car_menu_message = "\n" + "You are viewing car: %s, %s" % (user_car.car_id, user_car.make)
                car_menu_message += "\n"
                car_menu_message += "What do you want to do?" + "\n"
                car_menu_message += "Option 1: Display the properties of the car" + "\n"
                car_menu_message += "Option 2: Calculate fuel usage" + "\n"
                car_menu_message += "Option 3: Calculate resell value" + "\n"
                car_menu_message += "Option 4: Go back to the main menu" + "\n"
                print(car_menu_message)
                while user_car_running:

                    try:
                        user_car_choice = int(input("Choose option (1,2,3,4): "))
                        car_output_message = ""
                    except ValueError as e:
                        car_output_message = "ERROR: That was not a valid choice! Choose between the follow: 1,2,3,4"
                        user_car_choice = 0
                    if user_car_choice == 1:  # Display the properties of the car
                        car_output_message = user_car.__str__()
                    elif user_car_choice == 2:  # Calculate fuel usage
                        car_output_message = "Fuel usage of this car is: %s km/l" % user_car.calculate_fuel_usage()
                    elif user_car_choice == 3:  # Calculate resell value
                        car_output_message = "Resell value for this car is: R%s" % user_car.calculate_resell_value()
                    elif user_car_choice == 4:  # Exit this menu
                        user_car_running = False
                    elif user_car_choice == 0:  # Error code, nothing to do
                        pass
                    else:  # User didn't choose a valid option
                        car_output_message = "Your choice didn't match the options (1,2,3,4) choose between those."

                    print(car_menu_message)
                    print(car_output_message)
        elif user_choice == 2:  # Display all of the cars in the database
            for car in cars:
                print("")
                print(car)
        elif user_choice == 3:  # Exit
            exit()
        elif user_choice == 0:  # Error code, nothing to do
            pass
        else:
            output_message = "Your choice didn't match the options (1,2,3) choose between those."

        print(welcome_message)
        print(output_message)


main()
