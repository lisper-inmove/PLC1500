# -*- coding: utf-8 -*-

import argparse
import random

from GetData.parse_xlsx import ParseXlsx
from PLCUtil import PLCUtil
from data_structure.data import Data
from logger import Logger

logger = Logger()


class Main:

    def __init__(self, filename, plc_address):
        self._parser = ParseXlsx(filename)
        self._plc_address = plc_address
        self._db_datas = dict()
        self._plc_utils = dict()

    def read_data(self):
        for db_idx, db in self._parser._dbs.items():
            self.__load_db_datas(db)
            for data in db.datas:
                datatype = data.datatype.upper()
                if datatype == Data.INT:
                    self.read_int(data)
                elif datatype == Data.USINT:
                    self.read_usint(data)
                elif datatype == Data.REAL:
                    self.read_real(data)
                elif datatype == Data.BOOL:
                    self.read_bool(data)
                elif datatype == Data.STRING_ARRAY:
                    self.read_string(data)
                elif datatype == Data.UINT:
                    self.read_uint(data)

    def __load_db_datas(self, db):
        db_datas = self._db_datas.get(db.idx)
        if db_datas is None:
            self.create_plc_utils(db)
            db_datas = self._plc_utils.get(db.idx).load_bytes(db.max_offset)
        return db_datas

    def create_plc_utils(self, db):
        if self._plc_utils.get(db.idx) is not None:
            return
        self._plc_utils.update({
            db.idx: PLCUtil(address=self._plc_address, db_idx=db.idx)
        })

    def read_int(self, data):
        plc_util = self._plc_utils.get(data.db_idx)
        value = plc_util.read_int(data.word_tpe_offset)
        logger.info(f"{data} -> {value}")
        return value

    def read_usint(self, data):
        plc_util = self._plc_utils.get(data.db_idx)
        value = plc_util.read_usint(data.word_tpe_offset)
        logger.info(f"{data} -> {value}")
        return value

    def read_udint(self, data):
        plc_util = self._plc_utils.get(data.db_idx)
        value = plc_util.read_udint(data.word_tpe_offset)
        return value

    def read_real(self, data):
        plc_util = self._plc_utils.get(data.db_idx)
        value = plc_util.read_real(data.word_tpe_offset)
        return value

    def read_bool(self, data):
        plc_util = self._plc_utils.get(data.db_idx)
        value = plc_util.read_bool(data.word_tpe_offset, data.word_bit_offset)
        return value

    def read_string(self, data):
        plc_util = self._plc_utils.get(data.db_idx)
        value = plc_util.read_string(data.word_tpe_offset)
        return value

    def read_string_array(self, data):
        plc_util = self._plc_utils.get(data.db_idx)
        value = plc_util.read_string_array(data.word_tpe_offset, data.string_array_length)
        return value

    def read_uint(self, data):
        plc_util = self._plc_utils.get(data.db_idx)
        value = plc_util.read_uint(data.word_tpe_offset)
        return value


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", dest="filename", help="文件名")
    parser.add_argument("--host", dest="host", help="主机ip地址")
    parser.add_argument("--port", dest="port", help="端口", default=102, type=int)

    args = parser.parse_args()
    obj = Main(
        filename=args.filename,
        plc_address=(args.host, args.port)
    )
    obj.read_data()
