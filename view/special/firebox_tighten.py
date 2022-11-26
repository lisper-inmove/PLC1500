# -*- coding: utf-8 -*-

"""燃烧室拧紧专机."""

import json

from sanic import Blueprint

from view.unify_response import UnifyResponse


firebox_tighten_bp = Blueprint('FireboxTighten', url_prefix="/firebox-tighten")


@firebox_tighten_bp.route("/get")
async def get_firebox_tighten(request):
    """获取燃烧室拧紧专机数据."""
    with open("mock/format-v1.json", "r") as f:
        result = json.load(f)
        return UnifyResponse.R(result)
    return UnifyResponse.R(data="Hello")
