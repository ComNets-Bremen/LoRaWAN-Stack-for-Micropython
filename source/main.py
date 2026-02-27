from machine import SPI, Pin
import machine
import time
import ubinascii

## Configuration board
# Uncomment the section you need
##

### Setup for libraries on Heltec V3
#from SX1262 import Transceiver
#PIN_SCK=9
#PIN_MOSI=10
#PIN_MISO=11
#PIN_CS=8
#PIN_RST=12
#PIN_BUSY=13
#PIN_DIO1=14
#DIO_TXCO=True
#spi = machine.SoftSPI(
#        baudrate=400000,
#        sck=PIN_SCK,
#        mosi=PIN_MOSI,
#        miso=PIN_MISO
#        )
#
#cs = Pin(PIN_CS, Pin.OUT, value=1)
#rst = Pin(PIN_RST, Pin.OUT, value=1)
#busy = Pin(PIN_BUSY, Pin.IN)
#dio1 = Pin(PIN_DIO1, Pin.IN)
#transceiver = Transceiver(spi, cs, rst, busy, dio1, DIO_TXCO)


### Setup for MoleNet 7.0 (buggy)
### Connect BUSY to GPIO16
#from SX1262 import Transceiver
#PIN_SCK=14
#PIN_MOSI=47
#PIN_MISO=21
#PIN_CS=48
#PIN_RST=15
#PIN_BUSY=16
#PIN_DIO1=46
#DIO_TXCO=False
#spi = machine.SoftSPI(
#        baudrate=400000,
#        sck=PIN_SCK,
#        mosi=PIN_MOSI,
#        miso=PIN_MISO
#        )

#cs = Pin(PIN_CS, Pin.OUT, value=1)
#rst = Pin(PIN_RST, Pin.OUT, value=1)
#busy = Pin(PIN_BUSY, Pin.IN)
#dio1 = Pin(PIN_DIO1, Pin.IN)
#transceiver = Transceiver(spi, cs, rst, busy, dio1, DIO_TXCO)


### Setup for MoleNet 6.3
from SX1276 import Transceiver
PIN_SCK=14
PIN_MOSI=47
PIN_MISO=21
PIN_CS=48
PIN_RST=45
PIN_DIO=46
spi = machine.SoftSPI(
        baudrate=400000,
        sck=PIN_SCK,
        mosi=PIN_MOSI,
        miso=PIN_MISO
        )

cs = Pin(PIN_CS, Pin.OUT, value=1)
rst = Pin(PIN_RST, Pin.OUT, value=1)
rst = Pin(PIN_RST, Pin.IN)
dio = Pin(PIN_DIO, Pin.IN)
transceiver = Transceiver(spi, cs, rst, dio)


###
# End of config
###

###
# Helper functions
###

def get_machine_id():
    return ubinascii.hexlify(machine.unique_id()).decode("utf-8")

###
# Start of main app
###

FREQ=868.3

transceiver.settings(
    power=17,
    sf=7,
    bw=125,
    cr=4/5,
    syn_word=0x12,
    inv_iq=False,
    crc=True,
    exp_header=True
)


print(f"My id is {get_machine_id()}")
print("Starting RX / TX loop...")

while True:
    print("Sending data...")
    transceiver.send(f"test from {get_machine_id()}", FREQ)
    payload, snr, rssi = transceiver.receive(FREQ)
    print(f"Payload: {payload}")
    print(f"SNR    : {snr}")
    print(f"RSSI   : {rssi}")
    print(f"Meta: {transceiver.get_meta()}")
    time.sleep(5)


