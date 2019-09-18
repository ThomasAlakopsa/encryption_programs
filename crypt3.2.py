#   from itertools import cycle
#import codecs

def bruteforce_single_xor_key(message_bytes):
    for i , key in enumerate('abcdefghijklmopqrstuvwxyz'):
        output_bytes= b''
        for byte in message_bytes:
            output_bytes += bytes([byte ^ ord(key)])
        output_code = output_bytes.decode('utf-8')
        print('%s : %s' % (key, output_code))



message = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
x = bytes.fromhex(message);
bruteforce_single_xor_key(x)
