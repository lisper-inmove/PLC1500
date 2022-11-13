# -*- coding: utf-8 -*-

"""文件/目录相关操作模块."""

import os


class FileUtil:
    """文件/目录相关操作类."""

    @staticmethod
    def create_dir_if_not_exists(directory):
        """当目录不存在时创建."""
        if os.path.exists(directory):
            return
        os.makedirs(directory)

    @staticmethod
    def join_path_filename(directory, filename):
        """返回目录文件的绝对路径."""
        filepath = os.path.join(directory, filename)
        return filepath
