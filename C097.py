user_input = input()  # ユーザーからの入力を受け取る

# 入力が整数であるか確認
try:
    lists = list(map(int, user_input.split()))
except ValueError:
    print("無効な入力です。整数を入力してください。")
n = lists[0] 
kotae = []

x = lists[1]
y = lists[2]


def keisanki(i, x, y):
    if i % x == 0 and i % y == 0:
        kotae = 'AB'
    elif i % y == 0:
        kotae = 'B'
    elif i % x == 0:
        kotae = 'A'
    else:
        kotae = 'N'
    return kotae


for i in range(1, n+1):
    if i < x and i < y:
        print('N')
    else:
        print(keisanki(i, x, y))
    i += 1
