class Category:
    """Represent a category for specific budget."""

    def __init__(self, name):
        """Initialize name, ledger and balance attributes."""
        self.name = name
        self.ledger = []
        self.balance = 0

    def __str__(self):
        """Return a formatted representation of the budget category, including ledger entries and the current
        balance."""
        budget = self.name + "\n"
        for position in self.ledger:
            budget += position["description"] + " " + str(position["amount"]) + "\n"
        budget += str(self.balance)
        return budget

    def deposit(self, amount, description=""):
        """Take numeric value 'amount' and optional string 'description', insert them into 'self.ledger' and add
        'amount' to 'self.budget'."""
        self.ledger.append({"amount": amount,
                            "description": description,
                            })
        self.balance += amount

    def withdraw(self, amount, description=""):
        """Take numeric value 'amount' and optional string 'description', insert them into 'self.ledger' and subtract
        'amount' from 'self.budget' if sufficient funds are available. Return 'True' if withdrawal took place, 'False'
        if not."""
        check = self.check_funds(amount)
        if check:
            self.ledger.append({"amount": amount * (-1),
                                "description": description,
                                })
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        """Return numeric value for 'self.balance'."""
        return self.balance

    def transfer(self, amount, other_category):
        """Transfer numeric value 'amount' to instance 'other_category', update 'self.ledger' and 'self.budget' in each
        instance if sufficient funds are available and return 'True' if transfer took place, 'False' if not."""
        check = self.check_funds(amount)
        if check:
            self.ledger.append({"amount": amount * (-1),
                                "description": "Transfer to " + other_category.name,
                                })
            other_category.ledger.append({"amount": amount,
                                          "description": "Transfer from " + self.name,
                                          })
            self.balance -= amount
            other_category.balance += amount
            return True
        else:
            return False

    def check_funds(self, amount):
        """Check if numeric value 'amount' exceeds 'self.balance'."""
        if amount > self.balance:
            return False
        else:
            return True


def create_spend_chart(categories):
    pass


# Instance and method calls for testing
food = Category("FOOD")
clothing = Category("CLOTHING")

food.deposit(50, "food deposit")
food.deposit(25)
food.withdraw(10, "food withdraw")
food.withdraw(5)
food.transfer(10, clothing)

print(food)
print(clothing)
