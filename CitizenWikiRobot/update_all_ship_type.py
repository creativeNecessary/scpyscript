from CitizenWikiRobot.ship_robot import get_ships
from CitizenWikiRobot.roadmap import init_road_map
from CitizenWikiRobot.MysqlHelper import MysqlHelper
from CitizenWikiRobot.comm_link_spectrum_dispatch import get_galactic_guide

if __name__ == '__main__':
    mysqlHelper = MysqlHelper()
    mysqlHelper.insert_all_ship_type()
