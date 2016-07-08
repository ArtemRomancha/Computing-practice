# ­*­ coding: utf­8 ­*­
#import Simulation
import tkinter
import math
#
def CreateGraph(DataSet,duration):
    tk=tkinter.Tk()
    tk.title("Graph")
    canvas=tkinter.Canvas(tk)
    canvas["height"]=1000
    canvas["width"]=2700
    canvas["background"]="#eeeeff"
    canvas["borderwidth"]=2
    canvas.pack()
    # рисуем 1-ый график
    points1=[]
    ay=300
    y0=300
    x0=40
    x1=x0+45*duration
    dx=45
    j=0
    # цикл для определения всех точек 1-ого графика
    for n in range(x0,x1,dx):
        if DataSet[j][3]>=0:
            pp=(n,310-3*DataSet[j][3])
        else:
            pp=(n,-3*DataSet[j][3]+310)
        canvas.create_text(x0+45*j,640,text=DataSet[j][2],font= "Arial 6") #подписываем даты на графике DataSet[j][2]
        j=j+1
        points1.append(pp)
        #выводим график
    canvas.create_line(points1,fill="blue",smooth=1)
    # рисуем 2-ой график
    j=0
    points2=[]
    # цикл для определения всех точек 2-ого графика
    for n in range(x0,x1,dx):
        if DataSet[j][4]>=0:
            pp=(n,310-3*DataSet[j][4])
        else:
            pp=(n,-3*DataSet[j][4]+310)
        j=j+1
        points2.append(pp)
    # выводим график
    canvas.create_line(points2,fill="green",smooth=1)
    # рисуем 3-ий график
    j=0
    points3=[]
    # цикл для определения всех точек 2-ого графика
    for n in range(x0,x1,dx):
        if DataSet[j][5]>=0:
            pp=(n,310-3*DataSet[j][5])
        else:
            pp=(n,-3*DataSet[j][5]+310)
        j=j+1
        points3.append(pp)
    # выводим график
    canvas.create_line(points3,fill="red",smooth=1)
    # рисуем координатные оси
    y_axe=[]
    yy=(x0,0)
    y_axe.append(yy)
    yy=(x0,y0+ay+20)
    y_axe.append(yy)
    canvas.create_line(y_axe,fill="black",width=2)
    #
    x_axe=[]
    xx=(x0,y0+10)
    x_axe.append(xx)
    xx=(x1,y0+10)
    x_axe.append(xx)
    canvas.create_line(x_axe,fill="black",width=2)
    #
    y1=10
    y2=610
    dx=30
    j=1
    i=0
    for n in range(y1,y2,dx):
        if n<310:
            canvas.create_text(25,n,fill="black",text=(10-i)*10)
            i=i+1
        if n==310:
            canvas.create_text(25,n,fill="black",text=0)
        if n>310:
            canvas.create_text(25,n,fill="black",text=-j*10)
            j=j+1
    canvas.create_text(25,610,fill="black",text=-100)
    #
    canvas.create_text(300,670,fill="blue",text="- физическое состояние")
    canvas.create_text(300,680,fill="green",text="- эмоциональное состояние")
    canvas.create_text(300,690,fill="red",text="- интеллектуальное состояние")
    #
    tk.mainloop()