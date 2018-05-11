from CitizenWikiRobot.ship_robot import get_ships
from CitizenWikiRobot.roadmap import init_road_map
from CitizenWikiRobot.MysqlHelper import MysqlHelper

if __name__ == '__main__':
    # get_ships()
    # init_road_map()
    mysql_helper = MysqlHelper()
    mysql_helper.insert_constant_translate()
