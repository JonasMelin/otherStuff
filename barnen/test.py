import datetime
import dateutil.parser

def getYearMonthFromCollectionName(name):

    if "20" not in name:
        raise ValueError("collection has wrong naming convention. 20 missing in it so you are running in the wrong century")

    datePart = name.split("20")[1]
    if "_w" in datePart:
        datePart = datePart.split("_w")[0]
    yearPart = datePart[:2]
    monthPart = datePart[2:]
    return int(yearPart), int(monthPart)


def isCollectionInTimeRange(fromTime, toTime, collectionName):
    collectionY, collectionM = getYearMonthFromCollectionName(collectionName)
    fromTimeAsDate = dateutil.parser.parse(fromTime)
    toTimeAsDate = dateutil.parser.parse(toTime)
    fromTimeY = fromTimeAsDate.year - 2000
    toTimeY = toTimeAsDate.year - 2000
    fromTimeM = fromTimeAsDate.month
    toTimeM = toTimeAsDate.month


    if (collectionY >= fromTimeY and collectionY <= toTimeY) and \
            (collectionM >= fromTimeM and collectionM <= toTimeM):
        return True
    return False


result = isCollectionInTimeRange("2019-03-16T23:10:35.696839", "2019-04-16T23:10:35.696839", "blabar20193")

if result:
    print("IN RANGE")
else:
    print("NOT IN RANGE")
