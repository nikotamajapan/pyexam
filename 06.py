# 練習06 金種計算 (ex06.py)
# 　金額を入力するとその金額を出来るだけ少ない枚数の貨幣を使って支払えるように貨幣の枚数を数えるプログラムを書きなさい。貨幣は、{１万円札、五千円札、千円札、五百円玉、百円玉、五十円玉、十円玉、五円玉、一円玉}とする（余り使わないので２千円札は除く）。
# 実行結果
# 金額(円)> 48767
# 金額: 48767 円
# 一万円札= 4 枚
# 五千円札= 1 枚
# 千円札　= 3 枚
# 五百円玉= 1 枚
# 百円玉　= 2 枚
# 五十円玉= 1 枚
# 十円玉　= 1 枚
# 五円玉　= 1 枚
# 一円玉　= 2 枚
# ...

kane = int(input('kane - '))
a = kane

man = a // 10 ** 4
a = a % 10 ** 4
print('man - ', man)

gosen = a // (5 * 10 ** 3 )
a = a % (5 *10 ** 3 )
print('gosen - ', gosen)

sen = a // 10 ** 3
a = a % 10 ** 3
print('sen - ',sen)

gohyaku = a // (5 * 10 ** 2 )
a = a % (5 *10 ** 2 )
print('gohyaku - ', gohyaku)

hyaku = a // 10 ** 2
a = a % 10 ** 2
print('hyaku - ', hyaku)

gojyu = a // (5 * 10 ** 1 )
a = a % (5 *10 ** 1 )
print('gojyu - ', gojyu)

jyu = a // 10 ** 1
a = a % 10 ** 1
print('jyu - ', jyu)

go = a // (5 * 10 ** 1 )
a = a % (5 *10 ** 1 )
print('go - ', go)

ichi = a // 10 ** 1
a = a % 10 ** 1
print('ichi - ', ichi)

