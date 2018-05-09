import bs4
from CitizenWikiRobot.StaticField import StaticField
import requests
import json
from CitizenWikiRobot.Log import Log
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def init_road_map():
    url = 'https://robertsspaceindustries.com/api/roadmap/v1/boards/1'
    road_header = {
        'x-rsi-token': '6ec0661bc4216ad2b6017727e59349e7',
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'user-agent': 'Mozilla/5.0 Chrome/66.0.3359.139 Mobile Safari/537.36',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'

    }
    road_map_req = requests.get(url=url, headers=road_header)
    road_map_json = json.loads(road_map_req.content)
    data = road_map_json['data']
    road_map_releases_json = data['releases']
    # "category_id": 6 ships and vehicle
    # "category_id": 7 weapon and items
    # "category_id": 3 characters
    # "category_id": 4 locations
    # "category_id": 2 game_play
    # "category_id": 5 AI
    # "category_id": 1 Core Tech
    Log.d(road_map_releases_json)
