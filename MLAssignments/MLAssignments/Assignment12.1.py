import numpy as np

class Evaluation:
    def __init__(self):
        self.confusionMatrix = np.array([[46,12,2],[9,61,0],[2,3,25]])

    def recall(self):
        count = 0
        rList = []
        for row in self.confusionMatrix:
            print(row)
            TP = row[count]

            d = np.sum(row)
            recallVal = TP / d

            rList.append(recallVal)
            count = count + 1
        return rList

    def precision(self):
        transpose = np.transpose(self.confusionMatrix)
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

    def f1Score(self):
        pList = self.precision()
        rList = self.recall()

        size = pList.__len__()


        for i in range(size):
            f1Val = (2 * pList[i] * rList[i]) / (pList[i] + rList[i])

            print("F1score value for class %s is %s"%(i,f1Val))


e= Evaluation()

print(e.precision())