from itertools import cycle
from frequency import english_test
import codecs

def xor_bytes(byte_msg, byte_key):
    return bytes([x ^ y for x, y in zip(byte_msg, byte_key)])

def xor_single_char_key(msg, key):
    return xor_bytes(msg, bytes([key] * len(msg)))


def scoring(current_string):
    posible_highscore = 0;
    #print(current_string)
    for letter in current_string.lower():
        #print(letter)
        if ((letter >= 97 and letter <= 118) or letter == 32):
            posible_highscore += 1;
        else:
            posible_highscore -= 1;
    return posible_highscore;

def crack_single_charracter_XOR(message):
    current_highscore = -30;
    possible_target = "";
    for i in range(180):
        cyphered = xor_single_char_key(message, i)
        posible_highscore = scoring(cyphered)
        if (posible_highscore > current_highscore):
            current_highscore = posible_highscore;
            possible_target = cyphered;
    return possible_target

with open ("4.txt") as f:
    lines = f.read().splitlines()

for l in lines:
    current_highscore = -30;
    l_bytes = bytes.fromhex(l)
    p = crack_single_charracter_XOR(l_bytes)
    final_score = scoring(p)
    if (final_score > current_highscore):
        current_highscore = final_score;
        final = p;

print(final)
