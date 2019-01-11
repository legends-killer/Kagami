# -*- coding: UTF-8 -*-
# 电费爬虫

from urllib import parse, request
import re

class PowerRate:
    url = "http://wap.xt.beescrm.com/base/electricityHd/queryResult/ele_id/7/community_id/57/building_id/286/floor_id/2095/room_id/36085/flag/1"

    def get(self):
        req = request.Request(url = self.url)
        response = request.urlopen(req)
        response = response.read()
        regex = '.*2d9fd3">(.*)</span>.*'   # 正则匹配获取电费

        matches = re.findall(regex, str(response))

        for match in matches:
            price = str(match[:-14])

        return price

