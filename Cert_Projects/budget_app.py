class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.budget = 0.0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount,
                            "description": description,
                            })
        self.budget += amount

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
print(test.budget)
test.deposit(50)
print(test.ledger)
print(test.budget)
