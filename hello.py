# 这是注释，不被python解释器执行的
# print('hello python')
col_a = 1
col_b = 2
col_c = 3
# 一个语句分多行显示加 \
row = col_a + \
      col_b + \
      col_c
print(row)
# 语句包含()[]{}的直接回车换行，不需要连接符
print('hello '
      'python')
print(['hello '
       'python'])
print({'hello '
       'python'})
print(2)

word_zero = ' '
word_one = 'hello'
word_two = "your's world"
word_three = '''
你好
世界
你好
python
好好学习
天天向上
'''
print(word_zero)
print(word_one)
print(word_two)
print(word_three)
# input('请输入一些字符，按下回车键Enter退出\n')
x = 'Aa'
y = 'Bb'
X = 'Xx'
# 输出在一行
print(x + y + X)
# 分隔下输出的结果方便查看
print('-' * 20)
print(x, y, X)
print('-' * 20)
# 换行输出
print(x, end='')
print(y)
print(X)

a = 1
if a == 1:
    print('变量a是1')
    print(a+1)
else:
    print('变量a不是1')

