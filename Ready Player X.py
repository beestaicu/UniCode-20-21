'''
Ready Player X

It's 2045. Halliday is gone. Every living soul in the OASIS is looking for the Easter egg - the key to Halliday's fortune.

We've found something, a few snippets of deciphered text. Is this enough for you to break his cipher?

Message 1:

Halliday("Crystal Key") == "Pelfgny Xrl"


Message 2

Halliday("Orb of Osuvox") == "Beo bs Bfhibk"


We managed to get a few fragments of some other messages... we'll need the cipher to work on messages with the characters we can see in them, even though we can't get all of their content...

We marked the missing characters with *



Fragment 1:

*l**day("ro** 237") == "eb** 237"


Fragment 2:

*day("An**ak? $ mil**ons?!") == "Nabenx? $ zvyyvbaf?!"


Fragment 3:

**"+- the_distracted_globe -+") == "+- gur_qvfgenpgrq_ty******"

'''



# solution.py
class Cipher:

    def halliday(self, message):
        list = []
        for i in range(0, len(message)):
            if 65 <= ord(message[i]) <= 77 or 97 <= ord(message[i]) <= 109:
                n = chr(ord(message[i]) + 13)
                list.extend(n)
            elif 78 <= ord(message[i]) <= 90 or 110 <= ord(message[i]) <= 122:
                n = chr(ord(message[i]) - 13)
                list.extend(n)
            else:
                list.extend(message[i])

        return (''.join(list))

'''
# tests.py
from solution import Cipher
import unittest

class CipherTests(unittest.TestCase):

    def test1(self):
        solution = Cipher()
        self.assertEqual(solution.halliday("Crystal Key"), "Pelfgny Xrl")

    def test2(self):
        solution = Cipher()
        self.assertEqual(solution.halliday("Orb of Osuvox"), "Beo bs Bfhibk")

if __name__ == '__main__':
    unittest.main()
    
'''