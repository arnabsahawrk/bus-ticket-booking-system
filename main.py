from admin import Admin
from system import BusSystem


def passenger_interface():
    pass


def main():
    print("========== WELCOME TO BUS TICKET BOOKING SYSTEM ==========")
    while True:
        print("\nSelect User Type:")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nWelcome To Admin Dashboard:")
            admin = Admin()
            admin.admin_dashboard()

        elif choice == "2":
            passenger_interface()
        elif choice == "3":
            bus_system = BusSystem()
            bus_system.show_buses()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
