from CitizenWikiRobot.MysqlHelper import MysqlHelper
import os
from CitizenWikiRobot.Log import Log
import json

if __name__ == '__main__':
    my = MysqlHelper()
    jsonFile = open(os.curdir + "/priceJson", 'r')
    jsonStr = json.loads(jsonFile.read())
    for ship_price in jsonStr:
        name = ship_price.get('name')
        price = ship_price.get('msrp')
        my.update_ship_price(name, price)
