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

rating_dict = {}

def xor_byte(byte_msg, byte_key):
    return bytes([x ^ y for x, y in zip(byte_msg, byte_key)])

def xor_bytes(msg, key):
    return xor_byte(msg, bytes([key] * len(msg)))



def rating(i_bytes, frequency):
    rating = 0
    for char in i_bytes.lower():
        char_score = frequency.get(chr(char), 0)
        rating += float(char_score)
    return round(rating, 3)

with open ("4.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

for l in lines:
    str_bytes = bytes.fromhex(l)
    temp_dict = {}
    for i in range(127):
        string = xor_bytes(str_bytes, i)
        rtng = rating(string, frequency_table)
        temp_dict[i] = rtng
        temp_dict_sorted = sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)
        rating_dict[l] = temp_dict_sorted[0]

rating_dict_sorted = sorted(rating_dict.items(), key=lambda x: x[1][1], reverse=True)
# print(rating_dict_sorted[0])
sentence = xor_bytes(bytes.fromhex(rating_dict_sorted[0][0]), rating_dict_sorted[0][1][0])
print(sentence)
