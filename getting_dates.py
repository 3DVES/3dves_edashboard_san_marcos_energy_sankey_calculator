from datetime import datetime, timedelta

CurrentDateTime = datetime.now()
CurrentMonth = CurrentDateTime.month
if CurrentMonth < 10:
    CurrentMonth = "0" + str(CurrentMonth)
CurrentYear = str(format(CurrentDateTime.year))

CurrentDay = CurrentDateTime.day
if CurrentDay < 10:
    CurrentDay = "0" + str(CurrentDay)

LastMonth = CurrentDateTime - timedelta(days=30)
YearOfLastMonth = str(format(LastMonth.year))
LastMonthFormatted = LastMonth.month
ThirtyDaysAgo = LastMonth.day
if LastMonthFormatted < 10:
    LastMonthFormatted = "0" + str(LastMonthFormatted)
if ThirtyDaysAgo < 10:
    ThirtyDaysAgo = "0" + str(ThirtyDaysAgo)

LastYear = CurrentDateTime - timedelta(days=365)
PreviousYear = str(format(LastYear.year))
MonthOfLastYear = LastYear.month
DayOfLastyear = LastYear.day
if MonthOfLastYear < 10:
    MonthOfLastYear = "0" + str(MonthOfLastYear)
if DayOfLastyear < 10:
    DayOfLastyear = "0" + str(DayOfLastyear)


def CurrentDate():
    CurrentDate = CurrentYear + "-" + str(CurrentMonth) + "-" + str(CurrentDay)
    return CurrentDate


def FirstOfThisMonth():
    FirstOfThisMonth = CurrentYear + "-" + str(CurrentMonth) + "-01"
    return FirstOfThisMonth


def LastMonthDate():
    LastMonthDate = (
        YearOfLastMonth + "-" + str(LastMonthFormatted) + "-" + str(ThirtyDaysAgo)
    )
    return LastMonthDate


def AYearAgo():
    YearAgo = PreviousYear + "-" + str(MonthOfLastYear) + "-" + str(DayOfLastyear)
    return AYearAgo
