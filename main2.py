from tkinter import *
from tkinter.messagebox import showinfo
from random import *
# window
main = Tk()
main.title('game page')
# functions
def time_func():
    global time
    if time > 0:
        time_botton.config(state=DISABLED)
        time -= 1
        time_label.config(text= time)
    time_label.after(1000,time_func)
    if time == 0:
        time_label.destroy()
        showinfo('time is out', 'your time is run out')
    
    
        
def question_generator():
    random_num1 = randint(0,5)
    random_num2 = randint(0,5)
    random_char = choice(['+','-','/','*'])
    question = f'{random_num1} {random_char} {random_num2}'
    qeustion_label.config(text= question)



def right_wrong():
    pass



# labels
time = 60
time_label = Label(main,text= time )
time_label.place(x=370)
qeustion_label = Label(main,text='')
qeustion_label.pack(side=TOP)
score_label = Label(main, text=f'score : ' )
score_label.place(x=0 , y=0)
# geometry
screen_width = main.winfo_screenwidth() 
screen_height = main.winfo_screenheight() 
window_width = 400
window_height = 300
x = (screen_width - window_width) / 2
y = (screen_height - window_height) / 2
main.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
main.resizable(0,0)
# bottons 
time_botton = Button(main,text='start ',command=time_func,width=6,height=1)
time_botton.place(x=220 , y= 210)
select_botton = Button(main,text='slect ',command=time_func,width=6,height=1)
select_botton.place(x=130 , y= 210)
next_botton = Button(main,text='next',command=question_generator,width=6,height=1)
next_botton.place(x=176 , y= 250)
# radio button
v = IntVar(main,0)
option = {'one' : 1 , 'two' : 2 , 'three' : 3 , 'four' : 4 }
for txt , val in option.items():
    Radiobutton(text=txt , value= val , variable= v).pack(side=LEFT , padx= 20)
main.mainloop()