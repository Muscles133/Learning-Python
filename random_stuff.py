import random
import statistics
import sys
import cowsay
import requests

# cards = ['jack', 'queen', 'king']

# random.shuffle(cards)
# for card in cards:
#     print(card)


# print (statistics.mean([100,90]))

# print ("hello my name is ", sys.argv[1])


if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
