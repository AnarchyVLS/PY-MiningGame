import random
import main

def gather_ore(a,b,c,d,e):
    ore = a
    ore_amt = round(random.uniform(b, c),1)
    market_price = round(random.uniform(d, e),1)
    earnings = round(ore_amt * market_price,1)
    main.total_earnings += earnings
    main.currentbalance += earnings
    summary(ore_amt, ore, earnings, market_price)
    
def summary(a,b,c,d):
    print(f"You gathered {a} {b} ore and sold them for ${c}.")
    print(f"The market price per {b} ore was ${d}.\n")
    print(f"You now have a total balance of ${round(main.currentbalance,1)}")