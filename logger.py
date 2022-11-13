# -*- coding: utf-8 -*-

"""日志处理模块."""

import logging
import uuid
import socket
from logging.handlers import SysLogHandler

from util.sys_env import SysEnv
from util.file_util import FileUtil


class Logger(logging.Logger):
    """日志处理类."""

    def __init__(self):
        """日志处理类初始化函数."""
        self._message_uuid = uuid.uuid4()
        name = SysEnv.get_env(SysEnv.APPNAME)
        if name is None:
            name = "Default"
        self.name = name
        super().__init__(self.name)
        _formatter = f'{self.name}: %(asctime)s - %(levelname)s - %(message)s'
        self._formatter = logging.Formatter(_formatter)
        self.__set_level()
        self.__init_syslog_handler()
        self.__init_console_handler()
        self.__init_file_handler()

    def __wrap_message_with_uuid(self, message):
        result = f"{self._message_uuid} - {message}"
        return result

    def __name_to_level(self, name):
        return logging._nameToLevel[name]

    def debug(self, message):
        """记录debug日志."""
        message = self.__wrap_message_with_uuid(message)
        super().debug(message)

    def info(self, message):
        """记录info日志."""
        message = self.__wrap_message_with_uuid(message)
        super().info(message)

    def exception(self, message):
        """记录exception日志."""
        message = self.__wrap_message_with_uuid(message)
        super().exception(message)

    def error(self, message):
        """记录错误日志."""
        message = self.__wrap_message_with_uuid(message)
        super().error(message)

    def warning(self, message):
        """记录警告日志."""
        message = self.__wrap_message_with_uuid(message)
        self.logger.warning(message)

    def fatal(self, message):
        """记录致命日志."""
        message = self.__wrap_message_with_uuid(message)
        super().fatal(message)

    def __init_syslog_handler(self):
        """设置syslog日志."""
        enable = SysEnv.get_env(SysEnv.LOGGER_ENABLE_SYSLOG)
        if enable is None or enable == "false":
            return
        host = SysEnv.get_env(SysEnv.LOGGER_SYSLOG_HOST)
        port = int(SysEnv.get_env(SysEnv.LOGGER_SYSLOG_PORT))
        facility = SysEnv.get_env(SysEnv.LOGGER_SYSLOG_FACILITY)
        self.__create_syslog_handler(host, port, facility)

    def __create_syslog_handler(self, host, port, facility):
        handler = SysLogHandler(
            address=(host, port),
            facility=SysLogHandler.facility_names[facility],
            # socktype=socket.SOCK_STREAM # TCP
        )
        handler.setFormatter(self._formatter)
        handler.setLevel(self._level)
        self.addHandler(handler)

    def __init_console_handler(self):
        """设置终端日志."""
        enable = SysEnv.get_env(SysEnv.LOGGER_ENABLE_CONSOLE)
        if enable is None or enable == "false":
            return
        handler = logging.StreamHandler()
        handler.setFormatter(self._formatter)
        self.addHandler(handler)

    def __init_file_handler(self):
        """设置文件日志."""
        enable = SysEnv.get_env(SysEnv.LOGGER_ENABLE_FILE)
        if enable is None or enable == "false":
            return
        directory = SysEnv.get_env(SysEnv.LOGGER_FILE_DIRECTORY)
        FileUtil.create_dir_if_not_exists(directory)
        filename = f'{logging._levelToName.get(self._level).lower()}.log'
        filepath = FileUtil.join_path_filename(directory, filename)
        self.__create_file_handler(filepath)

    def __create_file_handler(self, filepath):
        handler = logging.FileHandler(filepath)
        handler.setLevel(self._level)
        handler.setFormatter(self._formatter)
        self.addHandler(handler)

    def __set_level(self):
        level = SysEnv.get_env(SysEnv.LOGGER_LEVEL)
        _level = logging.INFO
        if level == 'INFO':
            _level = logging.INFO
        elif level == 'DEBUG':
            _level = logging.DEBUG
        if level == 'ERROR':
            _level = logging.ERROR
        if level == 'FATAL':
            _level = logging.FATAL
        self.setLevel(_level)
        self._level = _level


if __name__ == '__main__':
    SysEnv.set_env(SysEnv.LOGGER_ENABLE_CONSOLE, 'true')
    SysEnv.set_env(SysEnv.LOGGER_ENABLE_SYSLOG, 'true')
    SysEnv.set_env(SysEnv.LOGGER_SYSLOG_HOST, 'logger.server')
    SysEnv.set_env(SysEnv.LOGGER_SYSLOG_PORT, '514')
    SysEnv.set_env(SysEnv.LOGGER_SYSLOG_FACILITY, 'local7')
    SysEnv.set_env(SysEnv.LOGGER_ENABLE_FILE, 'true')
    SysEnv.set_env(SysEnv.LOGGER_FILE_DIRECTORY, '/tmp/logs/')

    import random
    logger = Logger()
    logger.info(f"test-{random.randint(1, 1000)}")
