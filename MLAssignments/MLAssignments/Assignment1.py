import pandas as pd
import numpy as np
from scipy import stats
from datetime import date
import math as m

# x = [81,6,30,48,48,3,31,4,26,28,14,1]
#
# y= [23,1,33,23,48,53,30,24,39,1]
#
# z = [120,123,130,48,248,137,137,94,126,98,64,137]
#
# a = [12,13,30,48,47,73,31,94,26,18,24,20]
#
# b = [22,31,21,4,17,17,31,34,21,12.5,24.7,21]
#
# mean = np.mean(x)
# print(mean)
#
# median =np.median(y)
# print(median)
#
# mode = stats.mode(z)
# print(mode)
#
# varience = np.var(a)
# print(varience)
#
# sd = np.std(b)
# print(sd)

class User:
    firstname = ''
    dateOfBirth = ''

    def __init__(self, firstname, dateOfBirth):
        self.firstname = firstname
        self.dateOfBirth = dateOfBirth


    def setFirstname(self, name):
        self.firstname = name

    def getFirstname(self):
        return self.firstname

    def getAge(self,dateOfBirth):
        today = date.today()
        return today.year - dateOfBirth.year - ((today.month, today.day) < (dateOfBirth.month, dateOfBirth.day))




test = User('Sanjeev','1997-06-12')

test.setFirstname('Sameep')

test.getAge(date(1997,6,12))


print(test.getFirstname())
print(test.getAge(date(1997,6,12)))

