from itertools import cycle
import codecs

def crack_single_charracter_XOR(message):

    for i ,key in enumerate('abcdefghijklmopqrstuvwxyz'):
        cyphered = b''.join(chr(ord(a)^ord(b)) for a,b in zip(message, cycle(key)))
        dMessage = b''.join(chr(ord(c)^ord(k)) for c,k in zip(cyphered, cycle(key)))
        print('%s ^ %s = %s ' % (dMessage, key , cyphered))
        print('%s ^ %s = %s ' % (cyphered, key , dMessage))
        #cyphered = cyphered.lower();
        #print(cyphered)


message = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
dMessage = codecs.decode(message, 'hex');
print(dMessage);
#crack_single_charracter_XOR(message)
#crack_single_charracter_XOR(dMessage)
