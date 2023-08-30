#ЗАГРУЗЖАЕМ БИБЛИОТЕКУ
import tkinter as tk

# МЕТОДЫ
from tkinter import *
from tkinter import messagebox
def calculate_bmi():
   kg = int(weight_tf.get())
   m = int(height_tf.get())/100
   bmi = kg/(m*m)
 
   messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует недостаточному весу')
       
window = Tk() #создаем окно приложения
window.title("Калькулятор расходов") #Название окна
window.geometry('500x500') #размер окна

frame = Frame(
   window,     #Обязательный параметр, который указывает окно для размещения Frame.
   padx = 10,  #Задаём отступ по горизонтали.
   pady = 10   #Задаём отступ по вертикали.
)
frame.pack(expand=True) #Не забываем позиционировать виджет в окне. Здесь используется метод pack. С помощью свойства expand=True указываем, что Frame заполняет весь контейнер, созданный для него.
#      --------  1* ВВЕДИТЕ СВОЙ РОСТ
height_lb = Label(
   frame,
   text="Введите свой рост (в см)  "
)
#      --------  ОКНО ВВОДА ДЛЯ 1*
height_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
)
height_tf.grid(row=3, column=2)

#      --------  2* ВВЕДИТЕ СВОЙ РОСТ

height_lb.grid(row=3, column=1)
weight_lb = Label(
   frame,
   text="Введите свой вес (в кг)  ",
)
weight_lb.grid(row=4, column=1)

#      --------  ОКНО ВВОДА ДЛЯ 2*
weight_tf = Entry(
   frame,
)
weight_tf.grid(row=4, column=2, pady=5)

# ---------------
cal_btn = Button(
   frame, #Заготовка с настроенными отступами.
   text='Рассчитать ИМТ', #Надпись на кнопке.
   command = calculate_bmi
)
cal_btn.grid(row=5, column=2) #Размещаем кнопку в ячейке, расположенной ниже, чем наши надписи, но во втором столбце, то есть под ячейками для ввода информации.


window.mainloop()



# def clicked():  
#     lbl.configure(text="Я же просил...")  
  
  
# window = Tk()  
# window.title("Добро пожаловать в приложение PythonRu")  
# window.geometry('400x250')  
# lbl = Label(window, text="Привет")  
# lbl.grid(column=0, row=0)  
# txt = Entry(window,width=10)  
# txt.grid(column=1, row=0)  
# btn = Button(window, text="Не нажимать!", command=clicked)  
# btn.grid(column=2, row=0)  
# window.mainloop()
