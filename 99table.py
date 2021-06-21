if __name__ == '__main__':
    for i in range(1, 10):
        for j in range(1, i+1):
            # print(str(i) + '*' + str(j) + '=' + str(i * j) + '\t', end='')
            print('{1}*{0}={2}\t'.format(i, j, i*j), end='')
        print()


列表 = [1, 2, 3, 4]
print(列表)




def 说句话(name):
    print(name + '说哈哈哈')


说句话('刘国泰')
