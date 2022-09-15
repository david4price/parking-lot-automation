import random
import datetime as dt
from printing import *

def generate():
    keycode = ""
    chunk = ""
    alphabet = "ABCDEFGHIJKLMNOPQRZTUVWXYZ1234567890"
    while True:
        while len(keycode) < 8:
            char = random.choice(alphabet)
            keycode += char
            chunk += char
            if len(chunk) == 3:
                keycode += "-"
                chunk = ""
        keycode = keycode[:-1]
        return keycode


def enter_time():
    start = str(dt.datetime.now().strftime('%H:%M:%S'))
    return start


def exit_time():
    stop = str(dt.datetime.now().strftime('%H:%M:%S'))
    return stop


class Car:

    def __init__(self, car_number):
        self.car_number = car_number
        self.keycode = generate()
        self.enter_time = enter_time()
        self.exit_time = None

    # allows us to print the object as a string
    def __str__(self):
        return f"Car number: {self.car_number}, Keycode: {self.keycode}," \
               f" Enter time: {self.enter_time}, Exit time: {self.exit_time}"

    # check if keycode already exists
    def verify(self, car_number):
        if car_number.keycode in self.keycode:
            return False
        else:
            return True


# creates the parking lot
class ParkingLot(Car):
    counter = 1

    # adds cars to the parking lots inventory
    def __init__(self, inventory=None):
        super().__init__(self)
        self.base_price = 20
        self.parking_spots = 2
        self.free_space = 0
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    # check if keycode already exists
    def verify(self, car_number):
        if car_number.keycode in self.inventory:
            car_number.keycode = generate()
        else:
            print()

    def __str__(self):
        return f"{self.inventory}"

    # prints all the cars inside the parking lot
    def print_cars(self):
        for car in self.inventory:
            print(f"{car}")

    # shows the current free parking spaces
    def current_free_space(self):
        self.free_space = self.parking_spots - ParkingLot.counter + 1
        if self.free_space == 0:
            # print(f"Currently FREE parking spots: {free_space}")
            return False
        else:
            # print(f"Currently FREE parking spots: {free_space}")
            return True

    def print_free_space(self):
        print(f"Currently FREE parking spots: {self.free_space}")

    # sets the amount of parking spots in the lot
    def set_parking_space(self, amount):
        self.parking_spots = amount
        print(f"The parking spots have been set to: {self.parking_spots}")

    # set base price for parking
    def set_price(self, base_price):
        self.base_price = base_price
        print(f"The base price was successfully set to: {self.base_price}")

    # adding car to the parking lot
    def add_car(self, car):
        if ParkingLot.counter <= self.parking_spots:
            self.inventory.append(car)
            ParkingLot.counter += 1
            print(f"\nYour keycode is: {car.keycode}"
                  f"\nEntrance time: {car.enter_time}")
            return True
        else:
            return False

    # # searching for car by keycode ### not in use
    # def search_car_keycode(self, keycode):
    #     for i in self.inventory:
    #         if keycode == i.keycode:
    #             print(f"found car: {i}")

    # removes the car by keycode that exited the lot
    def exit_car_by_keycode(self, car):
        for i in self.inventory:
            if car == i.keycode:
                self.inventory.remove(i)
                ParkingLot.counter -= 1
                print(f"Good Bye,"
                      f"\n      Car number: {i.car_number}"
                      f"\n      Keycode: {i.keycode}"
                      f"\n      Entrance time: {i.enter_time}"
                      f"\n      Exit time: {i.exit_time}"
                      f"\n      Debit: {i.pay}\n")
            else:
                print("Please enter correct keycode")

    # searching car by car number for keycode
    def search_car_number(self, car_number):
        for i in self.inventory:
            if car_number == i.car_number:
                print(f"your keycode is: {i.keycode}")
                return True
            else:
                return False

    def check_keycode(self, keycode):
        for i in self.inventory:
            if keycode == i.keycode:
                return True
            else:
                return False

    # updates the exit time of the car and calculates the cost of the parking
    def update_exit_time(self, keycode):
        for i in self.inventory:
            if keycode == i.keycode:
                i.exit_time = exit_time()
                print(f"You are: Car number: {i.enter_time}"
                      f"\n         Keycode: {i.keycode}")
                start = i.enter_time
                end = i.exit_time
                form = '%H:%M:%S'
                total_time = (dt.datetime.strptime(end, form) - dt.datetime.strptime(start, form)).seconds / 3600
                pay1 = self.base_price * 1.25
                pay2 = self.base_price * 1.5
                pay3 = self.base_price * 2
                if 0.5 >= total_time:
                    cal = total_time * self.base_price
                    i.pay = cal
                    # print(f"you bill is {i.pay}")
                if 0.5 < total_time < 0.75:
                    first = total_time - 0.5
                    cal = (pay1 * first) + (self.base_price * 0.5)
                    i.pay = cal
                if 0.75 <= total_time < 1:
                    first = total_time - 0.75
                    cal = (pay2 * first) + (pay1 * 0.25) + (self.base_price * 0.5)
                    i.pay = cal
                if 1.0 <= total_time:
                    first = total_time - 1.0
                    cal = (pay3 * first) + (self.base_price * 0.5) + (pay1 * 0.25) + (pay2 * 0.25)
                    i.pay = cal

    # prints the debit parking_spots
    def print_bill(self, keycode):
        for i in self.inventory:
            if keycode == i.keycode:
                payment = round(i.pay)
                print(f"Remaining debit to pay: {payment}")

    # paying the bill
    def pay_bill(self, keycode):
        for i in self.inventory:
            if keycode == i.keycode:
                paying = input("Pay: ")
                if paying == "yes":
                    i.pay = "PAYED"
                    return True
                if paying == "no":
                    continue
                else:
                    print("you need to pay in order to exit the parking lot")

    # prints entrance time for client
    def print_ent_time(self, keycode):
        for i in self.inventory:
            if keycode == i.keycode:
                print(f"You entered at {i.enter_time}")
