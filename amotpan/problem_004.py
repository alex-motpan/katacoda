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
    lenght_num = len(str(n))
    
    def is_prime(n):
        if n == 2:
            return False
        return True if ((2  << (n - 2)) - n) % n == 1 else False


    def count_even(n):
        count = 0
        while n >= 10:
            if n % 10 % 2 == 0:
                n //= 10
                count += 1
                if n <= 10 and n % 2 == 0:
                    count += 1
                    n = 0
                    return count
            else:
                n //= 10
        return count
    
    even_count, prime_count = 0, 0
    
    while len(str(n)) >= lenght_num - 1:
        n -= 1
        if n % 2 != 0 and is_prime(n):
            even = count_even(n)
            if even > even_count:
                even_count = even
                prime_count = n

    return prime_count


print("f(1000) ---> 887", f(1000))
print("f(1210) ---> 1201", f(1210))
print("f(10000) ---> 8887", f(10000))
print("f(500) ---> 487", f(500))
print("f(487) ---> 467", f(487))
