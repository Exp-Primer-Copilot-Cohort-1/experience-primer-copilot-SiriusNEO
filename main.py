# Write a program which can compute the GCD of two numbers.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Write a test for gcd function
def test():
    assert gcd(12, 4) == 4
    assert gcd(4, 12) == 4
    assert gcd(5, 12) == 1
    assert gcd(12, 5) == 1
    assert gcd(12, 0) == 12
    assert gcd(0, 12) == 12
    assert gcd(0, 0) == 0
    assert gcd(1, 1) == 1
    assert gcd(1, 0) == 1
    assert gcd(0, 1) == 1
    print("All tests passed")

# Main function
def main():
    test()
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("GCD of {} and {} is {}".format(a, b, gcd(a, b)))

if __name__ == "__main__":
    main()