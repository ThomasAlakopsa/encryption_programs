import codecs

hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
b64Example = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

#decode the hex String to UTF-8
hexString = codecs.decode(hexString, 'hex');
String= hexString.decode();
print("decoded hex string: ",String);

#encode the UTF-8 hexString to base 64
b64 = codecs.encode(hexString,'base64');

#decode it back too a string for a print
x = b64.decode();
print("b64: ",x);
