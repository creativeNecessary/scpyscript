# -*- coding: UTF-8 -*-
import bs4
import sys
from CitizenWikiRobot.StaticField import StaticField
from CitizenWikiRobot.Vehicle import Vehicle
from CitizenWikiRobot.MysqlHelper import MysqlHelper
from CitizenWikiRobot.Equipment import ShipEquipment, Equipment, Manufacturer
import requests
import json
from CitizenWikiRobot.Log import Log
import progressbar
import os

reload(sys)
sys.setdefaultencoding('utf-8')
ship_list = []


def init_vehicle(url):
    vehicle = Vehicle(url)
    page = requests.get(StaticField.BASE_URL + vehicle.url)
    ship_soup = bs4.BeautifulSoup(page.content, "lxml")
    field_tags = ship_soup.find_all('div', attrs={'class': 'l-sheet__block'})
    for field_tag in field_tags:
        fields = field_tag.children
        index = 0
        field_key = None
        for field in fields:
            if type(field) is bs4.Tag:
                if field.name == "h4" and index % 2 == 0:
                    field_key = field.text.strip()
                    vehicle.fields[field_key] = ""
                elif field.name == "p" and index % 2 == 1:
                    if field_key is not None and field_key in vehicle.fields:
                        vehicle.fields[field_key] = field.text.strip()
                        # print field_key + ":" + vehicle.fields[field_key]
                index += 1

    script_tags = ship_soup.find_all('script', attrs={'type': 'text/javascript'})
    ship_json = ""
    for script_tag in script_tags:
        script = script_tag.text

        if script.find("new RSI.ShipSystemsView") != -1:
            one_step = script.split('data:')
            if len(one_step) >= 2:
                second_step = one_step[1].split('.resultset[0]')
                if len(second_step) >= 2:
                    ship_json = second_step[0]
                    vehicle.model3d_url = get_model3d(second_step[1])
                    break
    ship_data = json.loads(ship_json)
    result_set = ship_data['resultset']
    if result_set is not None and len(result_set) > 0:
        result_data = result_set[0]
        manufacturer_data = result_data['manufacturer']
        manufacturer = Manufacturer()
        manufacturer.code = manufacturer_data['code']
        manufacturer.name = manufacturer_data['name']
        manufacturer.known_for = manufacturer_data['known_for']
        manufacturer.description = manufacturer_data['description']
        manufacturer_media = manufacturer_data['media']
        if manufacturer_media is not None and len(manufacturer_media) > 0:
            media = manufacturer_media[0]
            images = media['images']
            if images is not None:
                manufacturer.icon = images['avatar']
        vehicle.manufacturer = manufacturer

        vehicle.name = result_data['name']
        vehicle.size = result_data['size']
        avionics = result_data['avionics']
        modular = result_data['modular']  # system
        propulsion = result_data['propulsion']
        thrusters = result_data['thrusters']
        weapons = result_data['weapons']
        vehicle.avionics = fill_equipment(avionics, 'avionics', 'avionic')
        vehicle.modular = fill_equipment(modular, 'modular', 'modular')
        vehicle.propulsion = fill_equipment(propulsion, 'propulsion', 'propulsion')
        vehicle.thrusters = fill_equipment(thrusters, 'thrusters', 'thruster')
        vehicle.weapons = fill_equipment(weapons, 'weapons', 'weapon')
    # 初始化图片合集
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
    return vehicle


def fill_equipment(equipment_list, belong_to, equip_tag):
    ship_equipment_list = []
    index = 0
    for ship_eq_data in equipment_list:
        ship_equipment = ShipEquipment()
        ship_equipment.belong_to = belong_to
        if ship_eq_data['size'] is not None:
            ship_equipment.size = ship_eq_data['size'].strip()

        if ship_eq_data['type'] is not None:
            ship_equipment.type = ship_eq_data['type'].strip()

        if ship_eq_data['details'] is not None:
            ship_equipment.details = ship_eq_data['details'].strip()

        if ship_eq_data['quantity'] is not None:
            ship_equipment.quantity = ship_eq_data['quantity'].strip()

        # ship_equipment.size = ship_eq_data['size'].strip()
        # ship_equipment.type = ship_eq_data['type'].strip()
        # ship_equipment.details = ship_eq_data['details'].strip()
        # ship_equipment.quantity = ship_eq_data['quantity'].strip()
        ship_equipment.tag = equip_tag
        equipment = Equipment()
        equipment_data = ship_eq_data[equip_tag]
        if equipment_data is not None:
            manufacturer_data = equipment_data['manufacturer']
            if manufacturer_data is not None:
                manufacturer = Manufacturer()
                if 'name' in manufacturer_data:
                    if manufacturer_data['name'] is not None:
                        manufacturer.name = manufacturer_data['name'].strip()
                if 'code' in manufacturer_data:
                    if manufacturer_data['code'] is not None:
                        manufacturer.code = manufacturer_data['code'].strip()
                if 'known_for' in manufacturer_data:
                    if manufacturer_data['known_for'] is not None:
                        manufacturer.known_for = manufacturer_data['known_for'].strip()
                if 'description' in manufacturer_data:
                    if manufacturer_data['description'] is not None:
                        manufacturer.description = manufacturer_data['description'].strip()

                # if manufacturer_data.has_key('name'):
                #     manufacturer.name = manufacturer_data['name'].strip()
                # if manufacturer_data.has_key('code'):
                #     manufacturer.code = manufacturer_data['code'].strip()
                # if manufacturer_data.has_key('known_for'):
                #     manufacturer.known_for = manufacturer_data['known_for'].strip()
                # if manufacturer_data.has_key('description'):
                #     manufacturer.description = manufacturer_data['description'].strip()
                equipment.manufacturer = manufacturer

            if equipment_data['type'] is not None:
                equipment.type = equipment_data['type'].strip()

            if equipment_data['size'] is not None:
                equipment.size = equipment_data['size'].strip()

            if equipment_data['name'] is not None:
                equipment.name = equipment_data['name'].strip()

            # equipment.type = equipment_data['type'].strip()
            # equipment.size = equipment_data['size'].strip()
            # equipment.name = equipment_data['name'].strip()
            ship_equipment.equipment = equipment
        index += 1
        ship_equipment_list.append(ship_equipment)
    return ship_equipment_list


