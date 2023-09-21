import time
import machine

led0 = machine.Pin(0, machine.Pin.OUT)
led1 = machine.Pin(1, machine.Pin.OUT)
led2 = machine.Pin(2, machine.Pin.OUT)


led0.on()
time.sleep(3)
led0.off()

led1.on()
time.sleep(3)
led1.off()

led2.on()
time.sleep(3)
led2.off()
