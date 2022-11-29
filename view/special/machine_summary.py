# -*- coding: utf-8 -*-

"""专机汇总页."""

import json

from sanic import Blueprint

from view.unify_response import UnifyResponse


machine_summary_bp = Blueprint(
    'MachineSummary',
    url_prefix="/machine-summary"
)


@machine_summary_bp.route("/get", methods=["POST"])
async def get_(request):
    """机器汇总页."""
    with open("mock/format-v2.json", "r") as f:
        result = json.load(f)
        return UnifyResponse.R(result)
    return UnifyResponse.R(data="Hello")
