class Time:
    """Class Time with default constructor"""

    def __init__(self, hour=0, minute=0, second=0):
        """Time constructor initializes each data member to zero"""
        self.setTime(hour, minute, second)

    def setTime(self, hour, minute, second):
        """Set values of hour, minute, and second"""
        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)

    def setHour(self, hour):
        """Set hour value"""
        if 0 <= hour < 24:
            self.__hour = hour
        else:
            raise ValueError("Invalid hour value: %d" % hour)

    def setMinute(self, minute):
        """Set minute value"""
        if 0 <= minute < 60:
            self.__minute = minute
        else:
            raise ValueError("Invalid minute value: %d" % minute)

    def setSecond(self, second):
        """Set second value"""
        if 0 <= second < 60:
            self.__second = second
        else:
            raise ValueError("Invalid second value: %d" % second)

    def getHour(self):
        """Get hour value"""
        return self.__hour

    def getMinute(self):
        """Get minute value"""
        return self.__minute

    def getSecond(self):
        """Get second value"""
        return self.__second

    def tick(self):
        if self.__second < 59:
            self.__second += 1
            return f"{self.__hour} : {self.__minute} : {self.__second}"
        elif self.__second == 59 and self.__minute < 59:
            self.__second += 1
            self.__second = 0
            self.__minute += 1
            return f"{self.__hour} : {self.__minute} : {self.__second}"
        elif self.__second == 59 and self.__minute == 59 and self.__hour < 23:
            self.__second += 1
            self.__second = 0
            self.__minute = 0
            self.__hour += 1
            return f"{self.__hour} : {self.__minute} : {self.__second}"
        elif self.__second == 59 and self.__minute == 59 and self.__hour == 23:
            self.__second += 1
            self.__second = 0
            self.__minute = 0
            self.__hour = 0
            return f"{self.__hour} : {self.__minute} : {self.__second}"

    def printMilitary(self):
        """Prints Time object in military format"""
        print(self.__hour, self.__minute, self.__second)

    def printStandard(self):
        """Prints Time object in standard format"""
        standardTime = ""
        if self.__hour == 0 or self.__hour == 12:
            standardTime += "12:"
        else:
            standardTime += "%d:" % (self.__hour % 12)
            standardTime += "%.2d:%.2d" % (self.__minute, self.__second)
        if self.__hour < 12:
            standardTime += " AM"
        else:
            standardTime += " PM"
            return standardTime


time_2 = Time(23, 59, 59)
print(time_2.getHour())
print(time_2.tick())
print(time_2.getHour())
time_3 = Time(22, 34, 59)
print(time_3.tick())
