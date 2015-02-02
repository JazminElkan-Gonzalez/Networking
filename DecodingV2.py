import time
import RPi.GPIO as GPIO

class Safeguards:
    def __enter__(self):
        return self
    def __exit__(self,*rabc):
        GPIO.cleanup()
        print("Safe exit succeeded")
        return not any(rabc)

def prepare_pin(pin=23):
    GPIO.setmode(GPIO.BCM)  #use Broadcom (BCM) GPIO numbers on breakout pcb
    
    GPIO.setup(pin,GPIO.IN) # allow pi to read levels

def read_pin(pin):
    return GPIO.input(pin)  # set 3.3V level on GPIO output

def delay(duration):            # sleep for duration seconds where duration is a float.
    time.sleep(duration)

def pulse_to_bit(blinks=200,duration=0.25,pin=23):
    prepare_pin(pin)
    bits = []
    for i in range(blinks):
        bits.append(read_pin(pin))
        delay(duration)
    return bits



if __name__ == "__main__":
    with Safeguards():
       receive()
