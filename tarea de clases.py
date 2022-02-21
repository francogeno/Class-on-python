# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 20:42:55 2021

@author: Lenovo
"""

#TAREA DE CLASES

#5
months = ["January", "February", "March","April","May",'June', 'July','August','September', 'October', 'November', 'December']



#2
def addleftzero(n, m=2):
    """
    n = numero entero 
    m = cantidad de cifras que debe tener
    returns: numero con la cant de 0 necesarios
    """
    for i in range(m-1,0,-1):
        if n < 10**(m-i):
            return "0"* i + str(n)
    return n


#1
class Date():
    def __init__(self, day=1, month=1, year=1):
        self.day = day
        self.month = month
        self.year = year 
   #2     
    def __str__(self):
        return "{} / {} / {}".format(addleftzero(self.day), addleftzero(self.month), addleftzero(self.year, 4))
    def isLeap(self):  #3
        if self.year % 4 == 0:
            return True
        else: return False

    def totalMonthDays(self): #4
        if self.month in [1,3,5,7,8,10,12]:
            return 31
        if self.month == 2:
            if self.isLeap() == True:
                return 29
            else: return 28
        else: return 30
    def validDate(self):
        if self.year < 0:
            return False
        elif self.month <= 0 or self.month >12:
           return False
        elif self.day <= 0 or self.day > self.totalMonthDays():
           return False
        else: return True
        
    def __init__(self, day=1, month=1, year=1):
        self.day = day
        self.month = month
        self.year = year
        if self.validDate() == False:
            raise ValueError ("The date is not valid")
    
    @property
    def monthName(self):
        for i in range(1,12):
            if self.month == i + 1:
                return months[i]
              #6       
    @staticmethod
    def areEqual(d1, d2):
        if d1.year == d2.year and d1.month == d2.month and d1.day == d2.day:
            return True
        return False

    @staticmethod
    def isLater(d1, d2):
        if d1.year > d2.year:
            return True
        elif d1.year == d2.year:
            if d1.month > d2.month:
                return True
            if d1.month == d2.month:
                if d1.day > d2.day:
                    return True
        return False
    @staticmethod
    def isPrevious(d1, d2):
        if not Date.isLater(d1,d2) and not Date.areEqual(d1,d2):
            return True
        return False
            #7
    @classmethod
    def firstDayOfTheYear(cls, year):
        if year >0:
            return cls(1,1,year)
        print("The year you have introduced is not valid")
    @classmethod
    def lastDayOfTheYear(cls,year):    
        if year >0:
            return cls(31,12,year)
        print("The year you have introduced is not valid")
        
    def plusDay(self):
        if Date.areEqual(self, Date.lastDayOfTheYear(self.year)):
            return Date(year=self.year+1)
        elif self.day == self.totalMonthDays():
            return Date(1,self.month+1,self.year)
        else: return Date(self.day+1, self.month, self.year)
        
    def minusDay(self):
        if Date.areEqual(self,Date.firstDayOfTheYear(self.year)):
            return Date.lastDayOfTheYear(self.year-1)
        elif self.day == 1:
            self.day = self.totalMonthDays()
            self.month -=1
        else: self.day -=1
        
    
    #8
    @classmethod
    def copy(cls,d):
        return cls(d.day, d.month,d.year)
    @staticmethod
    def difference(d1,d2):
        if Date.areEqual(d1, d2):
            return 0
        elif Date.isLater(d1,d2) == True:
            count = 0
            d2_copy = Date.copy(d2)
            while not Date.areEqual(d1, d2_copy):
                count +=1
                d2_copy.plusDay()
            return count
            
    @classmethod
    def randomDate(cls):
        import random
        month = random.randint(1,12)
        year = random.randint(0,3000)
        random_date = cls(1,month, year)
        random_date.day = random.randint(1, random_date.totalMonthDays())
        return random_date
    
    @classmethod
    def toDate(cls, d):
        dateList = d.split(" ")
        #Dia:
        day = int(dateList[0])
        #Mes
        if dateList[1] in months:
            month = months.index(dateList[1]) + 1
        else:
            print("Yo have introduced an invalid month ")
            return "NULL"
        #year
        year = int(dateList[2])
        return cls(day,month,year)
    

    
date1 = "19 May 1995"
date2 = Date.toDate(date1)
print(date2)

