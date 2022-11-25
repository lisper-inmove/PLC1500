# -*- coding: utf-8 -*-

"""发动机拆解."""

from sanic import Blueprint

from view.unify_response import UnifyResponse


engine_dismantle_bp = Blueprint('EngineDismantle', url_prefix="/engine-dismantle")


@engine_dismantle_bp.route("/get")
async def get_engine_dismantle(request):
    """获取发动拆解数据."""
    return UnifyResponse.R(data="Hello")
