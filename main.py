import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

sandwich_maker = SandwichMaker(data.resources)
cashier = Cashier()
while True:
    sandwich_size = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    if sandwich_size == "off":
        break

    elif sandwich_size == "report":
        print(f"Remaining resources: {data.resources}")

    elif sandwich_size in data.recipes:
        sandwich_recipe = data.recipes[sandwich_size]["ingredients"]
        sandwich_cost = data.recipes[sandwich_size]["cost"]

        if sandwich_maker.check_resources(sandwich_recipe):
            coins_inserted = cashier.process_coins()
            if cashier.transaction_result(coins_inserted, sandwich_cost):
                sandwich_maker.make_sandwich(sandwich_size, sandwich_recipe)
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")
    else:
        print("Invalid size selected")