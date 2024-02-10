from tkinter import *


win = Tk()
win.title('a game window')
# exit function 
def Exit():
    win.destroy()
# help function 
def hell():
    global x 
    global y
    global screen_width
    global screen_height
    top_width = 200
    top_height = 200
    top = Toplevel()
    top.geometry(f'{top_width}x{top_height}+{int(x)}+{int(y)}')
    top.title('help')
# start function change color
def start_function():
    win.destroy()
    global v_get
    if v_get == True:
        # window geometry 
        win2 = Tk()
        global x 
        global y
        global screen_width
        global screen_height
        global screen_width
        global screen_height
        win2.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
        # radio buttons
        vari = IntVar(win2,0)
        radios = {'blue' : 1 , 'red' : 2 , 'yellow' : 3 , 'green' : 4}
        bg_rediobutton = 'red'
        for txt , val in radios.items():
            Radiobutton(win2,text=txt,variable=vari,value=val).pack(side=TOP,pady= 10)
        def select_function():
            global bg_rediobutton
            vary_get = int(vari.get())
            if vary_get == 1:
                win2.config(bg='blue')
            elif vary_get == 2:
                win2.config(bg='red')
            elif vary_get == 3:
                win2.config(bg='yellow')
            elif vary_get == 4:
                win2.config(bg='green')
        # buttons
        select_btn = Button(win2,text='Select',width=10,height=1,command=select_function)
        select_btn.place(x=150 , y=250)
        win2.mainloop()

# labels
main_label = Label(win,text='Select an option and press start ',font='sens 12 bold')
main_label.place(x = 80 , y = 60)

# buttons 
btn_start = Button(win,text='Start',width=10,height=1,command=start_function)
btn_start.place(x=70 , y=250)

btn_exit = Button(win,text='Exit',width=10,height=1,command=Exit)
btn_exit.place(x=250 , y=250)

btn_help = Button(win,text='Help',width=10,height=1,command=hell)
btn_help.place(x=160 , y=320)
# geometry 
screen_width = win.winfo_screenwidth() 
screen_height = win.winfo_screenheight() 
window_width = 400
window_height = 400
x = (screen_width - window_width) / 2
y = (screen_height - window_height) / 2
win.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
win.resizable(0,0)
# radio buttons
v = IntVar(win,1)
v_get = v.get()
options = {'chngecolor' : 1 , 'game' : 2}
for txt , val in options.items():
    Radiobutton(win , text= txt , variable=v ,value=val).pack(side=LEFT , padx=55)
win.mainloop()