def add_func(n1,n2) :
    return n1+n2

def sub_func(n1,n2) :
    return n1-n2

def mul_func(n1,n2) :
    return n1*n2

num1, num2, res = 100, 200, 0

res = add_func(num1, num2)
print(num1, "+", num2, "=", res)
res = sub_func(num1, num2)
print(num1, "-", num2, "=", res)
res = mul_func(num1, num2)
print(num1, "x", num2, "=", res)
