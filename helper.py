class Helper:  # use case of factory method, design pattern
    @staticmethod
    def booking_id(bus_number, booked_seats):
        return f"BD-{bus_number}-{booked_seats:02d}"

    @staticmethod
    def continue_prompt():
        print("\n1. Continue Booking")
        print("2. View Buses")
        print("Press any other key to Exit.")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            return "continue"
        elif choice == "2":
            return "view_buses"
        else:
            return "exit"
