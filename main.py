import pandas as pd

df = pd.read_csv('hotels.csv')


class Hotel:
    def __init__(self,ID):
        pass
    def book(self):
        pass
    
    def view(self):
        pass
    
    def available(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_name):
        pass
    def generate(self):
        pass


id = input("Enter the id of the hotel: ")
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    reservation_ticket.generate()
else:
    print("Sorry, no reservation")