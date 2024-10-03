import ores.ore_functions as ore_f
import main
import upgrades.upgrades as up

def ore_select(t):
    match t:
        case 'iron':
            if main.mininglevel >= 1:
                ore_f.gather_ore("iron",1*main.ore_gather_mult,4*main.ore_gather_mult,2*main.ore_price_mult,5*main.ore_price_mult)
        case 'gold':
            if main.mininglevel >= 2:
                ore_f.gather_ore("gold",0*main.ore_gather_mult,3*main.ore_gather_mult,5*main.ore_price_mult,8*main.ore_price_mult)
        case 'lead':
            if main.mininglevel >= 2:
                ore_f.gather_ore("lead",0*main.ore_gather_mult,6*main.ore_gather_mult,2*main.ore_price_mult,6*main.ore_price_mult)
        case 'copper':
            if main.mininglevel >= 1:
                ore_f.gather_ore("copper",2*main.ore_gather_mult,9*main.ore_gather_mult,1*main.ore_price_mult,4*main.ore_price_mult)
        case 'tungsten':
            if main.mininglevel >= 3:
                ore_f.gather_ore("tungsten",0*main.ore_gather_mult,4*main.ore_gather_mult,10*main.ore_price_mult,20*main.ore_price_mult)
        case 'cobalt':
            if main.mininglevel >= 4:
                ore_f.gather_ore("cobalt",0*main.ore_gather_mult,6*main.ore_gather_mult,7*main.ore_price_mult,15*main.ore_price_mult)
        case 'ores':
            orenum = 0
            print("Available Ores:\n")
            main.checkavailableores(main.mininglevel)
            for i in main.unlockedores:
                print(main.unlockedores[orenum])
                orenum += 1
            print(" ")
        case 'exit':
            print(f"\n===You earned a total of ${main.total_earnings}.===\n")
        case other:
            print("Invalid input. Please enter 'yes', 'no', or 'exit' to return to the shack.")