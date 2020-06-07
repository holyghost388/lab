import tkinter

class ui:
    def __init__(self):
        self.root=tkinter.Tk()
        self.root.geometry('600x480')


        self.var_name=tkinter.StringVar
        self.var_pwd=tkinter.StringVar

        self.var_send_pin=tkinter.StringVar
        self.var_get_pin=tkinter.StringVar



        self.head_lab = tkinter.Label(text='登入系统', font=('黑体', 20)).place(x=200, y=20, width=200, height=70)

        self.nam_lab = tkinter.Label(text='用户名', font=('黑体', 15)).place(x=100, y=100, width=80, height=40)
        self.pwd_lab = tkinter.Label(text='密码', font=('黑体', 15)).place(x=100, y=160, width=80, height=40)
        self.pin_lab = tkinter.Label(text='验证码', font=('黑体', 15)).place(x=100, y=220, width=80, height=40)

        self.nam_ent = tkinter.Entry(textvariable=self.var_name, font=('黑体', 15)).place(x=200, y=100, width=250, height=40)
        self.pwd_ent= tkinter.Entry(textvariable=self.var_pwd, font=('黑体', 15)).place(x=200, y=160, width=250, height=40)
        self.pin_ent = tkinter.Entry(textvariable=self.var_send_pin, font=('黑体', 15)).place(x=200, y=220, width=140, height=40)

        self.pin_but = tkinter.Button(textvariable=self.var_get_pin, bg='red').place(x=360, y=220, width=90, height=40)

        self.sign_but = tkinter.Button(text='注册', font=('黑体', 15)).place(x=120, y=330, width=150, height=50)
        self.lgoin_but = tkinter.Button(text='登入', font=('黑体', 15)).place(x=300, y=330, width=150, height=50)

        self.root.mainloop()




a=ui()