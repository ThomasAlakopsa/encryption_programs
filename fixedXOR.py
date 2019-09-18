
import codecs

def foo(inputStr,key):
    nuOfIt = len(key)
    output=""
    for i in range(nuOfIt):
        current = inputStr[i]
        current_key = key[i]
        output += chr(ord(current) ^ ord(current_key))
    return output

s1="1c0111001f010100061a024b53535009181c"
s2="686974207468652062756c6c277320657965"

h1 = codecs.decode(s1, 'hex');
h2 = codecs.decode(s2, 'hex');

x = foo(h1,h2);
print (x)
print (x.encode('hex'))
