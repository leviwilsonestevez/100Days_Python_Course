# Write your code below this line 👇
from math import sqrt


def prime_checker(number):
    # no lets check from 2 to sqrt(n)
    # if we found any facto then we can print as not a prime number
    # this flag maintains status whether the n is prime or not
    prime_flag = 0
    if number > 1:
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                prime_flag = 1
                break
        if prime_flag == 0:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")
    else:
        print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
