import bs4
from bs4 import NavigableString
from CitizenWikiRobot.StaticField import StaticField
import requests
import json
from CitizenWikiRobot.Log import Log
from CitizenWikiRobot.comm_link import CommLink
from CitizenWikiRobot.comm_link import CommLinkContent
from CitizenWikiRobot.MysqlHelper import MysqlHelper
import time
import sys
import bs4

reload(sys)
sys.setdefaultencoding('utf-8')


def get_galactic_guide():
    mysql_helper = MysqlHelper()
    s = requests.Session()
    url = 'https://robertsspaceindustries.com/api/hub/getCommlinkItems'
    road_header = {
        'Connection': 'close',
        'x-rsi-token': '6ec0661bc4216ad2b6017727e59349e7',
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'user-agent': 'Mozilla/5.0 Chrome/66.0.3359.139 Mobile Safari/537.36',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }
    for page in range(0, 6):
        galactic_guide_req = ''
        pamas = {"channel": "spectrum-dispatch", "page": str(page), "series": "galactic-guide", "sort": "publish_new"}
        while galactic_guide_req == '':
            try:
                galactic_guide_req = s.post(url=url, data=pamas, headers=road_header)

            except:
                print("Connection refused by the server..")
                print("Let me sleep for 5 seconds")
                print("ZZzzzz...")
                time.sleep(5)
                print("Was a nice sleep, now let me continue...")
                continue

        galactic_guide_json = json.loads(galactic_guide_req.content)
        data = galactic_guide_json['data']
        guide_soup = bs4.BeautifulSoup(data, "lxml")
        for link in guide_soup.findAll('a'):
            guide_url = link.get('href')
            if guide_url is None:
                continue
            icon_origin_data = link.find('div', class_='background').get('style')
            start_index = icon_origin_data.find('(')
            end_index = icon_origin_data.find(')')
            background = icon_origin_data[start_index + +2:end_index - 1]
            title_tag = link.find('div', class_='title trans-opacity trans-03s')
            title = title_tag.string
            comm_link = CommLink()
            comm_link.type = 'galactic_guide'
            comm_link.url = guide_url
            comm_link.title = title
            comm_link.background = background
            link_page = ''
            while link_page == '':
                try:
                    link_page = requests.get(StaticField.BASE_URL + guide_url)
                except:
                    print("Connection refused by the server..")
                    print("Let me sleep for 5 seconds")
                    print("ZZzzzz...")
                    time.sleep(5)
                    print("Was a nice sleep, now let me continue...")
                    continue

            link_soup = bs4.BeautifulSoup(link_page.content, "lxml")

            content_block1_tag = link_soup.find('div', class_='content-block1 rsi-markup')
            content_tag = content_block1_tag.find('div', class_='content')

            first_image_tag = link_soup.find('div', class_='content clearfix')
            if first_image_tag is not None:
                image_tag = first_image_tag.find('img')
                if image_tag is not None:
                    first_image_comm_content = CommLinkContent()
                    first_image_comm_content.content_type = "image"
                    first_image_comm_content.content_data = image_tag.get('src')
                    first_image_comm_content.data_index = 0
                    # Log.d(first_image_comm_content.content_data)
                    comm_link.content.append(first_image_comm_content)

            content = content_tag.find_all('div', class_='variant-block')
            if len(content) > 0:
                for div in content:
                    get_comm_link_content(comm_link, div.children)
            else:
                get_comm_link_content(comm_link, content_tag.children)
            mysql_helper.insert_comm_link(comm_link)

            Log.d(title)


def get_comm_link_content(comm_link, content_list):
    from CitizenWikiRobot.translate_util import TransLateUtil
    translate_util = TransLateUtil()
    for sub_content in content_list:
        if sub_content is None or isinstance(sub_content, NavigableString):
            continue
        name = sub_content.name
        if name == 'p' or name == 'h2':
            comm_content = CommLinkContent()
            if sub_content.text:
                if name == 'h2':
                    comm_content.content_data = sub_content.text
                    comm_content.content_type = "title"
                if name == 'p':
                    comm_content.content_data = sub_content.text
                    comm_content.machine_translate_data = translate_util.translate(sub_content.text)
                    Log.d(comm_content.machine_translate_data)
                    comm_content.content_type = "content"
                comm_content.data_index = len(comm_link.content)
                comm_link.content.append(comm_content)
                # Log.d(comm_content.content_data)
        if name == 'a':
            comm_content_image = CommLinkContent()
            comm_content_image.content_type = "image"
            comm_content_image.content_data = sub_content.get('data-source_url')
            comm_content_image.data_index = len(comm_link.content)
            comm_link.content.append(comm_content_image)
            # Log.d(comm_content_image.content_data)
