from bus import Bus


class BusSystem:  # use case of singleton, design pattern
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(BusSystem, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, "buses"):  # Prevent re-initialization
            self.buses = []
            self.passengers = []

    def add_bus(self, number, route, seats, ticket_price):
        if any(bus.number.lower() == number.lower() for bus in self.buses):
            print("Bus with this number already exists.")
            return

        new_bus = Bus(number.upper(), route.upper(), seats, ticket_price)
        self.buses.append(new_bus)
        print("Bus added successfully.")
        return new_bus

    def find_bus(self, number):
        if not self.buses:
            return None

        bus = next(
            (bus for bus in self.buses if bus.number.lower() == number.lower()), None
        )
        return bus

    def show_buses(self):
        if not self.buses:
            print("No buses available.")
            return

        print("\n========== BUS DETAILS ==========\n")
        for bus in self.buses:
            print(
                f"Bus: {bus.number} | Route: {bus.route} | Total Seats: "
                f"{bus.total_seats} | Available Seats: {bus.available_seats()} | Fare: {bus.ticket_price}"
            )

    def total_revenue(self):
        total = 0
        for passenger in self.passengers:
            total += passenger.tickets * passenger.bus.ticket_price
        print(f"\nTotal Revenue Collected: ৳{total}")
