#
## Introducton to Python breadboarding
#
import time
import RPi.GPIO as GPIO

class Safeguards:
    def __enter__(self):
        return self
    def __exit__(self,*rabc):
        GPIO.cleanup()
        print("Safe exit succeeded")
        return not any(rabc)

To_Morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "10": "-----",
    "*": "..--"
}

To_Binary= {
    ".": "10",
    "-": "1110",
    " ": "00",
    "  ": "0000",
    "..--": "11110001111"
    }

def to_binary(message):
    morse = encode(message).split("  ")
    binary = ""
    for word in morse:
        binary += "00".join([To_Binary[x] for x in word]) + "0000"
    print(binary)

    

def encode(message):
    words = message.upper().split(" ")
    morse = ""
    for word in words:
        morse += " ".join([To_Morse[x] for x in word]) + "  "
    print(morse)
    return morse
    
def prepare_pin(pin=17):
    GPIO.setmode(GPIO.BCM)  #use Broadcom (BCM) GPIO numbers on breakout pcb
    
    GPIO.setup(pin,GPIO.OUT) # allow pi to set 3.3v and 0v levels

def turn_high(pin):
    GPIO.output(pin,GPIO.HIGH)  # set 3.3V level on GPIO output

def turn_low(pin):
    GPIO.output(pin,GPIO.LOW)  # set ground (0) level on GPIO output

def delay(duration):    # sleep for duration seconds where duration is a float.
    time.sleep(duration)


    
        
def blink(blinks=30,duration=1,pin=17):
    prepare_pin(pin)

    
    for i in range(blinks):
        turn_high(pin)
        delay(duration)
        turn_low(pin)
        delay(duration)
 


if __name__ == "__main__":
    to_binary("Hi Bonnie *")
##    with Safeguards():
##        blink()

    
    
