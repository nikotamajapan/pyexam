# 練習16 データ数のわからない集計 (ex16.py)
# 　数を次々と入力し、負の数が入力されるまで続け、負の数が入力されたら、それまでの数の合計と平均を求めるプログラムを書きなさい。
  
# counter = 0
# gokei = 0
# data = int(input('データ入力(負の数で終了)> '))
# while data >= 0 :
#     counter += 1
#     gokei += data
#     data = int(input('データ入力(負の数で終了)> '))
# heikin = gokei/counter
# print('データ数:',counter,'合計:',gokei,'平均:',heikin)

counter = 0
gokei = 0
data = int(input('data input1 -'))
while data >0:
    counter +=1
    gokei +=data
    data = int(input('data input2-' ))
heikin =  gokei / counter
print('datä', data  ,'total', gokei , 'average',    heikin )

# a=0
# total=0
# b=int(input('1-'))
# while b>=0:
#     a+=1
#     total+=b
#     b=int(input('2-'))
# ave = total/a
# print('datà-', a,'total:',total,'average',ave )
