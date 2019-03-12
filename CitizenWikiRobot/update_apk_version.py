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
    # my.update_apk(4, '1.0.3', "1.修复bug  \n下载地址 : https://pan.baidu.com/s/1jve5pn1sup-q6GiautlagA", 'sc_data_view_1.0.3-release.apk',"test","https://pan.baidu.com/s/1jve5pn1sup-q6GiautlagA")
    my.update_apk(5, '1.0.4', "1.添加飞船价格 \n 由于签名由jar签名升级为全包签名,所以此次更新不支持直接安装,需要将app卸载重装! 点击下载会将新版apk下载到 路径 /storage/emulated/0/Android/data/sc.com.scdataview/cache/NetCache/UpdateApk文件夹 中  \n网盘下载地址 : https://pan.baidu.com/s/1-KLcdAxmZNOqhlEri6rZiA", 'sc_data_view_1.0.4-release.apk',"test","https://pan.baidu.com/s/1-KLcdAxmZNOqhlEri6rZiA")
