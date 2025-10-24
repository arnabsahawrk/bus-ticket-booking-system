from datetime import datetime

from helper import Helper
from system import BusSystem
from users import User


class Passenger(User):
    def __init__(self, name, phone, tickets, bus):
        self.name = name
        self.phone = phone
        self.tickets = tickets
        self.bus = bus
        self.booking_id = Helper.booking_id(bus.number, bus.booked_seats)
        self.booking_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_details(self):
        print("\n========== TICKET DETAILS ==========")
        print(f"Passenger Name: {self.name}")
        print(f"Phone Number: {self.phone}")
        print(f"Bus Number: {self.bus.number}")
        print(f"Route: {self.bus.route}")
        print(f"Tickets Booked: {self.tickets}")
        print(f"Ticket Price: ৳{self.bus.ticket_price}")
        print(f"Total Fare: ৳{self.tickets * self.bus.ticket_price}")
        print(f"Booking ID: {self.booking_id}")
        print(f"Booking Time: {self.booking_time}")
        print("====================================\n")

    def display_profile(self):
        print(f"Passenger Name: {self.name} | Phone: {self.phone}")


def passenger_interface():
    bus_system = BusSystem()

    print("\n========== WELCOME TO PASSENGER INTERFACE ==========\n")

    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    while True:
        bus_number = input("Enter bus number to book ticket: ")
        bus = bus_system.find_bus(bus_number)

        if not bus:
            print("Bus not found. Please try again.")
            action = Helper.continue_prompt()

            if action == "view_buses":
                bus_system.show_buses()
                continue
            elif action == "exit":
                print("Exiting Passenger Interface.")
                return
            else:
                continue

        if bus.available_seats() == 0:
            print("No seats available on this bus. Please choose another.")
            action = Helper.continue_prompt()

            if action == "view_buses":
                bus_system.show_buses()
                continue
            elif action == "exit":
                print("Exiting Passenger Interface.")
                return
            else:
                continue

        try:
            seats_to_book = int(input("Enter number of seats to book: ").strip())
            if seats_to_book <= 0:
                print("Seats must be a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if seats_to_book > bus.available_seats():
            print(f"Only {bus.available_seats()} seats available. Please try again.")
            continue

        if bus.book_seat(seats_to_book):
            passenger = Passenger(name, phone, seats_to_book, bus)
            bus_system.passengers.append(passenger)
            print(f"Booking successful! Booking ID: {passenger.booking_id}")
        else:
            print("Booking failed. Try again.")
            continue

        while True:
            print("\n1. View Ticket Details")
            print("2. Exit")
            choice = input("Enter your choice (1-2): ")
            if choice == "1":
                passenger.get_details()
            elif choice == "2":
                print("Exiting Passenger Interface.\n")
                return
            else:
                print("Invalid choice. Please try again.")
