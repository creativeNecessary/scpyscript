# -*- coding: UTF-8 -*-
import hashlib
import random
import requests
import time
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

s = requests.Session()
m = hashlib.md5()


class TransLateUtil:
    def __init__(self, need_translate_data):
        self.need_translate_data = need_translate_data
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
            'Referer': 'http://fanyi.youdao.com/',
            'contentType': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='
        self.base_config()

    def base_config(self):
        """
        设置基本的参数，cookie
        """
        s.get('http://fanyi.youdao.com/')

    def translate(self):
        salf = str(int(time.time() * 1000) + random.randint(0, 9))
        n = 'fanyideskweb' + self.need_translate_data + salf + "rY0D^0'nM0}g5Mm1z%1G4"
        m.update(n.encode('utf-8'))
        sign = m.hexdigest()
        data = {
            'i': self.need_translate_data,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salf,
            'sign': sign,
            'doctype': 'json',
            'version': "2.1",
            'keyfrom': "fanyi.web",
            'action': "FY_BY_DEFAULT",
            'typoResult': 'false'
        }
        resp = s.post(self.url, headers=self.headers, data=data)
        json_dump = json.dumps(resp.json())
        json_data = json.loads(json_dump)
        result = ""
        if 'translateResult' in json_data:
            translate_result = json_data['translateResult']
            for result_item in translate_result:
                for item in result_item:
                    ch = item['tgt']
                    result = result + ch
        return result
