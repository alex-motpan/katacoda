# Find the closest prime number under a certain integer n that has the maximum possible amount of even digits.
# For n = 1000, the highest prime under 1000 is 887, having two even digits (8 twice)
# Naming f(), the function that gives that prime, the above case and others will be like the following below.
# f(1000) ---> 887 (even digits: 8, 8)
# f(1210) ---> 1201 (even digits: 2, 0)
# f(10000) ---> 8887
# f(500) ---> 487
# f(487) ---> 467
# Features of the random tests:

# Number of tests = 28
# 1000 <= n <= 5000000


def f(n):
    result, count, temp = 0, 0, 0
    even_nums = '02468'
    prime_number_list = []

    for num in range(int(n/1.5),n):
        if num % 2 != 0 and pow(2, num-1, num) == 1 and len(str(num)) >= len(str(n)) - 1:
            prime_number_list.append(num)
            
    for prime_number in prime_number_list:
        if len(str(prime_number)) >= len(str(n))-1:
            for number in str(prime_number):
                if number in even_nums:
                    temp += 1
            if temp >= count:
                count = temp
                result = prime_number
            temp = 0
    return result

print("f(1000) ---> 887", f(1000))
print("f(1210) ---> 1201", f(1210))
print("f(10000) ---> 8887", f(10000))
print("f(500) ---> 487", f(500))
print("f(487) ---> 467", f(487))