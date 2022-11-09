# We are interested in collecting the sets of six prime numbers, that having a starting prime p,
# the following values are also primes forming the sextuplet [p, p + 4, p + 6, p + 10, p + 12, p + 16]
# The first sextuplet that we find is [7, 11, 13, 17, 19, 23]
# The second one is [97, 101, 103, 107, 109, 113]
# Given a number sum_limit, you should give the first sextuplet which sum (of its six primes) surpasses the sum_limit value.
# find_primes_sextuplet(70) == [7, 11, 13, 17, 19, 23]
# find_primes_sextuplet(600) == [97, 101, 103, 107, 109, 113]
# Features of the tests:
# Number Of Tests = 18
# 10000 < sum_limit < 29700000


def find_primes_sextuplet(sum_limit):
    # your code here
    prime_number_list, result = [], []
    def_key, dict_1 = 1, {}

    for num in range(1,sum_limit):
        if pow(2, num-1, num) == 1:
            prime_number_list.append(num)

    for num_index in range(len(prime_number_list)-5):
        one, two = prime_number_list[num_index], prime_number_list[num_index + 1]
        three, four = prime_number_list[num_index + 2], prime_number_list[num_index + 3]
        five, six = prime_number_list[num_index + 4], prime_number_list[num_index + 5]
        
        total_sum = one + two + one + two + five + six
        
        if one + 4 == two and two + 2 == three and three + 4 == four and four + 2 == five and five + 4 == six and total_sum > sum_limit:
            result += one, two, three, four, five, six
            break
    return result
    
#Test
test_case = {70: [7, 11, 13, 17, 19, 23], 600: [97, 101, 103, 107, 109, 113]}
for key, value in test_case.items():
    if find_primes_sextuplet(key) == value:
        print(f'find_primes_sextuplet{key} = {value} -> OK!')
    else:
        print(f'find_primes_sextuplet{key} != {value} -> NOT OK!')