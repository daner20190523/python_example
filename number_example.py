def to_2jinzhi(num):
    result = ''
    while num != 0:
        result += str(num % 2)
        num = num // 2
    num_2 = result[::-1].rjust(8, '0')
    print(num_2)
    return num_2


if __name__ == '__main__':
    a = 10
    b = 4
    # print('加\t', a + b)
    # print('减\t', a - b)
    # print('乘\t', a * b)
    # print('除\t', a / b)
    # print('取模\t', a % b)
    # print('幂\t', a ** 2)
    # print('取商\t', a // 2)

    # print(a > b)
    # print(a < b)
    # print(a == b)
    # print(a != b)
    # print(a >= b)
    # print(a <= b)

# print(True and False)
# print(True or False)
# print(not True)
# print(not False)
# print(11 and 2)
# print(11 or 2)
# print(not 11)
# print(not 'you')
# print('you' and 'me')


# print('s' in '321312s')
# print('s' in '321312')
# print('s' not in '321312')
# print(1 not in [1, 2, 3])
# print(1 in [1, 2, 3])
# print(1 in (1, 2, 3))
c = 20
d = 20
e = 10
# print(c is c)
# print(c is d)
# print(c is e)
# print(c is not d)
# print(c is not e)
# print(id(c))
# print(id(d))
x = 89
y = 13
x_binary = to_2jinzhi(x)
y_binary = to_2jinzhi(y)
print(x & y)
print(x | y)
print(x ^ y)
print(~ y)
print(y << 2)
print(y >> 2)







