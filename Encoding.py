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
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '10': '-----',
    '*': '*'
}

To_Binary = {
    '-': '1110',
    '.': '10',
    ' ': '0000',
    '*': '11110'
}

def to_morse(message):
    morse = []
    words = message.split(' ')
    for word in words:
        for letter in word:
            morse.append(To_Morse[letter])
        morse.append(' ')
    return morse

def to_binary(morseList):

    binary = ''
    
    for letter in morseList:
        for character in letter:
            binary += To_Binary[character]
        if (letter != ' '):
            binary += '00'
    print(binary)
    return binary

def to_pulse(binMessage):
    duration = 1
    prepare_pin()
    for i in binMessage:
        if (i == '1'):
            turn_high()
            delay(duration)
        elif (i == '0'):
            turn_low()
            delay(duration)

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
    message = input('Enter Message: ').upper() + '*'
    to_pulse(to_binary(to_morse(message)))


if __name__ == "__main__":
    #with Safeguards():
    #    blink()

    main()
