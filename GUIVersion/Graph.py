import tkinter
import math
from datetime import datetime, timedelta
#
def CreateGraph(DataSet,duration):
	tk=tkinter.Tk()
	tk.title("Graph")
    
	screen_width = tk.winfo_screenwidth()
	screen_height = tk.winfo_screenheight()
    
	canvas=tkinter.Canvas(tk)
	canvas["height"] = screen_height
	canvas["width"] = screen_width
	canvas["background"] = "#eeeeff"
	canvas["borderwidth"] = 2
	canvas.pack()
        
	y0 = int((screen_height - 200) / 2)
	dy = int(y0 / 100)
	x0 = 40
	x1 = screen_width
	dx = int((x1 - x0) / duration)
	j = 0	
    # цикл для определения всех точек 1-ого графика
	points1=[]    
	points2=[]
	points3=[]
    
	for n in range(x0,x1,dx):
		pp=(n, y0 - dy * DataSet[j][3])
		points1.append(pp)
        
		pp=(n, y0 - dy * DataSet[j][4]) 
		points2.append(pp)  
        
		pp=(n, y0 - dy * DataSet[j][5])    
		points3.append(pp)
        
		date = datetime.strptime(DataSet[j][2], '%d-%m-%Y')
		fontSize = 14
		if dx < 25:
			fontSize = 11
		if dx < 15:
			fontSize = 10
		canvas.create_text(x0+dx*j, 2 * y0 + 45,text=date.strftime('%d\n-\n%m'),font= ("Arial", fontSize), justify = "center") #подписываем даты на графике DataSet[j][2]
		j=j+1
		if j == duration:
			break
        
    #выводим график
	canvas.create_line(points1,fill="blue",smooth=1)
	canvas.create_line(points2,fill="green",smooth=1)
	canvas.create_line(points3,fill="red",smooth=1)
    
    # рисуем координатные оси
	y_axe=[]
	yy=(x0,0)
	y_axe.append(yy)
	yy=(x0,2 * y0)
	y_axe.append(yy)
	canvas.create_line(y_axe,fill="black",width=2)
    #
	x_axe=[]
	xx=(x0,y0)
	x_axe.append(xx)
	xx=(x1,y0)
	x_axe.append(xx)
	canvas.create_line(x_axe,fill="black",width=2)
    #
    #y1=10
    #y2=610
    #dx=30
	j=1
	i=0
	for n in range(10, 2 * y0 + 10, dy * 10):
		if n < y0:
			canvas.create_text(25, y0 - (10 - i) * dy * 10, fill="black",text=(10-i)*10)
			i=i+1
		if n == y0:
			canvas.create_text(25, y0,fill="black", text=0)
		if n > y0:
			canvas.create_text(25, y0 + j * dy * 10, fill="black",text=-j*10)
			j=j+1 
		if j == 11:
			break   
    #
	canvas.create_text(x0, screen_height - 90, fill="blue", text="- физическое состояние", font=("Arial", 16), anchor = tkinter.W)
	canvas.create_text(int((x1 - x0) / 2), screen_height - 90, fill="green",text="- эмоциональное состояние", font=("Arial", 16), anchor = tkinter.W)
	canvas.create_text(x1 - x0, screen_height - 90, fill="red",text="- интеллектуальное состояние", font=("Arial", 16), anchor = tkinter.E)
    #
	tk.mainloop()
