# -*- coding: utf-8 -*-

"""深度测试专机."""

import json

from sanic import Blueprint

from view.unify_response import UnifyResponse


depth_test_bp = Blueprint('DepthTest', url_prefix="/depth-test")


@depth_test_bp.route("/get", methods=["POST"])
async def get_depth_test(request):
    """获取深度测试专机数据."""
    with open("mock/format-v1.json", "r") as f:
        result = json.load(f)
        result.update({"title": "深度测试专机"})
        return UnifyResponse.R(result)
    return UnifyResponse.R(data="Hello")
