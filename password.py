#!/usr/bin/env python3

# generate a password with length "passlen" with no duplicate characters in the password

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 12
p =  "".join(random.sample(s,passlen ))
print(p)
