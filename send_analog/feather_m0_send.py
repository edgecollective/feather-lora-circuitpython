import board
import busio
import digitalio
import time
import adafruit_rfm9x
from analogio import AnalogIn

# lora radio
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.RFM9X_CS)
reset = digitalio.DigitalInOut(board.RFM9X_RST)
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)


led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

uart = busio.UART(board.TX, board.RX, baudrate=1200)

A0=AnalogIn(board.A0)

def blink(delay,num_times):
    for i in range(num_times):
        led.value=True
        time.sleep(delay)
        led.value=False
        time.sleep(delay)

while True:

    reading=A0.value
    send_str=str(reading)
    print("sending ...",send_str)

    rfm9x.send(send_str)
    blink(.1,1)

    time.sleep(1)
