budget = float(input())
extras = int(input())
clothes_price = float(input())

decor = budget * 0.1
money_for_clothes = extras * clothes_price

starting_money = 0

if extras > 150:
    money_for_clothes = 0.9 * money_for_clothes
    starting_money = budget - (money_for_clothes + decor)



else:
    starting_money = budget - (money_for_clothes + decor)

if (money_for_clothes + decor) > budget:
    print("Not enough money!")
    print(f"Wingard needs {-(starting_money):.2f} leva more.")

else:
    print("Action!")
    print(f"Wingard starts filming with {starting_money:.2f} leva left.")





