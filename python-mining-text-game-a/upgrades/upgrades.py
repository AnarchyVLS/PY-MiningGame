import main

gatheringbuycost = 10
pricebuycost = 10
levelbuycost = 500

def commands(t):
    global gatheringbuycost
    global pricebuycost
    global levelbuycost

    match t:
        case 'gathering':
            buycost = gatheringbuycost
            if main.currentbalance >= buycost:
                main.currentbalance -= buycost
                main.ore_gather_mult += 0.1
                gatheringbuycost = round(buycost * 1.1, 1)
            else:
                print("Insufficient Funds")
        case 'price':
            buycost = pricebuycost
            if main.currentbalance >= buycost:
                main.currentbalance -= buycost
                main.ore_price_mult += 0.1
                pricebuycost = round(buycost * 1.1, 1)
            else:
                print("Insufficient Funds")
        case 'level':
            buycost = levelbuycost
            if main.currentbalance >= buycost:
                main.currentbalance -= buycost
                main.mininglevel +=1
                levelbuycost = buycost * 2
            else:
                print("Insufficient Funds")
        case other:
            print("Invalid Command")

def displayupgrades():
    print(f"Ore Gathering: {round(main.ore_gather_mult,1)}x - Price: $",str(gatheringbuycost))
    print(f"Ore Price: {round(main.ore_price_mult,1)}x - Price: $",str(pricebuycost))
    print(f"Mining Level: {main.mininglevel} - Price: $",str(levelbuycost))