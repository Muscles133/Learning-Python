#insert coin inital input
#if any of the coins that are not 25 10 or 5 reject
#append a value
def main():
    cost = 50
    print("Amount Due: " + str(cost))
    cumulative_sum = 0                                          #staring value

    while cumulative_sum < cost:                                #keep going untill the sum is at lest the cost
        value = int(input("Insert Coin: "))

        if value not in[5, 10, 25]:                             #check the coin value
            print("I only Accept '5' '10' or '25'")

        else:
            cumulative_sum += value                             #add the values

        if cumulative_sum < cost:
            print("Amount Due: " + str(cost-cumulative_sum))    #how much is left
    
                                                                #end of loop 
    change = cumulative_sum - cost
    print("Change Owed " + str(change))

main()
