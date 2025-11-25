# Solution to Project Euler Problem 2
# -- Find the sum of all even valued fibonacci numbers below 4,000,000
# -- Result 4613732

def main():
    limit = 4000000
    post_a = 1
    post_b = 2
    total = 2

    while post_b < limit:
        temp = post_a
        post_a = post_b
        post_b = post_a + temp
        if (post_b % 2 == 0):
            total = total+post_b

    print(total)

if __name__ == "__main__":
    main()
