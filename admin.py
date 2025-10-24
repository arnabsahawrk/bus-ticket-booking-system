from system import BusSystem


class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"

    def login(self, username, password):
        return self.username == username and self.password == password

    def admin_dashboard(self):
        while True:
            username = input("Enter username: ")
            password = input("Enter password: ")

            if self.login(username, password):
                print("Login Successful!")
                break
            else:
                print("Invalid credentials. Please try again.")

        print("\nWelcome To Admin Dashboard:")
        bus_system = BusSystem()
        while True:
            print("\nSelect Admin Option:")
            print("1. Add Bus")
            print("2. View Buses")
            print("3. Logout")
            choice = input("Enter your choice (1-3): ")
            if choice == "1":
                number = input("Enter bus number: ")
                route = input("Enter bus route: ")

                while True:
                    try:
                        seats = int(input("Enter total seats: "))
                        if seats <= 0:
                            print(
                                "Total seats must be a positive integer. Please try again."
                            )
                            continue
                        elif seats < 10 or seats > 40:
                            print(
                                "Total seats must be between 10 and 40. Please try again."
                            )
                            continue
                        break
                    except ValueError:
                        print(
                            "Invalid input. Please enter a valid number for total seats."
                        )

                    while True:
                        try:
                            ticket_price = float(input("Enter ticket price: "))
                            if ticket_price <= 0:
                                print(
                                    "Ticket price must be a positive number. Please try again."
                                )
                                continue
                            elif ticket_price < 500:
                                print(
                                    "Ticket price must be at least 500. Please try again."
                                )
                                continue
                            break
                        except ValueError:
                            print(
                                "Invalid input. Please enter a valid number for ticket price."
                            )

                bus_system.add_bus(
                    number=number, route=route, seats=seats, ticket_price=ticket_price
                )
            elif choice == "2":
                bus_system.show_buses()
            elif choice == "3":
                print("Logging out from Admin Dashboard.")
                break
            else:
                print("Invalid choice. Please try again.")
