# 練習12 数の比較 (ex12.py)
# 　３つの数を入力し、数を昇順に並べ替えてから出力するプログラムを作成してください。
# 実行結果
# 数1> 55
# 数2> 25
# 数3> 13
# 13 25 55
# ...

aa = int(input('aa -'))
bb = int(input('bb -' ))
cc = int(input('cc -' ))

if aa > bb:
    tt = aa
    aa = bb
    bb = tt
if aa > cc:
    tt = aa
    aa = cc
    cc = tt

if bb > cc:
    tt = bb
    bb = cc
    cc = tt

print(aa,bb,cc)

