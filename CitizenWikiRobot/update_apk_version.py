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
    # my.update_apk(2, '1.0.1', "新增功能: 飞船浏览筛选,银河指南系列文章", 'sc_date_view_1.0.1-release.apk')
    # my.update_apk(3, '1.0.2', "1.飞船搜索 \n2.飞船列表优化 \n3.修复bug  \n下载地址 : https://pan.baidu.com/s/18W7x95GsZ1ME8nyi2AlmiA", 'sc_data_view_1.0.2-release.apk',"test","https://pan.baidu.com/s/18W7x95GsZ1ME8nyi2AlmiA")
