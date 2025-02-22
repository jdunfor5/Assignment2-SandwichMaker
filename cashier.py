class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        large_dollars = int(input("how many large dollars ($1)?: ")) * 1.00
        half_dollars = int(input("how many half dollars ($0.50)?: ")) * 0.50
        quarters = int(input("how many quarters ($0.25)?: ")) * 0.25
        nickels = int(input("how many nickels ($0.05)?: ")) * 0.05

        total_money = large_dollars + half_dollars + quarters + nickels
        return round(total_money, 2)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        elif coins > cost:
            change = coins - cost
            print(f"Here is ${change} in change")
        return True
