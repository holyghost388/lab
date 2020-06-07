import tkinter



class ui:
    def __init__(self):
        self.root=tkinter.Tk()
        self.root.geometry('600x480')
        self.head_lab = tkinter.Label(text='后台系统', font=('黑体', 20)).place(x=200, y=20, width=200, height=70)
        self.us_lit_but=tkinter.Button(text='用户列表', font=('黑体', 20)).place(x=200,y=110,width=200,height=70)
        self.onli_lit_but=tkinter.Button(text='在线列表',font=('黑体', 20)).place(x=200, y=190, width=200, height=70)
        self.log_lit_but = tkinter.Button(text='日志', font=('黑体', 20)).place(x=200, y=270, width=200, height=70)
        self.clo_lit_but = tkinter.Button(text='关闭', font=('黑体', 20)).place(x=200, y=350, width=200, height=70)
        self.root.mainloop()



a=ui()