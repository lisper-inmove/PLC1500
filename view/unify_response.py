# -*- coding: utf-8 -*-

"""统一返回结构"""

from copy import copy

from sanic.response import json


class UnifyResponse:

    SUCCESS = (0, "成功")

    @staticmethod
    def R(data, response_status=None):
        if response_status is None:
            response_status = UnifyResponse.SUCCESS
        result = {
            "errcode": response_status[0],
            "errmsg": response_status[1]
        }
        if data is not None:
            result.update({"data": data})
        return json(result)
