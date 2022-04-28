import pandas as pd
import math as m

df = pd.read_csv('train.csv')
df = df.dropna()

dfTest = pd.read_csv('test.csv')
dfTest = dfTest.dropna()

meanYTest = dfTest['y'].mean()
print(df)

meanX = df['x'].mean()
print('Mean of X:',meanX)
meanY = df['y'].mean()
print('Mean of Y:',meanY)

#calculating slope 'm'
part1 = []
part2 = []
part3 = []

for index, row in df.iterrows():
    differenceX = row['x'] - meanX
    differenceY = row['y'] - meanY

    part1.append(differenceX)
    part2.append(differenceY)
    part3.append(m.pow(differenceX,2))

df.insert(2,"part1",part1,True)
df.insert(3,"part2",part2,True)
df.insert(4,"part3",part3,True)

sumXY = 0
sumXSquared = 0

for index, row in df.iterrows():
    sumXY = sumXY + row['part1']*row['part2']
    sumXSquared = sumXSquared + row['part3']

slope = sumXY / sumXSquared

print("Slope(m):",slope)

#y-intercept

yIntercept = meanY - (slope * meanX)
print("y-intercept(c):",yIntercept)

#----------------------For Test Data---------------------
#iterating over x with m and c obtained above on the test data to get predicted Y
predictedY = []
for index, row in dfTest.iterrows():
    y = slope * row['x'] + yIntercept
    predictedY.append(y)

dfTest.insert(2,"predictedY",predictedY,True)
print(dfTest)

#evaluating the model's performance using RMSE
diffPA = 0
for index, row in dfTest.iterrows():
    diffPA = diffPA + m.pow((row['predictedY'] - row['y']),2)

rmse = m.sqrt(diffPA/dfTest['x'].count())
print("RMSE of Test data:",rmse)
print("Normalised RMSE of Test data:",(rmse/meanYTest))


#---------------------For Training Data-------------------
#iterating over x with m and c obtained above on the training data to get predicted Y
predictedY1 = []
for index, row in df.iterrows():
    y = slope * row['x'] + yIntercept
    predictedY1.append(y)

df.insert(5,"predictedY",predictedY1,True)

#evaluating the model's performance using RMSE
diffPA = 0
for index, row in df.iterrows():
    diffPA = diffPA + m.pow((row['predictedY'] - row['y']),2)

rmse = m.sqrt(diffPA/df['x'].count())
print("RMSE of Training data:",rmse)
print("Normalised RMSE of Training data:",(rmse/meanY))