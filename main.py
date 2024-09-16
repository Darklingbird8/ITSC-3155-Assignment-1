### Data ###
from operator import truediv

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources.get(item, 0):
                print(f"Sorry, not enough {item}.")
                return False
            return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        total = quarters + dimes + nickels + pennies
        print(f"Total inserted: ${total:.2f}")
        return total


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Transaction succesful. Your change is ${change}")
            return True
        else:
            print("Transaction canceled. Not enough money.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"Made a {sandwich_size} sandwich.")

### Make an instance of SandwichMachine class and write the rest of the codes ###

sandwich_machine = SandwichMachine(resources)

sandwich_size = input("What size sandwich would you like? (small/medium/large): ").lower()
if sandwich_size in recipes:
    sandwich_recipe = recipes[sandwich_size]["ingredients"]
    sandwich_cost = recipes[sandwich_size]["cost"]

    if sandwich_machine.check_resources(sandwich_recipe):
        coins_inserted = sandwich_machine.process_coins()
        if sandwich_machine.transaction_result(coins_inserted, sandwich_cost):
            sandwich_machine.make_sandwich(sandwich_size, sandwich_recipe)
else:
    print("Invalid size selected")