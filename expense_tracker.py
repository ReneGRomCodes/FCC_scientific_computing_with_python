# Learning lambda functions by building an expense tracker:
# You'll explore the power of Lambda Functions by creating an expense tracker. Your resulting app will demonstrate how
# you can use Lambda Functions for efficient, streamlined operations.


def add_expense(expenses, amount, category):
    """Adds an expense to the list of expenses. 'expenses' is list of expenses, 'amount' is amount of expense(float),
    'category' is category of the expense (str)"""
    expenses.append({'amount': amount, 'category': category})


def print_expenses(expenses):
    """Prints all expenses (list 'expenses') in a formatted way."""
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')


def total_expenses(expenses):
    """Calculates the total expenses from list 'expenses' and returns the sum of expenses as (float)."""
    return sum(map(lambda expense: expense['amount'], expenses))


def filter_expenses_by_category(expenses, category):
    """Filters expenses by a specified category and returns a filter object containing expenses with specified
    category"""
    return filter(lambda expense: expense['category'] == category, expenses)


def main():
    """Main function to run the expense tracker program."""
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            print('Exiting the program.')
            break


if __name__ == '__main__':
    main()
