"""DESCRIPTION:
Part of Series 2/3
This kata is part of a series on the Morse code. Make sure you solve the previous part before you try this one. After you solve this kata, you may move to the next one.


In this kata you have to write a Morse code decoder for wired electrical telegraph.
Electric telegraph is operated on a 2-wire line with a key that, when pressed, connects the wires together, 
which can be detected on a remote station. The Morse code encodes every character being transmitted 
as a sequence of "dots" (short presses on the key) and "dashes" (long presses on the key).

When transmitting the Morse code, the international standard specifies that:

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
However, the standard does not specify how long that "time unit" is. And in fact different operators 
would transmit at different speed. An amateur person may need a few seconds to transmit a single character, 
a skilled professional can transmit 60 words per minute, and robotic transmitters may go way faster.

For this kata we assume the message receiving is performed automatically by the hardware 
that checks the line periodically, and if the line is connected (the key at the remote station is down), 1 is recorded, 
and if the line is not connected (remote key is up), 0 is recorded. After the message is fully received, 
it gets to you for decoding as a string containing only symbols 0 and 1.

For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may be received as follows:

1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011

As you may see, this transmission is perfectly accurate according to the standard, and the hardware sampled 
the line exactly two times per "dot".

That said, your task is to implement two functions:

Function decodeBits(bits), that should find out the transmission rate of the message, 
correctly decode the message to dots ., dashes - and spaces (one between characters, three between words) 
and return those as a string. Note that some extra 0's may naturally occur at the beginning and the end of a message, 
make sure to ignore them. Also if you have trouble discerning if the particular sequence of 1's is a dot or a dash, 
assume it's a dot.
2. Function decodeMorse(morseCode), that would take the output of the previous function and return a human-readable string.

NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

The Morse code table is preloaded for you (see the solution setup, to get its identifier in your language).


Eg:
  morseCodes(".--") //to access the morse translation of ".--"
All the test strings would be valid to the point that they could be reliably decoded as described above, 
so you may skip checking for errors and exceptions, just do your best in figuring out what the message is!

Good luck!

After you master this kata, you may try to Decode the Morse code, for real.
"""


MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

def decode_bits(bits):
    zero = '0'
    bits_list = []
    zero_list = []
    count = 0
    if bits.startswith("0"):
        bits = bits.strip("0")
    if zero not in bits:
        return '.'  # Повертаємо 'E', якщо нулі відсутні
    
    for index, bit in enumerate(bits):
        if bit == "0":
            count += 1
            if index == len(bits) - 1:
                zero_list.append(count)
        else:
            zero_list.append(count)
            count = 0
    filtered_zero_list = [x for x in zero_list if x != 0]
    print("filtered_zero_list", filtered_zero_list)
    
    for index, bit in enumerate(bits):
        if bit == "1":
            count += 1
            if index == len(bits) - 1:
                bits_list.append(count)
        else:
            bits_list.append(count)
            count = 0
    filtered_bits_list = [x for x in bits_list if x != 0]
    print("filtered_bits_list", filtered_bits_list)
    
    if len(filtered_zero_list) > 1:
        multiplier = min(filtered_zero_list)
    elif len(filtered_zero_list) == 1 and filtered_zero_list[0] == 1:
        multiplier = 1
    elif len(filtered_zero_list) == 1 and filtered_zero_list[0] == 2:
        multiplier = 2
    elif len(filtered_zero_list) == 1 and filtered_zero_list[0] == 3 and filtered_zero_list[0] != min(filtered_bits_list):
        multiplier = 1
    elif len(filtered_zero_list) == 1 and filtered_zero_list[0] == 3 and filtered_zero_list[0] % min(filtered_bits_list) == 0:
        multiplier = 3
    elif len(filtered_zero_list) == 1 and filtered_zero_list[0] % 3 != 0 and filtered_zero_list[0] % 7 != 0:
        multiplier = filtered_zero_list[0]
    elif len(filtered_zero_list) == 1 and filtered_zero_list[0] % 3 == 0:
        multiplier = int(filtered_zero_list[0] / 3)
    print("multiplier", multiplier)
    return bits.replace(multiplier*'111', '-').replace(multiplier*'000', ' ').replace(multiplier*'1', '.').replace(multiplier*'0', '')

def decode_morse(morse_code):
    if len(morse_code) == 1:
        return MORSE_CODE[morse_code]
    list_words = []
    sentence = ([i.split() for i in morse_code.split("   ")])
    for word in sentence:
        for char in word:
            list_words.append(MORSE_CODE[char])
        if sentence.index(word) < len(sentence) - 1:
            list_words.append(" ")
    new_sentence = "".join(list_words).strip()
    return new_sentence
    # return morseCode.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')


if __name__=="__main__":
    bit_code = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"
    bit_code1  = "10001"
    print(decode_bits(bit_code1))
    print(decode_morse(decode_bits(bit_code1)))
    