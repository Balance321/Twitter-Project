from datetime import datetime

currentYear = datetime.now().year

today = datetime.today()
week_num = today.isocalendar()[1]
currWeek = week_num % 13

currentMonth = datetime.now().month
currSeason = ''
if currentMonth <= 3:
    currSeason = 'winter'
elif currentMonth <= 6: 
    currSeason = 'spring'
elif currentMonth <= 9: 
    currSeason = 'summer'
else:
    currSeason = 'fall'

