class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount in ingredients.items():
            if self.machine_resources[item] < amount:
                print(f"Sorry, there is not enough {item}")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount

        print(f"{sandwich_size} sandwich is now ready. Bon appetit!")

    def print_report(self):
        for item, amount in self.machine_resources.items():
            if item != "cheese":
                print(f"{item.capitalize()}: {amount} slice(s)")
            else:
                print(f"{item.capitalize()}: {amount} pound(s)")