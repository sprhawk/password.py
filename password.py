#!/usr/bin/env python3

# generate a password with length "passlen" with no duplicate characters in the password

import random

SYMBOL = "!@#$%^&*()?_-\;'"
UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
DIGIT = '0123456789'

DEFAULT_LEN = 12

def generate(sample, length):
    random.seed()
    # p =  "".join(random.sample(sample,length ))
    p = random.choices(sample, k=length)
    p = "".join(p)
    return p
    
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()

    group.add_argument('-a', '--alphabet', help='[a-zA-Z]', action='store_true')
    group.add_argument('-u', '--uppercase', help='[A-Z]', action='store_true')
    group.add_argument('-l', '--lowercase', help='[a-z]', action='store_true')
    parser.add_argument('-s', '--symbol', help=r'symbols', action='store_true')
    parser.add_argument('-d', '--digit', help='[0-9]', action='store_true')
    parser.add_argument('-c', '--count', type=int, help='length of generated code')

    # parser.set_defaults(alphabet=True, symbol=True, digit=True, count=DEFAULT_LEN)
    parser.set_defaults(count=DEFAULT_LEN)
    args = parser.parse_args()

    # how to use argparse to handle this?
    if not (args.alphabet or args.uppercase or args.lowercase) \
       and not args.digit and not args.symbol:
        args.alphabet = True
        args.digit = True
        args.symbol = True
        
    samples = []
    if args.alphabet:
        samples.append(UPPERCASE)
        samples.append(LOWERCASE)
    elif args.uppercase:
        samples.append(UPPERCASE)
    elif args.lowercase:
        samples.append(LOWERCASE)

    if args.digit:
        samples.append(DIGIT)

    if args.symbol:
        samples.append(SYMBOL)

    sample = "".join(samples)

    p = generate(sample, args.count)
    print(p)
