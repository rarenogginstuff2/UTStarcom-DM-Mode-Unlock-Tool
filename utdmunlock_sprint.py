#UTStarcom DM Unlock Tool ©2023 Rare Noggin Stuff

import serial
import struct

ser = serial.Serial(
#Set COM port to your phone!
    port='COM1',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

print("UTStarcom DM Unlock Tool ©2023 Rare Noggin Stuff")
print("Unlocking DM Mode...")
thestring1 = (b"\x41\x54\x24\x51\x43\x44\x4D\x47\x0D\x0A")
thestring2 = (b"\x2E\x64\x00\x00\xCE\xC3\xC2\x77\x00\x00\x33\x00\xB0\xF0\x12\x00\x00\x00\x33\x00\xDB\x01\x91\x7C\xC9\xC3\xC2\x77\xF0\xEF\x12\x00\x00\x00\x33\x00\x03\x00\x00\x00\x6C\xEF\x01\x00\x03\x00\x00\x00\x74\xEF\x12\x00\x20\xE9\x90\x7C\x68\xF0\x01\x00\x02\x00\x00\x00")
thestring3 = (b"\x84\xEF\x12\x00\xFF\xFF\xFF\xFF\x78\xF0\x12\x00\xB8\x7A\x7E")
thestring4 = (b"\x2E\x64\x00\x00\xCE\xC3\xC2\x77\x00\x00\x33\x00\xB0\xF0\x12\x00\x00\x00\x33\x00\xDB\x01\x91\x7C\xC9\xC3\xC2\x77\xF0\xEF\x12\x00\x00\x00\x33\x00\x03\x00\x00\x00\x6C\xEF\x01\x00\x03\x00\x00\x00\x74\xEF\x12\x00\x20\xE9\x90\x7C\x68\xF0\x01\x00\x02\x00\x00\x00")
thestring5 = (b"\x84\xEF\x12\x00\xFF\xFF\xFF\xFF\x78\xF0\x12\x00\xB8\x7A\x7E")
thestring6 = (b"\x2E\x65\x00\xC1\xF7\x00\x00\x00\xEE\x00\x00\x00\x02\x00\x00\x00\x5E\x00\x00\x00\x06\x00\x00\x00\x0F\x00\x00\x00\xA8\x68\x02\x10\xE5\x00\x00\x00\xAB\x82\x00\x10\xAC\x6A\x02\x10\xC4\x6A\x02\x10\x00\x00\x00\x00\xA8\x68\x02\x10\x68\xF0\x01\x46\x20\xC3\x01\x10")
thestring7 = (b"\x00\x00\x00\x00\x4B\x05\x97\xF8\xAE\xE2\x13\xDB\xCC\xA3\x7E")
thestring8 = (b"\x2E\x30\x00\x00\x74\xEF\x12\x00\x20\xE9\x90\x7C\x68\xF0\x01\x00\x02\x00\x00\x00\x84\xEF\x12\x00\xFF\xFF\xFF\xFF\x78\xF0\x12\x00\x20\xE9\x90\x7C\x60\x00\x91\x7C\xFF\xFF\xFF\xFF\x5D\x00\x91\x7C\xDE\xC2\xC2\x77\x00\x00\x33\x00\x00\x00\x00\x00\xE3\xC2\xC2\x77")
thestring9 = (b"\xB7\x68\x02\x10\x60\x01\x00\x00\xA8\x68\x02\x10\x23\xDD\x7E")
thestring10 = (b"\x00\x78\xF0\x7E")
thestring11 = (b"\x0C\x14\x3A\x7E")
thestring12 = (b"\x20\xE9\x90\x7C\x60\x00\x91\x7C\xFF\xFF\xFF\xFF\x5D\x00\x91\x7C\xDE\xC2\xC2\x77\x00\x00\x33\x00")
thestring13 = (b"\x00\x00\x00\x00\xE3\xC2\xC2\x77\xA8\x68\x02\x10\xA0\x2A\x33\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xF0\x12\x00\x00\xF0\x12\x00\x3C\xEE\x12\x00\x38\xEE\x12\x00\x80\xF0\x12\x00\x80\xF0\x12\x00\x94\x5C\xC3\x77\x70\x20\xC1\x77\xFF\xFF\xFF\xFF\xE3\xC2\xC2\x77")
thestring14 = (b"\x7B\xA7\x01\x10\xE0\xBE\xEC\x7E")
data=(thestring1 + thestring2 + thestring3 + thestring4 + thestring5 + thestring6 + thestring7 + thestring8 + thestring9 + thestring10 + thestring11 + thestring12 + thestring13 + thestring14)

ser.write(data)
s = ser.read(1)
#print(s)
ser.close()
print("DM Mode Unlocked, try using any Qualcomm DM Mode Tool")