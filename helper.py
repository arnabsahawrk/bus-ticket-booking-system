class BookingId:
    @staticmethod
    def generate(bus_number, booked_seats):
        return f"BD-{bus_number}-{booked_seats + 1:03d}"