def get_model3d(model_str):
    model_3d_final = ""
    step_one = model_str.split("/media")
    if len(step_one) > 1:
        step_two = step_one[1].split(".ctm")
        if len(step_two) > 1:
            model_3d_final = "/media" + step_two[0] + ".ctm"

    return model_3d_final


def get_ships():
    mysql_helper = MysqlHelper()
    page = 1
    ship_json = get_ship_json(page)
    html = ship_json.get('data').get('html')
    totalrows = ship_json.get('data').get('totalrows')
    rowcount = ship_json.get('data').get('rowcount')
    init_ship(html, mysql_helper)
    need_req_time = float(totalrows) / rowcount
    if need_req_time != 0:
        need_req_time += 1
    for page in range(2, 2 + int(need_req_time)):
        print "正在获取第 " + str(page) + "页数据"
        ship_json = get_ship_json(page)
        html = ship_json.get('data').get('html')
        init_ship(html, mysql_helper)


def init_ship(html, mysql_helper):
    ship_shoup = bs4.BeautifulSoup(html, "lxml")
    ship_elements = ship_shoup.find_all("li", attrs={"class": "ship-item"})
    for ship_element in ship_elements:
        if type(ship_element) is not bs4.Tag:
            continue
        icon_url_tag = ship_element.find("img")
        icon_url = icon_url_tag.attrs['src']
        ship_data = ship_element.find("a", attrs={'class': 'filet'})
        ship_url = ship_data.attrs['href']
        vehicle = init_vehicle(ship_url)
        Log.d("init" + vehicle.name + "的数据")
        vehicle.icon = icon_url
        ship_list.append(vehicle)
        if vehicle.name in StaticField.SHIP_NAME_MAP:
            Log.d(StaticField.SHIP_NAME_MAP[vehicle.name])
        else:
            Log.d(vehicle.name)
        mysql_helper.insert2mysql(vehicle)


def get_ship_json(page):
    url = "https://robertsspaceindustries.com/api/store/getShips"
    pamas = {"itemType": "ships", "page": str(page), "sort": "store", "storefront": "pledge"}
    ships_req = requests.post(url=url, data=pamas)
    ships_json = json.loads(ships_req.content)
    code = ships_json.get('code')
    msg = ships_json.get('msg')
    if msg == "OK" and code == "OK":
        return ships_json
    else:
        return None


def download_file(file_url):
    if len(file_url) > 0:
        file_split = file_url.split('/')
        file_name = StaticField.IMAGE_PATH + file_split[len(file_split) - 1]
        Log.d("准备下载 ： " + file_name)
        url = StaticField.BASE_URL + file_url
        ctm_file = requests.request("GET", url, stream=True, data=None, headers=None)
        total_length = int(ctm_file.headers.get("Content-Length"))
        with open(file_name, "wb") as code:
            widgets = ['Progress: ', progressbar.Percentage(), ' ',
                       progressbar.Bar(marker='#', left='[', right=']'),
                       ' ', progressbar.ETA(), ' ', progressbar.FileTransferSpeed()]
            pbar = progressbar.ProgressBar(widgets=widgets, maxval=total_length).start()
            for chunk in ctm_file.iter_content(chunk_size=1):
                if chunk:
                    code.write(chunk)
                    code.flush()
                pbar.update(len(chunk) + 1)
            pbar.finish()


def create_dir():
    if not os.path.exists(StaticField.IMAGE_PATH):
        # 创建文件夹
        Log.d("创建 保存 图片 文件夹")
        os.makedirs(StaticField.IMAGE_PATH)
    else:
        Log.d("文件夹存在 不需要创建！")


# if __name__ == '__main__':
#     get_ships()
