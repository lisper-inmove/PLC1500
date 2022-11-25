# -*- coding: utf-8 -*-

import os


class SysEnv:

    APPNAME = 'APPNAME'
    # console
    LOGGER_ENABLE_CONSOLE = "LOGGER_ENABLE_CONSOLE"
    # SYSLOG
    LOGGER_ENABLE_SYSLOG = "LOGGER_ENABLE_SYSLOG"
    LOGGER_SYSLOG_HOST = "LOGGER_SYSLOG_HOST"
    LOGGER_SYSLOG_PORT = "LOGGER_SYSLOG_PORT"
    LOGGER_SYSLOG_FACILITY = "LOGGER_SYSLOG_FACILITY"
    # FILE
    LOGGER_ENABLE_FILE = "LOGGER_ENABLE_FILE"
    LOGGER_FILE_DIRECTORY = "LOGGER_FILE_DIRECTORY"
    LOGGER_LEVEL = "LOGGER_LEVEL"

    @staticmethod
    def get_env(key, default=None):
        value = os.environ.get(key, default)
        if value == 'true':
            return True
        if value == 'false':
            return False
        return value

    @staticmethod
    def set_env(key, value):
        os.environ[key] = value
