# -*- coding: utf-8 -*-

import os

from GetData.parse_xlsx import ParseXlsx


obj = ParseXlsx("special-signal.xlsx")
with open("special-singal.dumps", "w") as f:
    obj.dump(f)
