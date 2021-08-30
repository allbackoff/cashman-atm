# Banknotes available. 'D' stands for 'Dollar' and 'C' stands for 'Coin'.
banknotes = [
    ('D_HUNDRED', 100),
    ('D_FIFTY', 50),
    ('D_TWENTY', 20),
    ('D_TEN', 10),
    ('C_FIFTY', 0.5),
    ('C_TWENTY', 0.2),
    ('C_TEN', 0.1),
    ('C_FIVE', 0.05)
]


# Returns the amount of money left after the deposit transaction occurred.
def process_deposit(deposit_amount, old_amount):
    new_amount = {}

    for key, value in deposit_amount.items():
        new_amount[key] = old_amount[key] + int(value)

    return new_amount


# Returns the amount of money left after the withdrawal transaction occurred.
def process_withdrawal(withdrawal_combination, old_amount):
    new_amount = {}

    for key, value in withdrawal_combination.items():
        new_amount[key] = old_amount[key] - value

    return new_amount


# Returns the combination for a particular withdrawal amount.
def get_withdrawal_combination(withdraw_amount, present_amount, banknotes_combination):
    return get_combination_helper(withdraw_amount, present_amount, banknotes_combination, 0)


# Recursive function which returns a boolean indicating whether there is a suitable combination.
# Modifies the banknotes_combination dictionary in-place, without returning it.
def get_combination_helper(withdraw_amount, present_amount, banknotes_combination, current_banknote_index):

    # Name and valuation of the banknote under inspection
    current_banknote_value = banknotes[current_banknote_index][1]
    current_banknote_key = banknotes[current_banknote_index][0]

    # Number of particular banknote needed and present for the transaction.
    amount_rounded = withdraw_amount - \
        (withdraw_amount % current_banknote_value)
    banknotes_needed = int(amount_rounded / current_banknote_value)
    banknotes_present = present_amount[current_banknote_key]

    # Either take how much we need or how much we have of this type of banknote.
    withdraw_banknotes = banknotes_present if (
        banknotes_present < banknotes_needed) else banknotes_needed

    if withdraw_banknotes > 0:

        # Start by getting the maximum number of this banknote and checking the combinations.
        for i in range(withdraw_banknotes, 0, -1):
            banknotes_combination[current_banknote_key] = i
            withdraw_amount = withdraw_amount - i * current_banknote_value

            # We still have the amount to withdraw but it's the last banknote in our list, hence not valid.
            if withdraw_amount > 0 and current_banknote_index == len(banknotes) - 1:
                return False

            # We either got exact withdraw amount or continue by choosing banknotes for the amount left.
            elif withdraw_amount == 0 or get_combination_helper(withdraw_amount, present_amount, banknotes_combination, current_banknote_index + 1):
                return True

            # This number of this particular type of banknote was not suitable for combination.
            # Hence delete it from our combination and continue.
            banknotes_combination.pop(current_banknote_key, None)
            withdraw_amount = withdraw_amount + i * current_banknote_value

        # No combination for this banknote, continue if it's not the last.
        if current_banknote_index != len(banknotes) - 1:
            return get_combination_helper(withdraw_amount, present_amount, banknotes_combination, current_banknote_index + 1)

        # There is no combination we could find.
        return False

    # We don't need this banknote for combination.
    else:

        # We have tried the last banknote from the list and didn't succeed in finding the combination.
        if withdraw_amount > 0 and current_banknote_index == len(banknotes) - 1:
            return False

        # Continue with a next banknote in the list.
        else:
            return get_combination_helper(withdraw_amount, present_amount, banknotes_combination, current_banknote_index + 1)
