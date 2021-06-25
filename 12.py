# 練習12 数の比較 (ex12.py)
# 　３つの数を入力し、数を昇順に並べ替えてから出力するプログラムを作成してください。
# 実行結果
# 数1> 55
# 数2> 25
# 数3> 13
# 13 25 55

aa = int(input('aa -'))
bb = int(input('bb -'))
cc = int(input('cc -'))

if aa>bb:
    temp = aa
    aa = bb
    bb = temp

if aa>cc:
    temp = aa
    aa = cc
    cc = temp

if bb>cc:
    temp = bb
    bb = cc
    cc = temp

print(aa)
print(bb)
print(cc)
