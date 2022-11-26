# -*- coding: utf-8 -*-

"""长尾喷管拧紧专机."""

import json

from sanic import Blueprint

from view.unify_response import UnifyResponse


long_tail_tighten_bp = Blueprint('LongTailTighten', url_prefix="/long-tail-tighten")


@long_tail_tighten_bp.route("/get")
async def get_long_tail_tighten(request):
    """获取长尾喷管拧紧专机数据."""
    with open("mock/format-v1.json", "r") as f:
        result = json.load(f)
        return UnifyResponse.R(result)
    return UnifyResponse.R(data="Hello")
