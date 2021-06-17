# 練習08 整数曜日変換 (ex08.py)
# 　0から6までの整数を入力して、それぞれ、0ならば「日曜」、1ならば「月曜」、...と結果を返すプログラムを書きなさい。但し、0〜6の数以外の数値が入力された場合には、「0から6までの数を入力してください」とメッセージを返すようにしなさい。
# 実行結果
# 数(0-6)> 5
# 金曜日
# ...

a = int(input('0-6 ? '))

if a == 0:
    print('sun')
elif a == 1:
    print('mon')
elif a == 2:
    print('tue')
elif a == 3:
    print('wed')
elif a == 4:
    print('thu')
elif a == 5:
    print('fri')
elif a == 6:
    print('sat')
else:
    print('0-6 only ')