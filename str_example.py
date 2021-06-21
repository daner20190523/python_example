if __name__ == '__main__':
    str0 = 'aaa'
    str1 = 'bbb'
    # print(str0 + str1)

    str_test = '所有你能想到对字符串的操作都可以用python来试试'
    # print(str_test[5])
    # print(str_test[0: 5])
    # print(str_test[9: -5])
    # print(str_test[9:])
    # print(str_test[-1])
    # print(str_test[-3])
    # print(str_test[-5])
    # print(str_test[-10:-8])
    # print(str_test[-8:-10])
    # print(str_test[0-8])
    # print(len(str_test))
    # print(str_test[26])
    # str_test_replace = '所有你能想到对字符串的操作都可以用python python来试试'
    # print(str_test_replace.replace('python', 'Java', 1))
    # print(str_test_replace.replace('python', 'Java', 2))
    # print(str_test_replace.replace('python', 'Java', 0))
    # print(str_test_replace.replace('python', 'Java', 3))
    # print(str_test_replace.replace('python', 'Java'))

    str_test_split = 'E:\\Python\\PycharmProjects\\python_example'
    split_str = '\\'
    split_after_str_list = str_test_split.split(split_str)
    split_after_str_list1 = str_test_split.split(split_str, 0)
    split_after_str_list2 = str_test_split.split(split_str, 2)
    split_after_str_list3 = str_test_split.split(split_str, 8)
    # print(split_after_str_list)
    # print(split_after_str_list1)
    # print(split_after_str_list2)
    # print(split_after_str_list3)

    str_test_join = 'Python'
    str_test_join2 = ['E:', 'Python', 'PycharmProjects', 'python_example']
    join_str = '||'
    after_join_str = join_str.join(str_test_join)
    after_join_str2 = join_str.join(str_test_join2)
    # print(after_join_str)
    # print(after_join_str2)

    str_test_up_low = 'Python'
    python_upper = str_test_up_low.upper()
    python_lower = str_test_up_low.lower()
    # print(python_upper)
    # print(python_lower)
    # print(python_lower.lower())
    # print(python_upper.upper())

    # str_test_match = '{0}年{1}月{2}日'
    # str_test_match.format()

    str_completion = '001'
    # print(str_completion.rjust(10, '0'))
    # print(str_completion.ljust(10, '0'))

    str_repeat = '重要的事情说三遍  '
    print(str_repeat * 3)
