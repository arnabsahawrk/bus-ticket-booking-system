from helper import Helper
from system import BusSystem


class Passenger:
    def __init__(self, name, phone, Bus):
        self.name = name
        self.phone = phone
        self.bus = Bus
        self.booking_id = Helper.booking_id(Bus.number, Bus.booked_seats)

    def get_details(self):
        print(f"Passenger Name: {self.name}")
        print(f"Phone Number: {self.phone}")
        print(f"Bus Number: {self.bus.number}")
        print(f"Route: {self.bus.route}")
        print(f"Booking ID: {self.booking_id}")


def passenger_interface():
    bus_system = BusSystem()

    print("\nWelcome To Passenger Interface:")
    while True:
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")

        while True:
            bus_number = input("Enter bus number to book ticket: ")
            bus = bus_system.find_bus(bus_number)

            if not bus:
                print("Bus not found. Please try again.")
            elif bus.available_seats() == 0:
                print("No seats available on this bus. Please choose another bus.")
            else:
                break
        while True:
            try:
                seats_to_book = int(input("Enter number of seats to book: "))
                if seats_to_book <= 0:
                    print(
                        "Number of seats must be a positive integer. Please try again."
                    )
                    continue

                if bus.book_seat(seats_to_book):
                    passenger = Passenger(name, phone, bus)
                    bus_system.passengers.append(passenger)
                    print(
                        f"Booking successful! Your booking ID is {passenger.booking_id}."
                    )
                    break
                else:
                    print(
                        f"Only {bus.available_seats()} seats are available. Please try again."
                    )
            except ValueError:
                print("Invalid input. Please enter a valid number for seats to book.")

        print("1. Get Ticket Details")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")
        if choice == "1":
            passenger.get_details()
            break
        elif choice == "2":
            print("Exiting Passenger Interface.")
            break
        else:
            print("Invalid choice. Please try again.")
