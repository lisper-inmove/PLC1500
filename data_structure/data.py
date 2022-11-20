class Data:

    INT = "INT"
    UINT = "UINT"
    USINT = "USINT"

    @property
    def name(self):
        return self._name

    @property
    def datatype(self):
        return self._datatype

    @property
    def raw_address(self):
        return self._raw_address

    @property
    def comment(self):
        return self._comment

    @property
    def db_idx(self):
        return self._db_idx

    @property
    def word_tpe(self):
        return self._word_tpe

    @property
    def word_tpe_offset(self):
        return self._word_tpe_offset

    @property
    def word_bit_offset(self):
        return self._word_bit_offset

    @property
    def row_idx(self):
        return self._row_idx

    @row_idx.setter
    def row_idx(self, row_idx):
        self._row_idx = row_idx

    def __init__(
            self,
            name: str,
            datatype: str,
            raw_address: str,
            category_name: str,
            comment: str = None,
    ):
        self._name = name
        self._datatype = datatype
        self._raw_address = raw_address
        self._comment = comment
        self._category_name = category_name
        self._row_idx = None
        self.__parse_raw_address()

    def __parse_raw_address(self):
        address = self.raw_address.split(".")
        self._db_idx = int(address[0][2:])
        self._word_tpe = address[1][0:3]
        self._word_tpe_offset = int(address[1][3:])
        self._word_bit_offset = None
        if len(address) == 3:
            self._word_bit_offset = int(address[2])

    def __str__(self):
        msg = f"""
        文件中的行数: {self.row_idx}
        名称: {self.name}
        数据类型: {self.datatype}
        PLC地址: {self.raw_address}
        备注: {self.comment}
        数据库索引: {self.db_idx}
        字类型: {self.word_tpe}
        数据偏移量: {self.word_tpe_offset}
        位偏移量(只有boolean数据才会有值): {self.word_bit_offset}"""
        return msg
