from tkinter import*
from tkinter import messagebox

#root
root = Tk()
root.configure(bg="#82edba")
root.title("Simple payment X2")
root.geometry("700x650")
root.iconbitmap("D:\Izu\python icon sets\SPL.ico")

#Transfer
def Transfer_command():
    #window
    Window = Toplevel()
    Window.title("Simple payment X2 - Transfer")
    Window.configure(bg='#82edba')
    Window.geometry("500x500")
    Window.iconbitmap("D:\Izu\python icon sets\SPL.ico")
    #globalation 
    global tox
    global From
    global Amount
    global OTP_Method
    global OTP
    global Resend_OTP
    #transfer
    Label(Window, text="Transfer", bg="#82edba", font="Comfortaa 24 bold underline").pack() #Name
    #tox
    Label(Window, text="To:", bg="#82edba", font="Comfortaa 15").pack() # to:
    clicked = StringVar()
    clicked.set("Izkaan")
    tox = OptionMenu (Window, clicked, "Izkaan", "Dad", "Mom", "Kayan")
    tox.pack()
    tox.configure(bg="#82edba")
    #From
    Label(Window, text="From:", bg="#82edba", font="Comfortaa 15").pack() # Frome
    axe = StringVar()
    axe.set("Dad")
    From = OptionMenu (Window, axe, "Izkaan", "Dad", "Mom", "Kayan")
    From.pack()
    From.configure(bg="#82edba")
    #Amount
    Label(Window, text="Amount:", bg="#82edba", font="Comfortaa 15").pack() # tAmmount.org
    Amount  = Entry(Window, font="Calbari 13")
    Amount.configure(bg="#82edba")
    Amount.pack()
    #OTP method
    Label(Window, text="OTP method:", bg="#82edba", font="Comfortaa 15").pack()
    Methodify = StringVar()
    Methodify.set('Email')
    OTP_Method = OptionMenu (Window, Methodify, "Email", "Skype message")
    OTP_Method.configure(bg="#82edba")
    OTP_Method.pack()
    #OTP
    Label(Window, text="OTP:", bg="#82edba", font="Comfortaa 15").pack()
    OTP  = Entry(Window, font="Calbari 13")
    OTP.configure(bg="#82edba")
    OTP.pack()
    #ResendOTP
    Label(Window, text="Resend OTP:", bg="#82edba", font="Comfortaa 15").pack()
    Xman = StringVar()
    Xman.set('Email')
    Resend_OTP = OptionMenu (Window, Xman, "Yes", "No")
    Resend_OTP.configure(bg="#82edba")
    Resend_OTP.pack()

    #Submit Payment acter
    submit_payment_btn= Button(Window, text="Submit payment", font=("Comfortaa", "17"), command=submit_payment_action)
    submit_payment_btn.pack(pady=20)
    submit_payment_btn.configure(background="#b9fac9")

def submit_payment_action():
    submiting = messagebox.askyesno("Payment", "Are you sure you want to submit your payment?")
    if submiting:
        messagebox.showinfo("Payment", "Your payment has been submited")
    else:
        messagebox.showinfo("Payment", "Your payment has not been submited")

def Show_info():
    messagebox.showinfo("Version", "Simple payment X2, made by izkaan on 8/28/2020")

def registration_process():
    Registerwindow = Toplevel()
    Registerwindow.title("Simple payment X2 - Transfer")
    Registerwindow.configure(bg='#82edba')
    Registerwindow.geometry("500x500")
    Registerwindow.iconbitmap("D:\Izu\python icon sets\SPL.ico")

    Label(Registerwindow, text="Register into simple payment", font=("Comfortaa", "25"),  bg="#82edba").pack()

    Label(Registerwindow, text="Username", font=("Comfortaa", "19"),  bg="#82edba").pack()
    User_name  = Entry(Registerwindow, font="Calbari 13")
    User_name.configure(bg="#82edba")
    User_name.pack()

    Label(Registerwindow, text="Email", font=("Comfortaa", "19"),  bg="#82edba").pack()
    email_name  = Entry(Registerwindow, font="Calbari 13")
    email_name.configure(bg="#82edba")
    email_name.pack()

    Label(Registerwindow, text="Password", font=("Comfortaa", "19"),  bg="#82edba").pack()
    eps_name  = Entry(Registerwindow, font="Calbari 13")
    eps_name.configure(bg="#82edba")
    eps_name.pack()

    Label(Registerwindow, text="Custom PIN", font=("Comfortaa", "19"),  bg="#82edba").pack()
    Custom_pin  = Entry(Registerwindow, font="Calbari 13")
    Custom_pin.configure(bg="#82edba")
    Custom_pin.pack()

    Make_account_btn= Button(Registerwindow, text="Make account", font=("Comfortaa", "17"), command=submit_account_messagebox)
    Make_account_btn.pack(pady=20)
    Make_account_btn.configure(background="#b9fac9")

def submit_account_messagebox():
    submiting = messagebox.askyesno("Account", "Are you sure you want to make this account?")
    if submiting:
        messagebox.showinfo("Account", "Your account has been made, it will be possible to use it the next day")
    else:
        messagebox.showinfo("Account", "Your account has not been made")

#home frame
Home_frame = Frame(root)
Home_frame.pack()
Home_frame.configure(bg="#82edba")

#Homescreen label
Label(Home_frame, text="Simple payment X2", bg="#82edba", font=("Comfortaa", "40")).pack()
Label(Home_frame,text="Windows X2 edition", bg="#82edba", font=("Comfortaa", "22")).pack()
Label(Home_frame,text="", bg="#82edba", font=("Comfortaa", "22")).pack()
Label(Home_frame,text="Menu options", bg="#82edba", font=("Comfortaa", "30")).pack()

#buttons
Make_transfer_button = Button(root, text="Make a transfer", font=("Comfortaa", "17"), command=Transfer_command)
Make_transfer_button.pack(pady=10)
Make_transfer_button.configure(background="#b9fac9")

Version = Button(root, text="Simple payment version",  font=("Comfortaa", "17"), command = Show_info)
Version.pack(pady=10)
Version.configure(background="#b9fac9")

register_button = Button(root, text="Register into simple payment",  font=("Comfortaa", "17"), command = registration_process)
register_button.pack(pady=10)
register_button.configure(background="#b9fac9")

end= Button(root, text="Quit program",  font=("Comfortaa", "17"), command=root.destroy)
end.pack(pady=10)
end.configure(background="#b9fac9")

root.mainloop()
