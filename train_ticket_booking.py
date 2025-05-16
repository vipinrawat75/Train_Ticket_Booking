from random import randint

current_city = input("Enter from where you wnated to Book Your Ticket: ")
destination = input("Enter your destination to where you wanted to go: ")

class Train:
    def __init__(self, train_no):
        self.train_no = train_no

    def ticket(self, from_city, to_city):
        print(f"Your ticket from {from_city} to {to_city} was booked successfully and your seat no was {randint(222, 888)}")

    def departure(self, from_city, to_city):
        print(f"Train no {self.train_no} will be departure in about 10 min from {from_city} to {to_city}")

    def status(self):
        print(f"Train no {self.train_no} has departured from station in time")

a = Train(12345)
a.ticket(current_city, destination)
a.departure(current_city, destination)
a.status()    