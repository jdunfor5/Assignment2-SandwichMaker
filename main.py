import data
from sandwich_maker import SandwichMaker
from cashier import Cashier



# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier




def main():
    ###  write the rest of the codes ###
    while True:
        user_input = input("What would you like? (small/ medium/ large/ off/ report): ").strip().lower()

        if user_input in recipes:
            sandwich = recipes[user_input]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                coins_inserted = cashier_instance.process_coins(cashier_instance)
                if cashier_instance.transaction_result(cashier_instance, coins_inserted, cost):
                    sandwich_maker_instance.make_sandwich(user_input, ingredients)

        elif user_input == "report":
            sandwich_maker_instance.print_report()

        elif user_input == "off":
            print("Turning off the sandwich maker. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")
if __name__=="__main__":
    main()
