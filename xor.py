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


def xor_two_byte_strings(b_str1, b_str2):
    bytes_1 = [byte for byte in b_str1]
    bytes_2 = [byte for byte in b_str2]
    xored_bytes = [b1 ^ b2 for b1, b2 in zip(bytes_1, bytes_2)]
    return xored_bytes


""" xor a byte message with a unknown decimal """


def repeating_xor_key(message_bytes, key):
    output_bytes = b''
    index = 0
    for byte in message_bytes:
        output_bytes += bytes([byte ^ key[index]])
        if(index + 1) == len(key):
            index = 0
        else:
            index += 1
    return output_bytes


""" rates a byte string with the given frequency_table """


def rating(i_bytes, frequency):
    rating = 0
    for char in i_bytes.lower():
        char_score = frequency.get(chr(char), 0)
        rating += float(char_score)
    return round(rating, 3)


""" brutefore a byte string and sorts it acourding the function above"""


def bruteforce_single_char_xor_sorted(ciphertext):
    potential_messages = []
    for key_value in range(256):
        message = xor_single_char_key(ciphertext, key_value)
        score = rating(message, frequency_table)
        data = {
            'message': message,
            'score': score,
            'key': key_value
        }
        potential_messages.append(data)
    return sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]


"""" brutefore a hex encoded txt file and sort it with the sort function above"""


def bruteforce_single_char_file_sorted(file_name):
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
        temp_dict_sorted = sorted(
            temp_dict.items(), key=lambda x: x[1], reverse=True)
        rating_dict[l] = temp_dict_sorted[0]

    rating_dict_sorted = sorted(
        rating_dict.items(), key=lambda x: x[1][1], reverse=True)
    sentence = xor_single_char_key(bytes.fromhex(
        rating_dict_sorted[0][0]), rating_dict_sorted[0][1][0])
    return sentence


""" calculate the hamming distance between two byte strings """

def calculate_hamming_distance(byets_str1, bytes_str2):
    hamming_distance = 0
    byte_string = xor_two_byte_strings(byets_str1, bytes_str2)
    for byte in byte_string:
        for bit in bin(byte):
            if (bit == '1'):
                hamming_distance += 1
    return (hamming_distance)


""" break a base64 encoded txt file with a unkown repeating key size"""


def break_repeating_key_xor():
    with open("6.txt")as f:                         #open the file
        ciphertext = base64.b64decode(f.read())     #decode the file
    average_hamming = []                            #init value's
    possible_plaintext = []
    possible_key_lengths = []
    for keysize in range(2, 42):                    #take possible key range of 2 tot 42
        hamming = []

        """ devide the ciphertext in chucks the size of possible key size """

        chunks = [ciphertext[i:i + keysize]
                  for i in range(0, len(ciphertext), keysize)]

        """ calculate the hamming_distance with help of the first 10 chuncks  """

        for i in range(0, 10):
            chunk_0 = chunks[i]
            chunk_1 = chunks[i + 1]
            ham = calculate_hamming_distance(chunk_0, chunk_1)
            hamming.append(ham / keysize)

        result = {
            'key': keysize,
            'avg hamming': sum(hamming) / len(hamming) #normalize the hamming
        }
        average_hamming.append(result)

    """ sort all the possible keys and save the one with the smallest hamming distace"""
    possible_key_lengths = sorted(
            average_hamming, key=lambda x: x['avg hamming'])[0]

    key_lenght = possible_key_lengths['key']


    key = b''
    for i in range(key_lenght):
        block = b''
        for j in range(i, len(ciphertext), key_lenght):
            block += bytes([ciphertext[j]]) #safe ciphertext in byte blocks of the key keysize
        key += bytes([bruteforce_single_char_xor_sorted(block)['key']]) #brutefore the ciphertext blocks
    possible_plaintext.append((repeating_xor_key(ciphertext, key), key))
    return max(possible_plaintext, key=lambda x: rating(x[0], frequency_table))


""" run opdracht 6 """
print(break_repeating_key_xor())
