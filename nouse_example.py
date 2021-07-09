import matplotlib as mpl
mpl.use('Agg') # backendsを指定する
import matplotlib.pyplot as plt

'''
入力データ：x座標のデータとy座標のデータが交互に登場して半角スペースで区切って列挙してあるものとする
入力データ例：10 30 20 20 30 40
'''

class GraphData():
    def __init__(self,data):
        self.__x = data[0::2]
        self.__y = data[1::2]
    
    def getX(self):
        return list(map(self.createXLabel, self.__x))
    
    def getY(self):
        return list(map(int, self.__y))
    
    def createXLabel(self,x):
        return str(x) + "'s"

def rendering(data):
    ROW = 3
    COLUMN = 1
    
    fig = plt.figure()

    ay1 = fig.add_subplot(ROW, COLUMN, 1)
    ay1 = plt.pie(data.getY(),labels=data.getX())

    ay2 = fig.add_subplot(ROW, COLUMN, 2)
    ay2 = plt.plot(data.getX(), data.getY())

    ay3 = fig.add_subplot(ROW, COLUMN, 3)
    ay3 = plt.bar(data.getX(), data.getY())

if __name__=='__main__':

    DATA = GraphData(input().split())
    
    rendering(DATA)
    
    plt.savefig("hoge.png") 