from abc import ABC, abstractmethod

# created a class house
class house(ABC):
    # this function prints your house payment
    def payReminder(self, amount):
        print("Your house payment: ",amount)

    # this function is telling us to pass in an argument
    def payment(self, amount):
        pass

# defined how to implement the payment function from it's parent payReminder class
class debCardPayment(house):
    def payment(self, amount):
        print("Your house payment of {} is due today.".format(amount))


# this is calling our function
obj = debCardPayment()
obj.payReminder("$1800")
obj.payment("$1800")

