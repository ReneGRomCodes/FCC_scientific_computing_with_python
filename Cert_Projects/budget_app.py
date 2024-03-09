class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount,
                            "description": description,
                            })
        self.balance += amount

    def withdraw(self, amount, description=""):
        pass

    def get_balance(self):
        pass

    def transfer(self, amount, other_category):
        pass

    def check_funds(self, amount):
        pass


def create_spend_chart(categories):
    pass


# Instance and method calls for testing
test = Category("TEST")
print(test.balance)
test.deposit(50, "test")
test.deposit(25)
print(test.ledger)
print(test.balance)
