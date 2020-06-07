import tkinter



class ui:
    def __init__(self):
        self.root=tkinter.Tk()
        self.root.geometry('600x480')
        self.head_lab = tkinter.Label(text='welcome', font=('黑体', 20)).place(x=200, y=20, width=200, height=70)
        self.us_lit_but = tkinter.Button(text='登入', font=('黑体', 20)).place(x=200, y=110, width=200, height=70)
        self.onli_lit_but = tkinter.Button(text='注册', font=('黑体', 20)).place(x=200, y=230, width=200, height=70)
        self.root.mainloop()



a=ui()