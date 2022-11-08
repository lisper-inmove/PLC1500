import snap7
import struct

plc = snap7.client.Client()
plc.connect('192.168.0.77', 0, 0)  # IP address, rack, slot (from HW settings)
print(plc.get_cpu_info())

db_number = 1
start_offset = 0
bit_offset = 0
value = 1  # 1 = true | 0 = false

start_address = 100  # starting address
length = 4  # double word

def writeBool(db_number, start_offset, bit_offset, value):
    reading = plc.db_read(db_number, start_offset, 1)
    snap7.util.set_bool(reading, 0, bit_offset, value)
    plc.db_write(db_number, start_offset, reading)
    return None

def readBool(db_number, start_offset, bit_offset):
    reading = plc.db_read(db_number, start_offset, 1)
    a = snap7.util.get_bool(reading, 0, bit_offset)
    print('DB Number: ' + str(db_number) + ' Bit: ' + str(start_offset) + '.' + str(bit_offset) + ' Value: ' + str(a))
    return None


# writeBool(db_number, start_offset, bit_offset, value)
readBool(db_number, start_offset, bit_offset)
