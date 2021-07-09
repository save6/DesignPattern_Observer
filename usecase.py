import matplotlib as mpl
mpl.use('Agg') # backendsを指定する
import matplotlib.pyplot as plt

'''
入力データ：x座標のデータとy座標のデータが交互に登場して半角スペースで区切って列挙してあるものとする
入力データ例：10 30 20 20 30 40
'''

class Subject():
    def __init__(self):
        self.observers = []
    
    def add(self,observer):
        self.observers.append(observer)
    
    def notify(self):
        for observer in self.observers:
            observer.update()

class GraphModel(Subject):
    def __init__(self):
        super().__init__()
        self.data = []
    
    def sync(self,data):
        self.data = data
        self.notify()

class ChartView():
    def __init__(self,model):
        self.model = model
        self.model.add(self)
    
    def generateGraphData(self):
        self.labels = list(map(self.generateLabel, self.model.data[0::2]))
        self.vals = list(map(int, self.model.data[1::2]))
    
    def generateLabel(self,label):
        return str(label) + "'s"
    
    def update(self):
        self.render()

class Figure():
    def __init__(self,fig,order):
        self.ROW = 3
        self.COLUMN = 1
        self.order = order
        self.fig = fig
    
    def addPlot(self):
        self.fig.add_subplot(self.ROW,self.COLUMN,self.order)

class LineChartView(ChartView,Figure):
    def __init__(self, model, fig, order):
        ChartView.__init__(self,model)
        Figure.__init__(self,fig,order)
    
    def render(self):
        self.generateGraphData()
        self.addPlot()
        plt.plot(self.labels, self.vals)

class BarChartView(ChartView,Figure):
    def __init__(self, model, fig, order):
        ChartView.__init__(self,model)
        Figure.__init__(self,fig,order)
    
    def render(self):
        self.generateGraphData()
        self.addPlot()
        plt.bar(self.labels, self.vals)

class PieChartView(ChartView,Figure):
    def __init__(self, model, fig, order):
        ChartView.__init__(self,model)
        Figure.__init__(self,fig,order)
    
    def render(self):
        self.generateGraphData()
        self.addPlot()
        plt.pie(self.vals,labels=self.labels)
    
if __name__=='__main__':
    
    MODEL = GraphModel()
    fig = plt.figure()
    PieChartView(MODEL,fig,order=1)
    LineChartView(MODEL,fig,order=2)
    BarChartView(MODEL,fig,order=3)

    MODEL.sync(input().split())
    
    plt.savefig("hoge.png") 