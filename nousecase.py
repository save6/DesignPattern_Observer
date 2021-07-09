from abc import ABCMeta, abstractmethod
import matplotlib as mpl
mpl.use('Agg') # backendsを指定する
import matplotlib.pyplot as plt

'''
入力データ：x座標のデータとy座標のデータが交互に登場して半角スペースで区切って列挙してあるものとする
入力データ例：10 30 20 20 30 40
'''

class ChartView(metaclass=ABCMeta):
    def __init__(self,data):
        self.__labels = data[0::2]
        self.__vals = data[1::2]
    
    def getLabels(self):
        return list(map(self.generateLabel, self.__labels))
    
    def getVals(self):
        return list(map(int, self.__vals))
    
    def generateLabel(self,label):
        return str(label) + "'s"
    
    @abstractmethod
    def render(self):
        pass

class LineChartView(ChartView):
    def __init__(self, data):
        super().__init__(data)
    
    def render(self):
        plt.plot(self.getLabels(), self.getVals())

class BarChartView(ChartView):
    def __init__(self, data):
        super().__init__(data)
    
    def render(self):
        plt.bar(self.getLabels(), self.getVals())

class PieChartView(ChartView):
    def __init__(self, data):
        super().__init__(data)
    
    def render(self):
        plt.pie(self.getVals(),labels=self.getLabels())

def rendering(data):
    ROW = 3
    COLUMN = 1
    
    fig = plt.figure()

    fig.add_subplot(ROW, COLUMN, 1)
    PieChartView(data).render()
    
    fig.add_subplot(ROW, COLUMN, 2)
    LineChartView(data).render()

    fig.add_subplot(ROW, COLUMN, 3)
    BarChartView(data).render()
    
if __name__=='__main__':
    
    rendering(input().split())
    
    plt.savefig("hoge.png") 