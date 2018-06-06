# -*- coding: UTF-8 -*-
from CitizenWikiRobot.ship_robot import get_ships
from CitizenWikiRobot.roadmap import init_road_map
from CitizenWikiRobot.MysqlHelper import MysqlHelper
from CitizenWikiRobot.comm_link_spectrum_dispatch import get_galactic_guide

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    my = MysqlHelper()
    my.update_apk(2, '1.0.1', "新增功能: 飞船浏览筛选,银河指南系列文章", 'sc_date_view_1.0.1-release.apk')
