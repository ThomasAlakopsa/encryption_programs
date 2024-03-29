import base64
import codecs

frequency_table = {
    "a": 8.167,
    "b": 1.492,
    "c": 2.782,
    "d": 4.253,
    "e": 12.702,
    "f": 2.228,
    "g": 2.015,
    "h": 6.094,
    "i": 6.966,
    "j": 0.153,
    "k": 0.772,
    "l": 4.025,
    "m": 2.406,
    "n": 6.749,
    "o": 7.507,
    "p": 1.929,
    "q": 0.095,
    "r": 5.987,
    "s": 6.327,
    "t": 9.056,
    "u": 2.758,
    "v": 0.987,
    "w": 2.360,
    "x": 0.150,
    "y": 1.947,
    "z": 0.074,
    " ": 10.000
}

"""xor two bytes toghther"""


def xor_bytes(byte_msg, byte_key):
    return bytes([x ^ y for x, y in zip(byte_msg, byte_key)])


""" xor a byte message with one decimal """


def xor_single_char_key(msg, key):
    return xor_bytes(msg, bytes([key] * len(msg)))


def xor_two_byte_strings(b_str1,b_str2):
    bytes_1 = [byte for byte in b_str1]
    bytes_2 = [byte for byte in b_str2]
    xored_bytes = [b1 ^ b2 for b1,b2 in zip(bytes_1, bytes_2)]
    return xored_bytes


""" xor a byte message with a unknown decimal """


def brute_force_single_char_msg_all(msg):
    all = []
    for i in range(256):
        all.append(xor_single_char_key(msg, i))
    return (all)
    # print ('%s : %s' % (z,i))


def repeating_xor_key(message_bytes, key):
    output_bytes = b''
    index = 0
    for byte in message_bytes:
        output_bytes += bytes([byte ^ key[index]])
        if(index + 1) == len(key):
            index = 0;
        else:
            index += 1
    return output_bytes;


def rating(i_bytes, frequency):
    rating = 0
    for char in i_bytes.lower():
        char_score = frequency.get(chr(char), 0)
        rating += float(char_score)
    return round(rating, 3)

def brute_force_single_char_message_sorted(text, key):
    for i in range(key):
        str = xor_single_char_key(text, i)
        rate = rating(str, frequency_table)
        temp_dict[i] = rate
    temp_dict_sorted = sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)
    rating_dict[l] = temp_dict_sorted[0]

    rating_dict_sorted = sorted(rating_dict.items(), key=lambda x: x[1][1], reverse=True)
    sentence = xor_single_char_key(bytes.fromhex(rating_dict_sorted[0][0]), rating_dict_sorted[0][1][0])
    return sentence


def brute_force_single_char_file_sorted(file_name):
    temp_dict = {}
    rating_dict = {}
    with open(file_name) as f:
        lines = f.read().splitlines()

    for l in lines:
        str_bytes = bytes.fromhex(l)
        for i in range(127):
            str = xor_single_char_key(str_bytes, i)
            rate = rating(str, frequency_table)
            temp_dict[i] = rate
        temp_dict_sorted = sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)
        rating_dict[l] = temp_dict_sorted[0]

    rating_dict_sorted = sorted(rating_dict.items(), key=lambda x: x[1][1], reverse=True)
    sentence = xor_single_char_key(bytes.fromhex(rating_dict_sorted[0][0]), rating_dict_sorted[0][1][0])
    return sentence



def calculate_hamming_distance(byets_str1, bytes_str2):
    hamming_distance = 0
    byte_string= xor_two_byte_strings(byets_str1,bytes_str2)
    for byte in byte_string:
        for bit in bin(byte):
            if (bit == '1'):
                hamming_distance += 1
    return (hamming_distance)

def break_repeating_key_xor():
    with open("6.txt")as f:
        ciphertext = base64.b64decode(f.read())
    average_hamming = []
    for keysize in range(2,42):
        hamming = []
        chunks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]
        while True:
            try:
                chunk_0 = chunks[0]
                chunk_1 = chunks[1]
                ham = calculate_hamming_distance(chunk_0,chunk_1)
                hamming.append(ham/keysize)
                del chunks[0]
                del chunks[1]
            except Exception as e:
                break
        result = {
            'key': keysize,
            'avg hamming': sum(hamming) / len(hamming)
        }
        average_hamming.append(result)
    possible_key_lengths = sorted(average_hamming, key=lambda x: x['avg hamming'])[0]
    print(possible_key_lengths)

    key = b''
    possible_key_length = possible_key_lengths['key']
    for i in range(possible_key_length):

        # Creates an block made up of each nth byte, where n
        # is the keysize
        block = b''
        for j in range(i, len(ciphertext), possible_key_length):
            block += bytes([ciphertext[j]])
        key += bytes([brute_force_single_char_file_sorted(block)['key']])
    print ()


    #average_hamming = []
#print(brute_force_single_char_message_sorted("4.txt"))
#break_repeating_key_xor("6.txt")

#str1 = "this is a test"
#str2 = "wokka wokka!!!"

str = "36170f580c10190c580c101d5808190a0c0158110b58120d150811161f7572"
b_str = str.decode()
#print(brute_force_single_char_message_sorted(b_str))
#print(brute_force_single_char_file_sorted("hexline.txt"))

#b_str1 = str1.encode()
#b_str2 = str2.encode()

#print(calculate_hamming_distance(b_str1,b_str2))
#print(break_repeating_key_xor())
