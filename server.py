# -*- coding: utf-8 -*-


"""Main Service"""

from sanic import Sanic

from view.blueprint import InitBlueprint


app = Sanic("PLCService")

InitBlueprint.init(app)
