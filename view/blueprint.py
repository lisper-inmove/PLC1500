# -*- coding: utf-8 -*-

"""Sanic Blueprint Gather"""

from sanic import Sanic

from logger import Logger

from view.special import auto_fill_ammo_bp
from view.special import depth_test_bp
from view.special import engine_dismantle_bp
from view.special import firebox_tighten_bp
from view.special import long_tail_tighten_bp
from view.special import machine_summary_bp


class InitBlueprint:

    @classmethod
    def init(cls, app: Sanic):
        bps = [
            auto_fill_ammo_bp,                               # 自动装药专机
            depth_test_bp,                                   # 深度测试专机
            engine_dismantle_bp,                             # 发动拆解
            firebox_tighten_bp,                              # 燃烧室拧紧专机
            long_tail_tighten_bp,                            # 长尾喷管拧紧专机
            machine_summary_bp,                              # 机器汇总页
        ]
        logger = Logger()
        for bp in bps:
            logger.info(f">>>>>>>>>>> 注册: {bp.name} With UrlPrefix {bp.url_prefix}")
            app.blueprint(bp)
