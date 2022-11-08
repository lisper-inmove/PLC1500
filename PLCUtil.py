import snap7


class PLCUtil:

    def __init__(self, host: str):
        self.client = snap7.client.Client()
        self.client.connect(host, 0, 0)

    def load_bytes(self, db_number: int, size: int):
        self.buf = self.client.db_read(db_number, 0, size)

    def read_int(self, start: int):
        value = snap7.util.get_int(self.buf, start)
        return value

    def read_string(self, start: int):
        value = snap7.util.get_string(self.buf, start)
        return value

    def read_boolean(self, start: int, bit_offset: int):
        value = snap7.util.get_bool(self.buf, start, bit_offset)
        return value


if __name__ == '__main__':
    obj = PLCUtil('192.168.0.77')
    obj.load_bytes(1, 264)
    print(obj.read_int(4))
    print(obj.read_string(6))
    print(obj.read_boolean(262, 1))
