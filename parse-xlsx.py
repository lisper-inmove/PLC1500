# -*- coding: utf-8 -*-

"""解析xlsx数据模块."""

import os


class ParseXlsx:
    """解析xlsx数据类."""

    datapath = f"{os.path.realpath(os.path.dirname(__file__))}/data"

    def __init__(self, filename):
        """解析xlsx数据初始化函数.

        Args:
            filename: 文件路径
              如果filename是绝对路径,则以filename为准
              如果filename是相对路径,则文件需要放在项目根目录下的data目录下
        """
        if not os.path.isabs(filename):
            self._filepath = os.path.join(self.datapath, filename)
        else:
            self._filepath = filename
        if not os.path.exists(self._filepath):
            raise Exception(f"{self._filepath}不存在")
        if not self._filepath.endswith("xlsx"):
            raise Exception("文件需要以xlsx结尾")


if __name__ == '__main__':
    obj = ParseXlsx("test.txt")
