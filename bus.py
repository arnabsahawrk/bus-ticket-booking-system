class Bus:
    def __init__(self, number, route, total_seats, ticket_price):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.__booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.__booked_seats

    def book_seat(self, number_of_seats):
        if number_of_seats <= self.available_seats():
            self.__booked_seats += number_of_seats
            return True
        else:
            return False

    @property
    def booked_seats(self):
        return self.__booked_seats
