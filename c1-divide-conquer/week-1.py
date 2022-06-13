from math import ceil

# ====================
# Class definition
# ====================

class Karatsuba:
    """Karatsuba's alogrithm on integer multiplication"""

    def add_zero(num1, num2):
        str1 = str(num1)
        str2 = str(num2)
        n0 = len(str1) - len(str2)
        while not n0 == 0:
            if n0 > 0:
                str2 = '0' + str2
            if n0 < 0:
                str1 = '0' + str1
            n0 = len(str1) - len(str2)
        return str1, str2

    def mul(num1, num2):
        str1, str2 = Karatsuba.add_zero(num1, num2)
        n = len(str1)
        if n > 1:
            hdigit = ceil(n/2.) 

            a = str1[:hdigit]
            b = str1[hdigit:]
            c = str2[:hdigit]
            d = str2[hdigit:]

            ac = Karatsuba.mul(int(a), int(c))
            bd = Karatsuba.mul(int(b), int(d))

            a_b = int(a) + int(b)
            c_d = int(c) + int(d)
            sum = Karatsuba.mul(a_b, c_d)
            ad_bc = sum - ac - bd

            res = ac*10**((n - hdigit)*2) + (ad_bc)*10**(n - hdigit) + bd
            # print(res, '==', num1*num2)
            return res
        else:
            return num1*num2

# ====================
# Main
# ====================

# num1 = 4535
# num2 = 1235

num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627

print(Karatsuba.__doc__)
# print(Karatsuba.add_zero(1, 10))
print(Karatsuba.mul(num1, num2))
print(num1*num2)
