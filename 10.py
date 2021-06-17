# 練習10 あなたの誕生日は何曜日？ (ex10.py)
# 　Zëllerの公式(1887)という公式を使うと、1582年10月15日以降の日付から曜日を計算することができます。整数(int)として年をyear、月をmonth、日をdayとした時、曜日(weakday)は
#  weakday = (year + (year // 4) - (year // 100) + (year // 400) + ((13*month+8) // 5) + day) % 7
# という式で計算できます。曜日は整数として0が日曜、1が月曜、...、6が土曜となります。
# 但し、1月と2月はそれぞれ前の年の13月、14月として計算する必要があります。例えば、2000年1月というのは上の計算式では、1999年13月として計算しなければなりません。
# 自分の誕生日を入力して、生まれた日が何曜日かを調べなさい。
# 実行結果
# 年> 1996
# 月> 10
# 日> 4
# 1996年10月4日は金曜日です。
 
year = int(input('year'))
month = int(input('month'))
day = int(input('day'))
datestr = str(year)+'年'+str(month)+'月'+str(day)+'日'

if month == 1 or month == 2:
    year -= 1
    month +=12

weakday = (year + (year // 4) - (year // 100) + (year // 400) + ((13 * month + 8) // 5) + day) % 7

if weakday == 0 :
    weekstr = '日曜日'
elif weakday == 1 :
    weekstr = '月曜日'
elif weakday == 2 :
    weekstr = '火曜日'
elif weakday == 3 :
    weekstr = '水曜日'
elif weakday == 4 :
    weekstr = '木曜日'
elif weakday == 5 :
    weekstr = '金曜日'
elif weakday == 6 :
    weekstr = '土曜日'

print(datestr,'=',weekstr)