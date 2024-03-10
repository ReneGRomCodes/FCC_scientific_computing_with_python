class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def __str__(self):
        budget = self.name + "\n"
        for position in self.ledger:
            budget += position["description"] + " " + str(position["amount"]) + "\n"
        budget += str(self.balance)
        return budget

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
test.deposit(50, "test")
test.deposit(25)
print(test)
