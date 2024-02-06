import re

dic = {
    'posts': 'sdsad', 
    'followers': 'qwwqewqe', 
    'following': 'eweeeeee',
}

dicc = {
    'post': 'aaaaaa', 
    'ddd': 'dddddd', 
    'bbb': 'bbbbb',
}
# 리스트는 안댐
# item = []

# for i in dic:
#     item.append(i)

# print(item[1]['posts'])

item = []
item.append(dicc)
print(dicc)
dic['ppp'] = item
print(dic)

ll = ['aaa', 'bbb', 'ccc']


# tags = re.findall(r'#[^Ws#,\\]+', ll)
# listTostring = '\n'.join(ll)
# print(listTostring)

tags = ['#첫번째 공백', '#두번쨰', '#세번째 ']
fillist = []
for i in tags:
    if ' ' in i:
        index = i.find(' ')
        fillist.append(i[0:index])
    else:
        fillist.append(i[0:index])

print(fillist)