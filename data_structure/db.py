class DB:

    @property
    def datas(self):
        return self._datas

    @property
    def idx(self):
        return self._idx

    @property
    def max_offset(self):
        return self._max_offset

    def __init__(self, idx):
        self._idx = idx
        self._datas = list()
        self._max_offset = 0

    def add_data(self, data):
        self._datas.append(data)
        self._max_offset = max(self._max_offset, data.word_tpe_offset)
