from tickets import *
from printing import *
from utils import *

empty_list = []
save(empty_list, "parking.data")

"""
secret admin menu, in choice enter "666"
"""

my_parking = ParkingLot()  # creates the parking lot
check_space = True
search = True
admin_action = True

while True:
    while check_space:
        startmessage()  # prints message
        check_space = ParkingLot.current_free_space(my_parking)
        ParkingLot.print_free_space(my_parking)
        choice()  # prints choice message

        action = input("\nYour choice: ")

        if action == "1":  # adds the car that entered the parking lot
            temp_car_number = input("Enter your vehicle number here: ")
            car_number = temp_car_number.replace(" ", "")
            temp_car = Car(car_number)  # makes it a class with values
            my_parking.add_car(temp_car)  # adds car to parking lot
            my_parking.verify(temp_car)  # checks the keycode so there will be no duplicates
            save(my_parking, "parking.data")
            break

        if action == "2":  # removes the exiting car form the parking
            car_action = input("Enter your keycode here: ")
            if car_action == "":
                break
            else:
                my_parking.update_exit_time(car_action)  # updates the exit time and sums up the bill
                my_parking.print_bill(car_action)  # prints the bill
                paying = my_parking.pay_bill(car_action)  # paying the bill
                search = my_parking.check_keycode(car_action)
                if not search:
                    print("Please try again and enter a VALID keycode")
                else:
                    if paying:
                        my_parking.exit_car_by_keycode(car_action)  # removes car from parking lot
                        check_space = ParkingLot.current_free_space(my_parking)  # updates the current free spaces in the lot
                        save(my_parking, "parking.data")
                    else:
                        break
                break

        if action == "3": # checks your entrance time
            car_action = input("Enter your keycode here: ")
            if car_action == "":
                break
            else:
                my_parking.print_ent_time(car_action)
                break

        if action == "4":  # if you forgot your keycode you can get it again
            car_action = input("Enter your vehicle number here: ")
            if car_action == "":
                break
            else:
                search = my_parking.search_car_number(car_action)
                if not search:
                    print("Please try again and enter a valid vehicle number")
                else:
                    break

        if action == "666":  # admin menu
            while admin_action:
                admin_choice()
                admin_action = input("\nYour choice: ")
                if admin_action == "1":  # sets parking spots in the lot
                    try:
                        amount = int(input("How many parking spots to you want?\nEnter here: "))
                        my_parking.set_parking_space(amount)
                        ParkingLot.current_free_space(my_parking)
                    except:
                        print("Please enter a VALID number")

                if admin_action == "2":  # set the base price for parking
                    try:
                        base_price = int(input("Whats the base price you want: "))
                        my_parking.set_price(base_price)
                    except:
                        print("Please enter a VALID number")

                if admin_action == "3":  # reset file
                    try:
                        admin_action2 = input("Are you sure?\n")
                        if admin_action2 == "yes":
                            empty_list = []
                            save(empty_list, "parking.data")
                            print("Reset Successfully")
                        else:
                            print("Please answer yes or no next time")
                    except:
                        pass

                if admin_action == "4":  # prints all the cars parked inside the parking lot
                    my_parking.print_cars()
                if admin_action == "5":  # returns to main menu
                    admin_action = False
                if admin_action == "":
                    admin_action = False
        else:
            print("Please choose ONE of the options")
            continue

    # menu for when the parking lot is full and no more cars can enter
    while not check_space:
        admin_action = True
        search = True
        startmessage()
        choice2()
        action = input("\nYour choice: ")
        if action == "1":  # removes the exiting car form the parking
            car_action = input("Enter your keycode here: ")
            if car_action == "":
                break
            else:
                my_parking.update_exit_time(car_action)  # updates the exit time and sums up the bill
                my_parking.print_bill(car_action)  # prints the bill
                paying = my_parking.pay_bill(car_action)  # paying the bill
                search = my_parking.check_keycode(car_action)
                if not search:
                    print("Please try again and enter a VALID keycode")
                else:
                    if paying:
                        my_parking.exit_car_by_keycode(car_action)  # removes car from parking lot
                        check_space = ParkingLot.current_free_space(
                            my_parking)  # updates the current free spaces in the lot
                        save(my_parking, "parking.data")
                    else:
                        break
                break

        if action == "2":  # checks your entrance time
            car_action = input("Enter your keycode here: ")
            if car_action == "":
                break
            else:
                my_parking.print_ent_time(car_action)
                break

        if action == "3":  # if you forgot your keycode you can get it again
            car_action = input("Enter your vehicle number here: ")
            if car_action == "":
                break
            else:
                search = my_parking.search_car_number(car_action)
                if not search:
                    print("Please try again and enter a valid vehicle number")
                else:
                    break

        if action == "666":  # admin menu
            while admin_action:
                admin_choice()
                admin_action = input("\nYour choice: ")
                if admin_action == "1":  # sets parking spots in the lot
                    try:
                        amount = int(input("How many parking spots to you want?\nEnter here: "))
                        my_parking.set_parking_space(amount)
                        ParkingLot.current_free_space(my_parking)
                    except:
                        print("Please enter a VALID number")

                if admin_action == "2":  # set the base price for parking
                    try:
                        base_price = int(input("Whats the base price you want: "))
                        my_parking.set_price(base_price)
                    except:
                        print("Please enter a VALID number")

                if admin_action == "3":  # reset file
                    try:
                        admin_action2 = input("Are you sure?\n")
                        if admin_action2 == "yes":
                            empty_list = []
                            save(empty_list, "parking.data")
                            print("Reset Successfully")
                        else:
                            print("Please answer yes or no next time")
                    except:
                        pass

                if admin_action == "4":  # prints all the cars parked inside the parking lot
                    my_parking.print_cars()
                if admin_action == "5":  # returns to main menu
                    admin_action = False
                if admin_action == "":
                    admin_action = False
        else:
            print("Please choose ONE of the options")
            continue
