>>> import string
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.digits
'0123456789'
>>> string.punctuations
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    string.punctuations
AttributeError: module 'string' has no attribute 'punctuations'
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> string.hexdigits
'0123456789abcdefABCDEF'
>>> string.octdigits
'01234567'
>>> test_string1= "The prime minister of india is gonna be great 21st century"
>>> test_string1.isalpha()
False
>>> test_string.isnumeric()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    test_string.isnumeric()
NameError: name 'test_string' is not defined
>>> test_string1.isnumeric()
False
>>> test_string1.isalnum()
False
>>> k=" ".join([c for c in test_string1 if c in string.ascii_letters])
>>> k
'T h e p r i m e m i n i s t e r o f i n d i a i s g o n n a b e g r e a t s t c e n t u r y'
>>> 
