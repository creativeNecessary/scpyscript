from CitizenWikiRobot.StaticField import StaticField
from CitizenWikiRobot.Log import Log
import sys
import bs4

reload(sys)
sys.setdefaultencoding('utf-8')


class CommLink:
    def __init__(self):
        self.id = -1
        self.url = ""
        self.background = ""
        self.title = ""
        self.type = ""
        self.content = []


class CommLinkContent:
    def __init__(self):
        self.data_index = -1
        self.content_type = ""
        self.content_data = ""
        self.machine_translate_data = ""
        self.human_translate_data = ""
