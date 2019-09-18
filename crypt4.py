
#from xor import xor_single_char_key, break_xor_char_key
from frequency import english_test


def xor_bytes(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def xor_single_char_key(msg, key):
    print(key);
    print(msg);
    return xor_bytes(msg, bytes([key] * len(msg)))

def break_xor_char_key(ciphertext, quality_test=english_test):
    return rank_xor_char_keys(ciphertext, quality_test)[0]


def rank_xor_char_keys(ciphertext, quality_test=english_test):
    possible_keys = range(127)
    decryptions = [(key, xor_single_char_key(ciphertext, key))
                   for key in possible_keys]
    # sort with a tuple to get deterministic results on quality equality
    best_decryptions = sorted(decryptions,
                              key=lambda key_decryption:
                              (quality_test(key_decryption[1]),
                               key_decryption[1]),
                              reverse=True)
    keys = [key for key, _ in best_decryptions]
    return keys


with open("hexlineAll.txt") as f:
    ciphers = [bytes.fromhex(line.strip()) for line in f.readlines()]

message = max([xor_single_char_key(cipher, break_xor_char_key(cipher))
               for cipher in ciphers],
              key=english_test).decode('ascii')

print(message)
#print (ciphers)
