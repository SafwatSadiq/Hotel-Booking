import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient="records")
df_cards_security = pd.read_csv('card-security.csv', dtype=str)

class Hotel:
    def __init__(self, hotel_ID):
        self.hotel_ID = hotel_ID
        self.name = df.loc[df["id"] == hotel_ID, 'name'].squeeze()
    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_ID, "available"] = 'no'
        df.to_csv('hotels.csv', index=False)
            
    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_ID, "available"].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class SpaHotel(Hotel):
    def book_spa_packages(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_obj):
        self.customer_name = customer_name
        self.hotel = hotel_obj

    def generate(self):
        """Generates a reservation ticket"""
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name.title()}
        Hotel name: {self.hotel.name}
        """
        return content
    

class CreditCard:
    def __init__(self, number):
        self.number = number
    
    def validate(self, expiration, holder, cvc):
        """Validate the credit card information"""
        card_data = {'number': self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, customer_password):
        """Verify if the provided password matches the real password"""
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == customer_password:
            return True
        else:
            return False


class SpaReservationTicket:
    def __init__(self, customer_name, hotel_obj):
        self.customer_name = customer_name
        self.hotel = hotel_obj

    def generate(self):
        """Generates a spa reservation ticket"""
        content = f"""
        Thank you for your SPA reservation!
        Here are your booking data:
        Name: {self.customer_name.title()}
        Hotel name: {self.hotel.name}
        """
        return content


print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = SpaHotel(hotel_id)
if hotel.available():
    credit_card = SecureCreditCard(number='1234')
    if credit_card.validate(expiration='12/26', holder="JOHN SMITH", cvc="123"):
        credit_card_password = input("Enter your credit card password: ")
        if credit_card.authenticate(credit_card_password):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_obj=hotel)
            print(reservation_ticket.generate())
            spa_resver = input("Do you want to book a spa package? (y/n): ")
            if spa_resver == "y":
                hotel.book_spa_packages()
                spa_reservation_ticket = SpaReservationTicket(customer_name=name, hotel_obj=hotel)
                print(spa_reservation_ticket.generate())
        else:
            print("Invalid credit card password!")
    else:
        print("Invalid credit card!")
else:
    print("Sorry, no reservation")