year = int(input('西暦で年を入力して下さい> '))
leap = False # 最初にうるう年ではないと指定。
if year % 400 == 0 :
    leap = True
elif year % 100 == 0 :
    leap = False
elif leap % 4 == 0 :
    leap = True
if leap :
    print(str(year)+'年はうるう年です。')
else :
    print(str(year)+'年はうるう年ではありません。')
