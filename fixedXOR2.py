import numpy
import codecs

def bxor_numpy(b1, b2):
    #readthevalues
    n_b1 = numpy.frombuffer(b1, dtype='uint8')
    n_b2 = numpy.frombuffer(b2, dtype='uint8')

    #XORs them toghther and covert them back to a string
    return (n_b1 ^ n_b2).tostring()


# starting strings
s1="1c0111001f010100061a024b53535009181c"
s2="686974207468652062756c6c277320657965"

#decode them too hexadecimal
h1 = codecs.decode(s1, 'hex');
h2 = codecs.decode(s2, 'hex');

XOR = bxor_numpy(h1,h2)
print (XOR)
print (codecs.encode(XOR,'hex'))
