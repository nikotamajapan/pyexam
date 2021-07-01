# 練習15 棒グラフ (ex15.py)
# 　数字を入力して、1からその数までの棒グラフを順に表示するプログラムを書きなさい。
# 実行結果
# 数> 8
# 1:■
# 2:■■
# 3:■■■
# 4:■■■■
# 5:■■■■■
# 6:■■■■■■
# 7:■■■■■■■
# 8:■■■■■■■■
# ...

# n = int(input('数> '))
# for j in range(n+1) :
#     print(str(j)+':',end='') # 改行しない出力
#     for i in range(0,j) :
#         print('■',end='')
#     print() # 改行だけ出力


# a = int(input())
# for b in range(1,1+a):
#     print(str(b)+':',end='')
#     for c in range(0,b):
#         print('*',end='')
#     print()


a=int(input())
for b in range(1,a+1):
    print(b,':',end='')
    for c in range(0,b):
        print('*',end='')
    print()
