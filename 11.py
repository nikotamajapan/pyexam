# 練習11 ジャンケンするプログラム (ex11.py)
# 　計算機とジャンケンをするプログラムを書きましょう。グー、チョキ、パーをそれぞれ0,1,2の整数で表すとします。あなたの出す手を整数で入力し、勝負するようにします。
# コンピュータの出す手は乱数（同じ確率ででたらめに数を自動的に生成する仕組み）を使って作り出します。具体的には、random.randint(最小値, 最大値)という式を使うと自動的に最小値から最大値までのでたらめな整数を作ってくれます。(プログラムの始めに、'import random'の宣言が必要)
#  comp=random.randint(0,2)
# こうすると、このcompに0か1か2の整数がでたらめに代入されます。入力したあなたの手とこのcompを比較して、ジャンケンの勝負を判定するプログラムを作りなさい。
# 実行結果
# ジャンケンポン！
# あなたは？(0:グー, 1:チョキ, 2:パー)> 0
# わたしはチョキ。あなたはグー。あなたの勝ちです。
# ...

import random

comp = random. randint(0,2)
print('ジャンケンポン！')
me=int(input('あなたは？(0:グー, 1:チョキ, 2:パー)> - '))
if comp == 0:
    print('comp - gu')
elif comp == 1:
    print('comp - choki')
else:
    print('comp - paa')


print('jibun - ')
if me == 0:
    print('gu')
    if comp == me:
        print('aiko')
    elif comp == 1:
        print('kachi')
    else:
        print('make')
        

if me == 1:
    print('choki')
    if comp == me:
        print('aiko')
    elif comp == 2:
        print('kachi')
    else:
        print('make')
        

if me == 2:
    print('paa')
    if comp == me:
        print('aiko')
    elif comp == 0:
        print('kachi')
    else:
        print('make')
        
    
