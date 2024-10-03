import random
import upgrades.upgrades as up
import ores.ore_selection_function as ore_sf
import saving.saving as sv

total_earnings = 0
unlockedores = ["Iron","Copper"]
currentbalance = 0
ore_gather_mult = 1
ore_price_mult = 1
mininglevel = 1

def main():
    sv.initialiseDB()
    print("===Welcome to the Iron Ore Market Game!===\n")
    print("The goal of this game is to gather as much raw material as possible to sell at a markup on the open market.")
    print("You begin with harvesting iron ore, and with the purchase of enhanced tools, dig deeper and find more valuable materials.\n")
    print("Good luck!")

    modeselect()

def modeselect():
        print("Would you like to access the shack or the mines? (type 'shack' or 'mine', or type 'exit' to quit)")
        mode_selection = input("Command: ").lower()

        if mode_selection == "shack":
            upgrades()
        elif mode_selection == "mine":
            mines()
        elif mode_selection == "exit":
            sv.updateDB()
            ore_sf.ore_select(mode_selection)
        else:
            modeselect()

def mines():
    print("Which ore would you like to start mining? (type 'exit' to cancel or 'ores' to see a list of available ores.)\n")
    ore_selection = input("Command: ").lower()
    ore_sf.ore_select(ore_selection)
    if ore_selection == "exit":
        sv.updateDB()
        modeselect()
    else:
        mines()

def upgrades():
    up.displayupgrades()
    print("What would you like to upgrade? (type 'exit' to cancel or 'upgrades' to see a list of upgrades.)\n")
    up_selection = input("Command: ").lower()
    if up_selection == "exit":
        sv.updateDB()
        modeselect()
    else:
        up.commands(up_selection)
        upgrades()

def checkavailableores(level):
    global unlockedores
    match level:
        case 1:
            unlockedores = ["Iron","Copper"]
        case 2:
            unlockedores = ["Iron","Copper","Gold","Lead"]
        case 3:
            unlockedores = ["Iron","Copper","Gold","Lead","Tungsten"]
        case 4:
            unlockedores = ["Iron","Copper","Gold","Lead","Tungsten","Cobalt"]

if __name__ == "__main__":
    main()
