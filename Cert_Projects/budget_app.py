class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        pass

    def withdraw(self, amount, description=""):
        pass

    def get_balance(self):
        pass

    def transfer(self, amount, other_instance):
        pass

    def check_funds(self, amount):
        pass


def create_spend_chart(categories):
    pass
