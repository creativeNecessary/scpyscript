# -*- coding: UTF-8 -*-
import bs4
import sys
from CitizenWikiRobot.StaticField import StaticField
from CitizenWikiRobot.Vehicle import Vehicle
from CitizenWikiRobot.MysqlHelper import MysqlHelper
from CitizenWikiRobot.Equipment import ShipEquipment, Manufacturer
import requests
import json
from CitizenWikiRobot.Log import Log
import progressbar
import os
import time

reload(sys)
sys.setdefaultencoding('utf-8')
manufacturer_list = []
chassis_id_list = []


def init_vehicle(url):
    mysql_helper = MysqlHelper()
    vehicle = Vehicle(url)
    page = ''
    while page == '':
        try:
            page = requests.get(StaticField.BASE_URL + vehicle.url)
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue

    ship_soup = bs4.BeautifulSoup(page.content, "lxml")

    all_script_tag = ship_soup.find_all('script')
    chassis_id_tag = all_script_tag[1].text

    start_index = chassis_id_tag.find('chassis_id:')
    chassis_id_content = chassis_id_tag[start_index:start_index + 30]
    start_index = chassis_id_content.find(':')
    end_index = chassis_id_content.find('}')
    chassis_id = chassis_id_content[start_index + 1: end_index]
    id_url = 'https://robertsspaceindustries.com/ship-matrix/index?chassis_id=' + chassis_id
    ships_req = ''
    while ships_req == '':
        try:
            ships_req = requests.get(url=id_url)
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue

    content_json = json.loads(ships_req.content)
    data = content_json.get('data')
    for ship_item in data:
        ship_url = ship_item.get('url')
        if url == ship_url:
            vehicle.data_json = ship_item
            vehicle.init_with_data_json()
            break
    # icon store_large
    thumbnails = ship_soup.find("span", attrs={'class': 'thumbnails clearfix'})
    if thumbnails is not None:
        img_urls = []
        for img_tag in thumbnails.contents:
            if type(img_tag) is bs4.Tag and img_tag.attrs['href'] != 'vimeo':
                img_url = img_tag.attrs['href']
                url_array = img_url.split(".")
                if len(url_array) > 1 and (url_array[1] == 'jpg' or url_array[1] == 'png'):
                    img_urls.append(img_url)

        vehicle.img_urls = img_urls
    mysql_helper.insert_vehicle(vehicle)


def get_ships():
    page = 1
    ship_json = get_ship_json(page)
    html = ship_json.get('data').get('html')
    totalrows = ship_json.get('data').get('totalrows')
    rowcount = ship_json.get('data').get('rowcount')
    init_ship(html)
    need_req_time = float(totalrows) / rowcount
    if need_req_time != 0:
        need_req_time += 1
    for page in range(2, 2 + int(need_req_time)):
        print "正在获取第 " + str(page) + "页数据"
        ship_json = get_ship_json(page)
        html = ship_json.get('data').get('html')
        init_ship(html)

    mysql_helper = MysqlHelper()
    #     插入公司
    Log.d('开始将公司插入数据库')
    mysql_helper.insert_manufacturer(manufacturer_list)


def init_ship(html):
    ship_shoup = bs4.BeautifulSoup(html, "lxml")
    ship_elements = ship_shoup.find_all("li", attrs={"class": "ship-item"})
    for ship_element in ship_elements:
        if type(ship_element) is not bs4.Tag:
            continue
        ship_data = ship_element.find("a", attrs={'class': 'filet'})
        ship_url = ship_data.attrs['href']
        init_vehicle(ship_url)


def get_ship_json(page):
    url = "https://robertsspaceindustries.com/api/store/getShips"
    pamas = {"itemType": "ships", "page": str(page), "sort": "store", "storefront": "pledge"}

    ships_req = ''
    while ships_req == '':
        try:
            ships_req = requests.post(url=url, data=pamas)
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue

    ships_json = json.loads(ships_req.content)
    code = ships_json.get('code')
    msg = ships_json.get('msg')
    if msg == "OK" and code == "OK":
        return ships_json
    else:
        return None


def append_manufacturer(manufacturer):
    have_same = False
    for manufacturer_item in manufacturer_list:
        if manufacturer.id == manufacturer_item.id:
            have_same = True
            break
    if not have_same:
        manufacturer_list.append(manufacturer)

# def download_file(file_url):
#     if len(file_url) > 0:
#         file_split = file_url.split('/')
#         file_name = StaticField.IMAGE_PATH + file_split[len(file_split) - 1]
#         Log.d("准备下载 ： " + file_name)
#         url = StaticField.BASE_URL + file_url
#         ctm_file = requests.request("GET", url, stream=True, data=None, headers=None)
#         total_length = int(ctm_file.headers.get("Content-Length"))
#         with open(file_name, "wb") as code:
#             widgets = ['Progress: ', progressbar.Percentage(), ' ',
#                        progressbar.Bar(marker='#', left='[', right=']'),
#                        ' ', progressbar.ETA(), ' ', progressbar.FileTransferSpeed()]
#             pbar = progressbar.ProgressBar(widgets=widgets, maxval=total_length).start()
#             for chunk in ctm_file.iter_content(chunk_size=1):
#                 if chunk:
#                     code.write(chunk)
#                     code.flush()
#                 pbar.update(len(chunk) + 1)
#             pbar.finish()
#
#
# def create_dir():
#     if not os.path.exists(StaticField.IMAGE_PATH):
#         # 创建文件夹
#         Log.d("创建 保存 图片 文件夹")
#         os.makedirs(StaticField.IMAGE_PATH)
#     else:
#         Log.d("文件夹存在 不需要创建！")

# if __name__ == '__main__':
#     get_ships()
