##Simple Code For Euler Project Problem 1
# -- Find the sum of all the multiples of 3 or 5 below 1000 --
# -- Result: 233168

def main():
    sum = 0
    for i in range(1000):
        if(i%3 == 0 or i % 5 == 0):
            sum = sum+i
    print(sum)

#
if __name__ == "__main__":
    main()
