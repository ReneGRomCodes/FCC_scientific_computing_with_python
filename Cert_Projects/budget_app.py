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
        # Set 'self.name' centered in between "*"s for a 30-character long title line.
        title_line_stars = (30 - len(self.name)) // 2 * "*"
        title_line = title_line_stars + self.name + title_line_stars
        if len(title_line) < 30:
            title_line = "*" + title_line
        budget = title_line + "\n"
        # Construct the ledger section in block style format.
        for position in self.ledger:
            # Restrict length of description to 23 characters in printout.
            if len(position["description"]) > 23:
                position["description"] = position["description"][:23]
            formatted_amount = "{:.2f}".format(position["amount"])
            length_space = (30 - (len(position["description"]) + len(formatted_amount))) * " "
            budget += position["description"] + length_space + formatted_amount + "\n"
        # Total budget.
        budget += f"Total: {self.balance:.2f}"
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
        """Check if numeric value 'amount' exceeds 'self.balance'. Return 'False' if it does and 'True' if not."""
        if amount > self.balance:
            return False
        else:
            return True


def create_spend_chart(categories):
    pass


# Instance and method calls for testing.
food = Category("FOOD")
clothing = Category("CLOTHING")
entertainment = Category("ENTERTAINMENT")

food.deposit(50, "food deposit")
food.deposit(25)
food.withdraw(10, "food withdraw")
food.withdraw(15.89, "restaurant and more food for dessert")
food.withdraw(5)
food.transfer(10, clothing)

print(food)
print(clothing)
print(entertainment)
