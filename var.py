user_name = 'admin'
phone_num = '15003340338' #全局变量
weight = 50
weight_unit = 'kg'

user_name, phone_num, weight, weight_unit = 'admin', '15003340338', 50, 'kg'

user_info = [user_name, phone_num, weight, weight_unit]
print(user_info)

phone_num = '15003340338'  # 全局变量


def update_phone_num():
    phone_num_new = '15100883569'  # 局部变量
    # print(phone_num_new)
    # print(phone_num)


# print(phone_num_new)

if __name__ == '__main__':
    # print(phone_num_new)
    update_phone_num()

phone_num = '18401102010'
print(phone_num)