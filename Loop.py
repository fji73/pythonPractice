# for 変数 in range(繰り返す回数):
#    繰返し中に実行する処理

for i in range(5):
    print(i)
    if i == 3:
        break


# continue : 条件に当てはまった場合処理をスキップする
for i in range(5):
    if i == 3:
        continue
    print(i)


# ネスト
for i in range(3):
    for j in range(3):
        print(i, j , sep = "-")


arr = [2, 4, 6, 8, 10]
sum = 0
for i in arr:
    sum += i
    print(sum)
print(sum)
