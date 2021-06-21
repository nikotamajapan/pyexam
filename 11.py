# 練習11 ジャンケンするプログラム (ex11.py)
# 　計算機とジャンケンをするプログラムを書きましょう。グー、チョキ、パーをそれぞれ0,1,2の整数で表すとします。あなたの出す手を整数で入力し、勝負するようにします。コンピュータの出す手は乱数（同じ確率ででたらめに数を自動的に生成する仕組み）を使って作り出します。具体的には、random.randint(最小値, 最大値)という式を使うと自動的に最小値から最大値までのでたらめな整数を作ってくれます。(プログラムの始めに、'import random'の宣言が必要)
#  comp=random.randint(0,2)
# こうすると、このcompに0か1か2の整数がでたらめに代入されます。入力したあなたの手とこのcompを比較して、ジャンケンの勝負を判定するプログラムを作りなさい。
# 実行結果
# ジャンケンポン！
# あなたは？(0:グー, 1:チョキ, 2:パー)> 0
# わたしはチョキ。あなたはグー。あなたの勝ちです。
# ...

import random

aa = random.randint(0, 2)
if aa == 0:
    print('0:グー')
if aa == 1:
    print('1:チョキ')
if aa == 2:
    print('2:パー')
    
bb=int(input('あなたは？(0:グー, 1:チョキ, 2:パー)> '))
print(bb)

if aa == 0:
    if bb == aa:
        print('aiko')
    elif bb == 1:
        print('lose')
    else:
        print('win')

if aa == 1:
    if bb == aa:
        print('aiko')
    elif bb == 2:
        print('lose')
    else:
        print('win')

if aa == 2:
    if bb == aa:
        print('aiko')
    elif bb == 0:
        print('lose')
    else:
        print('win')

