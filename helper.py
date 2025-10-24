class Helper:  # use case of factory method, design pattern
    @staticmethod
    def booking_id(bus_number, booked_seats):
        return f"BD-{bus_number}-{booked_seats + 1:03d}"
