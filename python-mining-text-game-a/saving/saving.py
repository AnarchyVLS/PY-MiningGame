import sqlite3
import main
import upgrades.upgrades as up

db = sqlite3.connect("saving/saveData.db")

def initialiseDB():
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS globalData(id int, mininglevel int, mininglevelcost int, priceupgrade real, priceupgradecost real, gatheringupgrade real, gatheringupgradecost real, totalincome real, balance real, PRIMARY KEY (id))")
    cur.execute("INSERT OR IGNORE INTO globalData(id, mininglevel, mininglevelcost, priceupgrade, priceupgradecost, gatheringupgrade, gatheringupgradecost, totalincome, balance) VALUES (?,?,?,?,?,?,?,?,?)", (1,1,1,1,10,1,10,0,0))
    db.commit()
    updateInitalValues()

def updateDB(level,cost,pricemult,pricecost,gathermult,gathercost,totalincome,bal):
    cur = db.cursor()
    cur.execute("UPDATE globalData SET mininglevel = ?, mininglevelcost = ? priceupgrade = ?, priceupgradecost = ?, gatheringupgrade = ?, gatheringupgradecost = ?, totalincome = ?, balance = ? WHERE id = 1", (level,cost,pricemult,pricecost,gathermult,gathercost,totalincome,bal))
    db.commit()

def updateInitalValues():
    level = db.cursor()
    level.execute("SELECT mininglevel, mininglevelcost, priceupgrade, priceupgradecost, gatheringupgrade, gatheringupgradecost, totalincome, balance FROM globalData WHERE id = 1")
    data = level.fetchall()
    for table in data:
        main.mininglevel = table[0] #Update Mining Level
        up.levelbuycost = table[1] #Update Mining Level Cost
        main.ore_price_mult = table[2] #Update Ore Price Mult
        up.pricebuycost = table[3] #Update Ore Price Upgrade Cost
        main.ore_gather_mult = table[4]#Update Ore Gather Mult
        up.gatheringbuycost = table[5]#Update Ore Gather Upgrade Cost
        main.total_earnings = table[6]#Update Total Earnings
        main.currentbalace = table[7]#Update Current Balance