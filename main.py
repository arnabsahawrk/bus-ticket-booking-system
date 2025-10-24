from admin import Admin
from passenger import passenger_interface
from system import BusSystem


def main():
    print("========== WELCOME TO BUS TICKET BOOKING SYSTEM ==========")
    while True:
        print("\nSelect User Type:")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            admin = Admin()
            admin.admin_dashboard()

        elif choice == "2":

            bus_system = BusSystem()
            if not len(bus_system.buses):
                print("No buses available. Please contact admin.")
            else:
                passenger_interface()

        elif choice == "3":
            bus_system = BusSystem()
            bus_system.show_buses()

        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
