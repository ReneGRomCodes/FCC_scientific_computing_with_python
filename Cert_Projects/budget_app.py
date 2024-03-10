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
        check = self.check_funds(amount)
        if check:
            amount = amount * (-1)
            self.ledger.append({"amount": amount,
                                "description": description,
                                })
            self.balance += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, other_category):
        pass

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True


def create_spend_chart(categories):
    pass


# Instance and method calls for testing
test = Category("TEST")
test.deposit(50, "testdeposit")
test.deposit(25)
test.withdraw(10, "testwithdraw")
test.withdraw(5)
print(test)
