import snap7


class PLCUtil:

    def __init__(
            self,
            host: str = None,
            port: int = None,
            address: tuple = None,
            size: int = None,
            db_idx: int = None,
    ):
        self.client = snap7.client.Client()
        if address is not None:
            host, port = address[0], address[1]
        if port is None:
            port = 102
        if size is None:
            size = 1024
        self.size = size
        self.buf = bytearray(size)
        self.db_idx = db_idx
        self.client.connect(host, 0, 0, tcpport=port)

    def load_bytes(self, size: int):
        self.buf = self.client.db_read(self.db_idx, 0, size)

    def read_int(self, start: int):
        value = snap7.util.get_int(self.buf, start)
        return value

    def write_int(self, start: int, value: int):
        # snap7.util.set_int(self.buf, start, value)
        data = bytearray(2)
        snap7.util.set_int(data, 1, value)
        self.client.db_write(self.db_idx, start, data)

    def read_usint(self, start: int):
        value = snap7.util.get_usint(self.buf, start)
        return value

    def read_udint(self, start: int):
        value = snap7.util.get_udint(self.buf, start)
        return value

    def read_real(self, start: int):
        value = snap7.util.get_real(self.buf, start)
        return value

    def read_bool(self, start: int, bit_offset: int):
        value = snap7.util.get_bool(self.buf, start, bit_offset)
        return value

    def read_string(self, start: int):
        value = snap7.util.get_string(self.buf, start)
        return value

    def read_string_array(self, start: int, length: int):
        result = []
        while length:
            value = snap7.util.get_string(self.buf, start)
            length -= 1
            result.append(value)
        return result

    def write_string(self, start: int, value: str):
        data = bytearray(len(value) + 20)
        snap7.util.set_string(data, len(value) + 10, value)
        self.client.db_write(self.db_idx, start, data)


if __name__ == '__main__':
    # obj = PLCUtil("192.168.0.77", db_idx=1)
    # obj.load_bytes(264)
    # print(obj.read_int(4))
    # print(obj.read_string(6))

    size = 2840
    obj1 = PLCUtil("192.168.0.77", size=size, db_idx=10)
    obj1.load_bytes(size)
    import random
    obj1.write_int(1, random.randint(10, 20))
    print(obj1.read_string(12))
    print(obj1.read_string(268))
    print(obj1.read_string(2828))
