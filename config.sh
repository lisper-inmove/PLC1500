#!/bin/bash

export APPNAME=PLC1500
export LOGGER_ENABLE_CONSOLE=true
export LOGGER_ENABLE_SYSLOG=false
export LOGGER_SYSLOG_HOST=logger.server
export LOGGER_SYSLOG_PORT=514
export LOGGER_SYSLOG_FACILITY=local7
export LOGGER_ENABLE_FILE=false
export LOGGER_FILE_DIRECTORY=/tmp/logs
export LOGGER_LEVEL=INFO
export ROOT_PATH=`pwd`
export PYTHONPATH=$ROOT_PATH
export DEBUG=true
