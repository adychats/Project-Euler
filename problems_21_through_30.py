import os
my_path = os.path.abspath(os.path.dirname(__file__))
names_path = os.path.join(my_path, "names.txt")

import string

#Problem 21
def problem21():
    """
    Project Euler Problem 21
    https://projecteuler.net/problem=21

    The problem:

    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    """

    factor_sum_dict = {}

    for i in range(1,10001):
        factor_sum_dict[i] = sum_factors(i)

    amicable_numbers_list = []
    for i in range(1,10001):
        for j in range(i + 1, 10001):
            if factor_sum_dict[i] == j and factor_sum_dict[j] == i:
                amicable_numbers_list.append(i)
                amicable_numbers_list.append(j)
    print(problem21.__doc__)
    print("    Answer: The sum of all amicable numbers less than 10000 is {num}.".format(num = sum(amicable_numbers_list)))


def problem22():
    """
    Project Euler Problem 22
    https://projecteuler.net/problem=22

    The problem:

    Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
    Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to 
    obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 
    938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
    """
    with open(names_path, 'r') as file:
        names = file.read()
        names_list = names.split('","')

    names_list.sort()
    alphabet_dict = {}
    counter = 1
    for i in string.ascii_uppercase:
        alphabet_dict[i] = counter
        counter += 1
    def score_name(name):
        """
        Returns the sum of the letter scores in the name, assuming a = 1, b = 2, ... , z = 26.
        """
        score = 0
        for i in name:
            score += alphabet_dict[i]

        return score

    total_score = 0

    for i in range(len(names_list)):
        total_score += score_name(names_list[i]) * (i + 1)

    print(problem22.__doc__)
    print("    Answer: The total of all name scores in the file is {score}.".format(score = total_score))

#Problem 23
def problem23():
    """
    Project Euler Problem 23
    https://projecteuler.net/problem=23

    The problem:

    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
    For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of 
    two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as 
    the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that
    the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
    """
    abundant_numbers_list = []
    for i in range(1, 20162):
        if sum_factors(i) > i:
            abundant_numbers_list.append(i)

# we now have a list that is sorted, making our job a bit easier.
    
    def is_sum_of_abundant_numbers(n: int):
        """
        Returns True if n is a sum of 2 abundant numbers, False otherwise.
        """
        i = 0
        temp = abundant_numbers_list[i]
        while temp < n:
            try:
                if sum_factors(n - temp) > (n - temp):
                    return True
                i += 1
                temp = abundant_numbers_list[i]
            except IndexError:
                return False
        else:
            return False

    total_sum = 0
    for j in range(1, 20162):
        if not is_sum_of_abundant_numbers(j):
            total_sum += j

    print(problem23.__doc__)
    print("    Answer: The sum of all positive integers that cannot be written as a sum of abundant numbers \
is {num}.".format(num = total_sum))
#------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------- Helper functions ---------------------------------------------------------------

def sum_factors(n: int):
    """
    Finds the sum of proper divisors of n.
    """
    factor_list = []
    for i in range(1, int(n ** 0.5 + 1)):
        if n % i == 0:
            if (n/i == i):
                factor_list.append(i)
            else:
                factor_list.append(i)
                factor_list.append(n/i)
    return int(sum(factor_list) - n)