
"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    savings_account = Account(balance, 0)

    # Calculate interest earned
     # ADD YOUR CODE HERE
    interest_earned = balance * (interest_rate / 100 * months / 12)


    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_balance(balance)
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_interest(interest_rate)
    # Return the updated balance and interest earned.
    return updated_balance, interest_earned

    updated_balance, interest_earned = create_savings_account(savings_balance, savings_interest, months)

    print("Here are the details of the savings account. ")
    print("The balance is: $", format(savings_balance.get_balance(), ',.2f'))
    print("APR Interest Rate is:", format(savings_interest.get_interest(), ',.2f'),'%')