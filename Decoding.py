def read():
    input = GPIO.input(pin) 
    if input:
        return 1
    else:
        return 0
    
def get(character):
    to_morse = {
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
    '10': '-----'
    }
    new_dict = {}
    
    for k,v in to_morse.iteritems():
        new_dict[v] = k
    if new_dict.has_key(character):
        return new_dict[character]
    else:
        return None

def decode(sequence): #NA NC E
    last_zero = -1
    length = 0
    skip = 0
    character = ""
    sentence = ""
    for i in xrange(len(sequence)):
        if skip == 0:
            if sequence[i]==0:
                if i-last_zero == 2:
                   character = character + "."
                elif i-last_zero == 4:
                    character = character + "-"
                elif i-last_zero == 1:
                    if character != "":
                        sentence = sentence + get(character)
                        character = ""
                    if is_word_end(sequence, i):
                        sentence = sentence + " "
                        skip = 4
                last_zero = i
        else:
            skip = skip - 1
            last_zero = i
    print "("+sentence+")"
         
def is_word_end(sequence, i):
    tot = sum(sequence[i:i+5])
    if tot == 0:
        return True
    return False

if __name__ == "__main__":
    test = [1,1,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,0,1,0,1,1,1,0,1,0,0,0,1,0,0,0,0,0,0,0]
    decode(test)
#     while True:
#         value = read()
#         pulse_sequence.append(value)
# #         end = is_end(pulse_sequence)
# #         if end:
# #             break
#     

