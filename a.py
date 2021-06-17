year = int(input('年> '))
month = int(input('月> '))
day = int(input('日> '))
datestr = str(year)+'年'+str(month)+'月'+str(day)+'日'




if month == 1 or month == 2 :
    year = year - 1
    month = month + 12





weekday = (year + (year // 4) - (year // 100) + \
  (year // 400) + ((13*month+8) // 5) + day) % 7
if weekday == 0 :
    weekstr = '日曜日'
elif weekday == 1 :
    weekstr = '月曜日'
elif weekday == 2 :
    weekstr = '火曜日'
elif weekday == 3 :
    weekstr = '水曜日'
elif weekday == 4 :
    weekstr = '木曜日'
elif weekday == 5 :
    weekstr = '金曜日'
elif weekday == 6 :
    weekstr = '土曜日'
print(datestr+'は'+weekstr+'です。')
