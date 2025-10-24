from helper import Helper


class Passenger:
    def __init__(self, name, phone, Bus):
        self.name = name
        self.phone = phone
        self.bus = Bus
        self.booking_id = Helper.booking_id(Bus.number, Bus.booked_seats)

    def get_details(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "bus_number": self.bus.number,
            "route": self.bus.route,
            "ticket_number": self.booking_id,
        }
