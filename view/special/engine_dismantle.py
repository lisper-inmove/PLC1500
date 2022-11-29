# -*- coding: utf-8 -*-

"""发动机拆解."""

import json

from sanic import Blueprint

from view.unify_response import UnifyResponse


engine_dismantle_bp = Blueprint('EngineDismantle', url_prefix="/engine-dismantle")


@engine_dismantle_bp.route("/get", methods=["POST"])
async def get_engine_dismantle(request):
    """获取发动拆解数据."""
    with open("mock/format-v1.json", "r") as f:
        result = json.load(f)
        result.update({"title": "发动机拆解专机"})
        return UnifyResponse.R(result)
    return UnifyResponse.R(data="Hello")
