# 練習13 べき乗計算 (ex13.py)
# 　1以上の整数を入力し、その数までのべき乗を計算するプログラムを作成せよ。
# 実行結果
# 数> 25
# 25! = 15511210043330985984000000
# ...

# n = int(input('数> '))
# fac = 1
# for i in range(1,n+1) :
#     fac *= i
# print(str(n)+'! =',fac,sep=' ')
n = int(input())
fac = 1

for i in range(1,1+n):
    fac*=i

print(fac)
