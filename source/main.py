#Testing libraries on Heltec V3

from SX1262 import Transceiver
from machine import SPI, Pin
import machine
import utime

spi = machine.SoftSPI(baudrate=400000, sck=9, mosi=10, miso=11)
cs = Pin(8, Pin.OUT, value=1)
rst = Pin(12, Pin.OUT, value=1)
busy = Pin(13, Pin.IN)
dio1 = Pin(14, Pin.IN)

sx1262 = Transceiver(spi, cs, rst, busy, dio1)


sx1262.send("25 byte test Transmission")
msg = sx1262.receive()
print(sx1262.get_meta())
