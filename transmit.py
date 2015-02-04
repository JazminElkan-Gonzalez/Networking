from BJ_Morse03 import *
import time
import RPi.GPIO as GPIO

class Safeguards:
    def __enter__(self):
        return self
    def __exit__(self,*rabc):
        GPIO.cleanup()
        print("Safe exit succeeded")
        return not any(rabc)

def prepare_pin(pin=17):
    GPIO.setmode(GPIO.BCM)  #use Broadcom (BCM) GPIO numbers on breakout pcb
    
    GPIO.setup(pin,GPIO.OUT) # allow pi to set 3.3v and 0v levels

def turn_high(pin=17):
    GPIO.output(pin,GPIO.HIGH)  # set 3.3V level on GPIO output

def turn_low(pin=17):
    GPIO.output(pin,GPIO.LOW)   # set ground (0) level on GPIO output

def delay(duration):            # sleep for duration seconds where duration is a float.
    time.sleep(duration)  
        
def blink(blinks=30,duration=1,pin=17):
    prepare_pin(pin)

    for i in range(blinks):
        turn_high(pin)
        delay(duration)
        turn_low(pin)
        delay(duration)

def main():
	MorseCodeStack = BJ_Stack((
        msg2words,
        word2letters,
        letter2dotsanddashes,
        dotordashormark2pulse
        ))
	message = input('Enter Message: ').upper()

	words = msg2words.fn(message)
	letters = words2letters.fn(words)

	morse = ""
	for letter in letters:
		morse += letter2dotsanddashes.fn(letter)

	
	pulses = []
	for mark in morse:
		pulses.append(dotordashormark2pulse.fn(mark))

	prepare_pin()

	print(pulses)
	with Safeguards():
		for pulse in pulses:
			if pulse[0]:
				turn_high()
			else:
				turn_low()
			delay(pulse[1])


if __name__ == "__main__":
	main()