# -*- coding: utf-8 -*-

"""Sanic Blueprint Gather"""

from sanic import Sanic

from logger import Logger

from view.engine_dismantle import engine_dismantle_bp
from view.long_tail_tighten import long_tail_tighten_bp


class InitBlueprint:

    @classmethod
    def init(cls, app: Sanic):
        bps = [
            engine_dismantle_bp,  # 发动拆解
            long_tail_tighten_bp,  # 长尾喷管拧紧专机
        ]
        logger = Logger()
        for bp in bps:
            logger.info(f">>>>>>>>>>> 注册: {bp.name} With UrlPrefix {bp.url_prefix}")
            app.blueprint(bp)
