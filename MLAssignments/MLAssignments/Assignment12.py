
import numpy as np

confusionMatrix = np.array([[46,12,2],[9,61,0],[2,3,25]])

def recall(matrix):
    count = 0
    rList = []
    for row in matrix:
        print(row)
        TP = row[count]

        d = np.sum(row)
        recallVal = TP / d

        rList.append(recallVal)
        count = count + 1
    return rList

def precision(matrix):
    transpose = np.transpose(matrix)
    count = 0
    pList = []
    TPlist = []
    FPList = []
    for row in transpose:
        TP = row[count]
        print(TP)
        listRow = list(row)
        print(listRow)

        listRow.remove(int(TP))
        print(listRow)


        d = np.sum(row)
        precisionVal = TP / d

        pList.append(precisionVal)
        TPlist.append(TP)
        FPList.append(listRow)

        count = count + 1
    print(FPList)
    print(TPlist)
    return pList

def f1Score(matrix):
    pList = precision(matrix)
    rList = recall(matrix)

    size = pList.__len__()


    for i in range(size):
        f1Val = (2 * pList[i] * rList[i]) / (pList[i] + rList[i])

        print("F1score value for class %s is %s"%(i,f1Val))

def macroAvgPrecision(matrix):
    pList = precision(matrix)
    mAP = sum(pList)/len(pList)

    print(mAP)

def microAvgPrecision(matrix):

    #calculating precision of each and identifying TP and FP
    transpose = np.transpose(matrix)
    count = 0
    pList = []
    TPlist = []
    FPList = []
    for row in transpose:
        #TP value
        TP = row[count]

        listRow = list(row)

        #list of FP values
        listRow.remove(int(TP))

        #caculating precision
        d = np.sum(row)
        precisionVal = TP / d

        pList.append(precisionVal)
        TPlist.append(TP)
        FPList.append(listRow)

        count = count + 1

    FPsum = 0
    for row in FPList:
        FPsum = FPsum + sum(row)

    #Micro average precision
    mAP = sum(TPlist) / (sum(TPlist) + FPsum)
    print(mAP)

    return mAP


microAvgPrecision(confusionMatrix)