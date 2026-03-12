# Custom Exceptions
class SeatNotAvailableError(Exception):
    pass

class InvalidPassengerError(Exception):
    pass

class PaymentFailedError(Exception):
    pass


class FlightSystem:
    def __init__(self):
        self.flights = {
            "AI101": {"destination": "Delhi", "seats": 3, "price": 5000},
            "AI202": {"destination": "Mumbai", "seats": 2, "price": 7000},
            "AI303": {"destination": "Bangalore", "seats": 1, "price": 6000}
        }
        self.bookings = []

    # Search Flights
    def search_flights(self):
        print("\nAvailable Flights:")
        for f, details in self.flights.items():
            print(f, "->", details)

    # Book Ticket
    def book_ticket(self, flight_no, name, age, payment):
        try:
            if not name or age <= 0:
                raise InvalidPassengerError("Invalid passenger details!")

            if flight_no not in self.flights:
                raise Exception("Flight not found!")

            if self.flights[flight_no]["seats"] == 0:
                raise SeatNotAvailableError("No seats available!")

            if payment not in ["UPI", "Card"]:
                raise PaymentFailedError("Payment method failed!")

            self.flights[flight_no]["seats"] -= 1
            self.bookings.append((name, flight_no))

            print("Ticket booked successfully!")

        except (SeatNotAvailableError, InvalidPassengerError, PaymentFailedError) as e:
            print("Error:", e)

    # Cancel Ticket
    def cancel_ticket(self, name):
        try:
            for booking in self.bookings:
                if booking[0] == name:
                    self.bookings.remove(booking)
                    self.flights[booking[1]]["seats"] += 1
                    print("Ticket cancelled successfully!")
                    return

            raise Exception("Booking not found!")

        except Exception as e:
            print("Error:", e)


# Main Program
system = FlightSystem()

while True:
    print("\n1. Search Flights")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.search_flights()

    elif choice == "2":
        flight = input("Enter flight number: ")
        name = input("Enter passenger name: ")
        age = int(input("Enter age: "))
        payment = input("Payment method (UPI/Card): ")

        system.book_ticket(flight, name, age, payment)

    elif choice == "3":
        name = input("Enter passenger name: ")
        system.cancel_ticket(name)

    elif choice == "4":
        print("Exiting system...")
        break

    else:
        print("Invalid choice!")