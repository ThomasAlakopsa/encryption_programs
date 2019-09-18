
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

message = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = "ICE"
byte_message = bytes(message, 'utf-8')
byte_key = bytes(key, 'utf-8')

cipher_text = repeating_xor_key(byte_message,byte_key);
print(cipher_text.hex())
