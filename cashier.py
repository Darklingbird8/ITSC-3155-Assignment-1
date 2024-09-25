class Cashier:
    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")

        large = int(input("How many large dollars?: ")) * 1
        half = int(input("How many half dollars?: ")) * 0.5
        quarters = int(input("How many quarters?: ")) * 0.25
        nickels = int(input("How many nickels?: ")) * 0.05
        total = large + half + quarters + nickels
        print(f"Total inserted: ${total:.2f}")
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here change is ${change} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False