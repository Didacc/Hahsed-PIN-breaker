#Made by Didacc 

import sys

from numpy import empty
from Crypto.Hash import SHA256

import argparse

from termcolor import colored

parser = argparse.ArgumentParser(description='4 digit hashed PIN breaker')
parser.add_argument("hashedPIN", help="The PIN hashed in SHA256 that you want to break.", type=str)
parser.add_argument('-s', '--salt',
                    type=str,
                    required=False,
                    help='The salt added at the beginning already hashed in SHA256')
args = parser.parse_args()


pinHashed = args.hashedPIN

if args.salt:
	saltHashed = args.salt

	for i in range(0,10):
		for j in range(0,10):
			for z in range(0,10):
				for c in range(0,10):
					
					toHash = saltHashed + str(i) + str(j) + str(z) + str(c)
					toHash = bytes(toHash, 'utf-8')				

					if SHA256.new(toHash).hexdigest() == pinHashed:
						print(colored("\n[*]The pin is: " + str(i) + str(j) + str(z) + str(c) + '\n','blue'))
						sys.exit(0)

else:
	for i in range(0,10):
		for j in range(0,10):
			for z in range(0,10):
				for c in range(0,10):
					
					toHash = str(i) + str(j) + str(z) + str(c)
					toHash = bytes(toHash, 'utf-8')				

					if SHA256.new(toHash).hexdigest() == pinHashed:
						print(colored("\n[*]The pin is: " + str(i) + str(j) + str(z) + str(c) + '\n','blue'))
						sys.exit(0)

print(colored("\n[!]No valid hashed PIN found\n",'red'))
sys.exit(1)

