import random

cards = ["jack", "queen", "king"]

def main():
    # print(random.choice(cards))
    # print(random.choices(cards, k=2)) #replaces card back in
    # print(random.sample(cards, k=2)) # without replacement unique selection
    #print(random.choices(cards, weights=[75,20,5], k=2)) # sets weights
    random.seed(1) #set generation for fix the random in place
    print(random.choices(cards, k=2))




main()