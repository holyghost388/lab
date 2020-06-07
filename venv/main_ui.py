import tkinter

class ui:
    def __init__(self):
        self.root=tkinter.Tk()
        self.root.geometry('600x480')
        self.var_name=tkinter.StringVar
        self.var_addr=tkinter.StringVar
        self.head_lab = tkinter.Label(text='主界面', font=('黑体', 20)).place(x=200, y=20, width=200, height=70)

        self.nam_lab = tkinter.Label(text='用户名', font=('黑体', 15)).place(x=100, y=100, width=80, height=40)
        self.add_lab=tkinter.Label(text='地址',font=('黑体',15)).place(x=100,y=200,width=80,height=40)
        self.nam_ent = tkinter.Entry(textvariable=self.var_name, font=('黑体', 15)).place(x=200, y=100, width=250,height=40)
        self.add_ent = tkinter.Entry(textvariable=self.var_addr, font=('黑体', 15)).place(x=200, y=200, width=250,height=40)
        self.close_but = tkinter.Button(text='关闭', font=('黑体', 15)).place(x=225, y=330, width=150, height=50)

        self.root.mainloop()



a=ui()