import datetime

# Min ~ Max year. (Const)
print("Min year : " + str(datetime.MINYEAR))
print("Max year : " + str(datetime.MAXYEAR) + "\n")

# Timedelta.
setTime = datetime.timedelta(days=3, seconds=10, microseconds=500, milliseconds=110, minutes=55, hours=7)
print(setTime)

# Today. (yyyy-mm-dd)
print("[Today is...]")
print("%s\n" % (datetime.date.today()))

print("[Another Date...]")
print("%s" % (datetime.date(2025, 3, 22)))

anotherDate = datetime.date.fromisoformat('2020-05-22')
print("%d %d %d\n" % (anotherDate.year, anotherDate.month, anotherDate.day))

print("[Replace Test]")
anotherDate = anotherDate.replace(month=11)
print(anotherDate)

print("[Weekday Test]")
print("%s %s\n" % (anotherDate.weekday(), anotherDate.isoweekday()))
# weekday() : 0 ~ 6
# isoweekday() : 1 ~ 7


today = datetime.date.today()
todayWeekday = today.weekday()

if todayWeekday == 0 : print("Monday")
elif todayWeekday == 1 : print("Tuseday")
elif todayWeekday == 2 : print("Wednesday")
elif todayWeekday == 3 : print("Thursday")
elif todayWeekday == 4 : print("Friday")
elif todayWeekday == 5 : print("Saturday")
elif todayWeekday == 6 : print("Sunday")
else : print("???")