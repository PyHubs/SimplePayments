from tkinter import*
root = Tk()

root.configure(background="Lightgreen")
Label(root, text="Welcome to simple payments", bg="Lightgreen", font="calibri 40 bold").pack()
Label(root, text="Version 4.0", bg="Lightgreen", font="calibri 20 bold").pack()
root.title("simple payment for windows")

# going to work on the trnafser option
# going to work on the trnafser option

Label(root, text="Transfer", bg="lightgreen", font="calibri 20 bold underline").pack() # Transfer
Label(root, text="To:", bg="lightgreen", font="calibri 16 bold").pack() # to:
to = Entry(root, bg="lightgreen").pack() #input for to
Label(root, text="From:", bg="lightgreen", font="calibri 16 bold").pack() # From:
From = Entry(root, bg="lightgreen").pack() #input for from
root.geometry("700x600")
Label(root, text="Amount:", bg="lightgreen", font="calibri 16 bold").pack() # Amount:
Amount = Entry(root, bg="lightgreen").pack()  # input for ammount
Label(root, text="SendOTP:", bg="lightgreen", font="calibri 16 bold").pack()  #SendOTP
SendOTP = Entry(root, bg="lightgreen").pack()  # input for SendOTP
Label(root, text="OTP:", bg="lightgreen", font="calibri 16 bold").pack()  # OTP
OTP = Entry(root, bg="lightgreen").pack()  # input for OTP
Label(root, text="Resend OTP:", bg="lightgreen", font="calibri 16 bold").pack()  # Resend OTP
ResendOTP = Entry(root, bg="lightgreen").pack()  # input for resend OTP
Label(root, text="Remarks:", bg="lightgreen", font="calibri 16 bold").pack()  # S
remarksLOLpackage = Entry(root, width=70 ,bg="lightgreen").pack()  # input for remarksLOLpackage
Label(root, text="", bg="lightgreen", font="calibri 16 bold").pack()  # S
submit_hah_payment = Button (root, text="Submit payment", font="None 18")
submit_hah_payment.pack()

root.iconbitmap("D:\Izu\python icon sets\SPX.ico")
root.mainloop()