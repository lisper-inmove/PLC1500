# -*- coding: utf-8 -*-

"""自动装药专机."""

import json

from sanic import Blueprint

from view.unify_response import UnifyResponse


auto_fill_ammo_bp = Blueprint("AutoFillAmmo", url_prefix="/auto-fill-ammo")


@auto_fill_ammo_bp.route("/get")
async def get_auto_fill_ammo(request):
    """获取自动装药专机数据."""
    with open("mock/format-v1.json", "r") as f:
        result = json.load(f)
        return UnifyResponse.R(result)
    return UnifyResponse.R(data="Hello")
