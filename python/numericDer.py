import math
import sympy as sp
from tabulate import tabulate

class NumericDerivation:
    def __init__(self, h, x, y):
        self.h = h
        self.x = x
        self.y = y
    

    def __threePointsStart(self, y, h, index):
        return 1/(2*h)*(4*y[index+1] -3*y[index] -y[index+2])
    
    def __threePointsCentral(self, y, h, index):
        return 1/(2*h)*(y[index + 1] - y[index-1])
    
    def __threePointsEnd(self, y, h, index):
        isThereNeg = False
        for i in range(0, 3):
            if index - i < 0:
                isThereNeg = True
        return "valor incalculable bajo la dimension del arreglo" if isThereNeg else -1/(2*h)*(4*y[index-1] -3*y[index] -y[index-2])

    
    def getThreePoints(self):
        heads = ["x", "f(x)", "f'(x)"]
        tableData = []
        try:                
            for i in range(0, len(self.x)):
                if i == 0:
                    try:
                        tableData.append([self.x[i], self.y[i], self.__threePointsStart(self.y, self.h, i)])
                    except:
                        tableData.append([self.x[i], self.y[i], "valor incalculable bajo la dimension del arreglo"])

                elif i == len(self.x)-1:
                    try:
                        tableData.append([self.x[i], self.y[i], self.__threePointsEnd(self.y, self.h, i)])
                    except:
                        tableData.append([self.x[i], self.y[i], "valor incalculable bajo la dimension del arreglo"])

                else:
                    try:
                        tableData.append([self.x[i], self.y[i], self.__threePointsCentral(self.y, self.h, i)])
                    except:
                        tableData.append([self.x[i], self.y[i], "valor incalculable bajo la dimension del arreglo"])

            print(tabulate( tableData, headers=heads,  tablefmt="grid"))
        except:
            print("ha ocurrido un error")

    def __fivePointsStart(self, h, y, index):
        return 1/(12*h)*(-25*y[index] + 48*y[index+1] -36*y[index+2] +16*y[index+3] - 3*y[index+4])
    
    def __fivePointsEnd(self, h, y, index):
        thereIsNeg = False
        for i in range(0, 5): 
            if index - i < 0: 
                thereIsNeg = True
        return "valor incalculable bajo la dimension del arreglo" if thereIsNeg else  -1/(12*h)*(-25*y[index] + 48*y[index-1] -36*y[index-2] +16*y[index-3] - 3*y[index-4])
    
    def __fivePointsCentral(self,h, y, index):
        return 1/(12*h)*(y[index - 2] - 8*y[index - 1] + 8*y[index + 1] - y[index + 2])
    
    def getFivePoints(self):
        heads = ["x", "f(x)", "f'(x)"]
        tableData = []
        try:
            for i in range(0, len(self.x)):
                if i == 0 or i == 1:
                    try:
                        tableData.append([self.x[i], self.y[i], self.__fivePointsStart(self.h, self.y, i)])
                    except:
                        tableData.append([self.x[i], self.y[i], "valor incalculable bajo la dimension del arreglo"])
                elif   i == (len(self.x) - 1) or i == (len(self.x) - 2):
                    try:
                        print(i, self.x[i - 4])
                        tableData.append([self.x[i], self.y[i], self.__fivePointsEnd(self.h, self.y, i)])
                    except:
                        tableData.append([self.x[i], self.y[i], "valor incalculable bajo la dimension del arreglo"])

                else:
                    try:
                        tableData.append([self.x[i], self.y[i], self.__fivePointsCentral(self.h, self.y, i)])
                    except:
                        tableData.append([self.x[i], self.y[i], "valor incalculable bajo la dimension del arreglo"])

            print(tabulate(tableData, headers=heads, tablefmt="grid"))               
        except:
            print("ha ocurrido un error")

        