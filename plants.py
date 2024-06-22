from soil import sample

def main():
    moisture = sample()
    days = 0
    print(f"moisture is {moisture}%")

    while moisture > 20:
        moisure = sample()
        days += 1
        print(f"Day {days}: moisture is {moisture}%")

    print("Time to water!")

main()